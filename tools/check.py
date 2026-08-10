#!/usr/bin/env python3
"""Prueft die Zusagen aus docs/superpowers/specs/2026-08-10-growth-lab-blueprint-design.md."""
import html
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEITEN = ["index.html", "impressum.html", "datenschutz.html", "agb.html",
          "haftungsausschluss.html"]
CSS_DATEIEN = ["styles.css", "assets/fonts/fonts.css"]

# Belege, die laut Auftraggeber erfunden sind und nirgends mehr auftauchen duerfen.
VERBOTEN = ["Lena", "Marco", "+133", "3.4x", "3,4x", "67 Tage", "92%", "92 %",
            "Skala", "Kinetic Noir", "Space Grotesk",
            # Agenturvokabular: Diese Seite beschreibt ein Coaching, keine Agentur.
            "SEO", "Paid Media", "CPC", "CPL", "Werbekonto", "Werbebudget",
            "Kampagne", "Retainer", "Ranking", "Ads-Management", "Newsletter",
            "Suchmaschinen-Platzierung", "Case Stud"]
PLATZHALTER = ["TODO", "TBD", "Lorem ipsum", "XXX", "PLATZHALTER"]
# Erlaubte externe Ziele: nur nutzerinitiiert.
ERLAUBT_EXTERN = ["calendly.com", "mailto:", "tel:"]
# Einzige zulaessigen Geld- und Zeitraumangaben auf index.html.
ERLAUBTE_ZAHLEN = ["3.000 €", "8.000 €", "6 Monate"]

fehler = []


def lies(pfad):
    with open(os.path.join(WURZEL, pfad), encoding="utf-8") as f:
        return f.read()


def text_von(roh):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", roh)))


def pruefe_seite_existiert():
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            fehler.append(f"{s}: Datei fehlt")


def pruefe_keine_fremdanfragen():
    muster = re.compile(r'(?:src|href)\s*=\s*["\'](https?://[^"\']+)', re.I)
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            continue
        for url in muster.findall(lies(s)):
            if not any(a in url for a in ERLAUBT_EXTERN):
                fehler.append(f"{s}: externe Ressource {url}")


def pruefe_verbotene_inhalte():
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            continue
        roh = lies(s)
        for wort in VERBOTEN + PLATZHALTER:
            if wort.lower() in roh.lower():
                fehler.append(f"{s}: verbotener Inhalt {wort!r}")


def pruefe_interne_links():
    muster = re.compile(r'(?:href|src)\s*=\s*["\']([^"\'#][^"\']*)["\']')
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            continue
        for ziel in muster.findall(lies(s)):
            if ziel.startswith(("http", "mailto:", "tel:", "#", "//")):
                continue
            pfad = os.path.join(WURZEL, ziel.split("#")[0].lstrip("/"))
            if not os.path.exists(pfad):
                fehler.append(f"{s}: toter Link/Ressource -> {ziel}")


def pruefe_keine_skripte():
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            continue
        roh = lies(s)
        if re.search(r"<\s*script", roh, re.I):
            fehler.append(f"{s}: enthaelt <script>")
        if re.search(r"<\s*iframe", roh, re.I):
            fehler.append(f"{s}: enthaelt <iframe>")


def pruefe_css():
    for pfad in CSS_DATEIEN:
        voll = os.path.join(WURZEL, pfad)
        if not os.path.exists(voll):
            fehler.append(f"{pfad}: Datei fehlt")
            continue
        with open(voll, encoding="utf-8") as f:
            inhalt = f.read()
        for treffer in re.findall(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)', inhalt):
            if treffer.startswith("//"):
                fehler.append(f"{pfad}: protokolllose URL {treffer!r}")
            elif treffer.startswith(("http://", "https://")):
                fehler.append(f"{pfad}: fremder Host in url() {treffer!r}")
        for treffer in re.findall(r'@import\s+["\']?([^"\';]+)', inhalt):
            if treffer.startswith("//") or treffer.startswith(("http://", "https://")):
                fehler.append(f"{pfad}: fremder Host in @import {treffer!r}")


def pruefe_zahlen():
    s = "index.html"
    if not os.path.exists(os.path.join(WURZEL, s)):
        return
    text = text_von(lies(s))
    muster = re.compile(r"\d[\d.,]*\s?€|\d+\s*Monate?\b")
    for treffer in muster.findall(text):
        if treffer not in ERLAUBTE_ZAHLEN:
            fehler.append(f"{s}: unzulaessige Zahlenangabe {treffer!r}")


def pruefe_kopfangaben():
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            continue
        roh = lies(s)
        if 'lang="de"' not in roh:
            fehler.append(f"{s}: lang=\"de\" fehlt")
        if not re.search(r"<title>[^<]{10,}</title>", roh):
            fehler.append(f"{s}: aussagekraeftiger <title> fehlt")
        if not re.search(r'name="description"\s+content="[^"]{30,}"', roh):
            fehler.append(f"{s}: meta description fehlt oder ist zu kurz")


def pruefe_marke():
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            continue
        if "Growth Lab Blueprint" not in lies(s):
            fehler.append(f"{s}: Markenname fehlt")


def pruefe_entfallene_dateien():
    for s in ["leistungen.html", "projekte.html", "überuns.html"]:
        if os.path.exists(os.path.join(WURZEL, s)):
            fehler.append(f"{s}: haette entfernt werden muessen")


def main():
    pruefe_seite_existiert()
    pruefe_keine_fremdanfragen()
    pruefe_verbotene_inhalte()
    pruefe_interne_links()
    pruefe_keine_skripte()
    pruefe_css()
    pruefe_zahlen()
    pruefe_kopfangaben()
    pruefe_marke()
    pruefe_entfallene_dateien()
    if fehler:
        print(f"FEHLGESCHLAGEN — {len(fehler)} Verstoesse:\n")
        for f in fehler:
            print("  -", f)
        return 1
    print("BESTANDEN — alle Bedingungen erfuellt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
