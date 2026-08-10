# Growth Lab Blueprint — Umsetzungsplan

> **Für agentische Bearbeiter:** ERFORDERLICHE SUB-SKILL: `superpowers:subagent-driven-development`
> (empfohlen) oder `superpowers:executing-plans`, um diesen Plan Aufgabe für Aufgabe
> umzusetzen. Schritte nutzen Checkbox-Syntax (`- [ ]`) zur Nachverfolgung.

**Ziel:** Die bestehende Skala-Website lokal zu einem hellen, seriösen One-Pager namens
Growth Lab Blueprint umbauen, der sowohl B2B-Interessenten überzeugt als auch einer
Compliance-Prüfung durch Bank oder Zahlungsanbieter standhält.

**Architektur:** Statisches HTML ohne Build-Schritt. Ein `index.html` als One-Pager, vier
Rechtsseiten, eine gemeinsame `styles.css` mit CSS-Custom-Properties als Design-Tokens.
Sämtliche Ressourcen liegen im Repo — beim Seitenaufruf geht keine einzige Anfrage an
einen fremden Server.

**Tech-Stack:** HTML5, handgeschriebenes CSS (ersetzt Tailwind-CDN), lokal eingebundene
Webfonts (Source Serif 4, Inter), Python 3 für das Prüfskript und den lokalen Server.

## Globale Vorgaben

Diese Bedingungen gelten für **jede** Aufgabe.

- **Nichts pushen, nichts deployen, keine Domain kaufen.** Ausschließlich lokale Arbeit im
  Repo `~/Downloads/capitalcouncilmarketing`. Lokale Commits sind erwünscht.
- **Keine Fremdanfragen beim Seitenaufruf.** Keine CDNs, keine Google Fonts von Google,
  kein Analytics, keine externen Bilder. Einzige Ausnahme: der Calendly-Link, der erst
  nach einem Klick des Besuchers geladen wird.
- **Nichts erfinden.** Keine Zahlen, Namen, Fallbeispiele, Kundenstimmen oder Belege, die
  nicht vom Auftraggeber geliefert wurden. Fehlt eine Angabe, bleibt der Abschnitt
  ungebaut — siehe „Offene Eingaben".
- **Sprache:** Deutsch, `lang="de"`.
- **Marke:** Growth Lab Blueprint. Rechtsträger: 28 Capital Council LLC, Sheridan, WY, USA.
  Gesicht: Claudio Fuersatz. „Skala" darf nirgends mehr vorkommen.
- **„LinkedIn"** darf im Fließtext frei verwendet werden, aber nicht im Markennamen,
  im Seitentitel als Marke oder in Dateinamen.
- **Farben, exakt:** Hintergrund `#F7F9FC` · Flächen `#FFFFFF` · Rand `#E3E8EF` ·
  Text `#0A2540` · Nebentext `#5B6B7F` · Primär `#1B5FCC` · Hell-Akzent `#E8F0FE`.
  LinkedIns `#0A66C2` wird bewusst **nicht** verwendet.
- **Schriften:** Source Serif 4 (Überschriften), Inter (Fließtext). Beide lokal.
- **Preise:** Gruppencoaching 3.000 €, Einzelbetreuung 8.000 €.
- **Layout-Erbe:** Containerbreite 1200 px, Abschnittsabstand 140 px, Versal-Labels,
  Pill-Navigation.
- **Commit-Nachrichten** auf Deutsch, im Imperativ, ohne Präfixe wie `feat:`.

## Offene Eingaben

Fünf Angaben fehlen. Aufgaben, die davon abhängen, sind unten mit **GESPERRT** markiert
und dürfen nicht mit erfundenen Inhalten umgesetzt werden.

| # | Angabe | Sperrt |
|---|---|---|
| 1 | Laufzeit, Zahlungsweise, Kündigungsfrist beider Pakete | Aufgabe 6, 10 |
| 2 | Claudios Werdegang | Aufgabe 8 |
| 3 | Echtes Porträtfoto von Claudio | Aufgabe 8 |
| 4 | Telefonnummer | Aufgabe 9, 10 |
| 5 | Methodendetails: Phasen, Sitzungen, Materialien | Aufgabe 7 |

Aufgaben 1–5 sind vollständig unblockiert und sollten zuerst laufen.

## Dateistruktur

| Datei | Zuständigkeit |
|---|---|
| `index.html` | One-Pager, neun Abschnitte |
| `impressum.html` | Anbieterkennzeichnung, Marke aktualisiert |
| `datenschutz.html` | um Calendly/Fonts/Hosting ergänzt, Analytics gestrichen |
| `agb.html` | inhaltlich neu: Coaching statt Agenturleistungen |
| `haftungsausschluss.html` | Marke aktualisiert, Haftungstexte übernommen |
| `styles.css` | sämtliche Styles: Tokens, Grundlagen, Bausteine, Abschnitte |
| `assets/fonts/` | Schriftdateien + `fonts.css` mit lokalen Pfaden |
| `assets/img/` | Stockfotos, Porträt, Favicon |
| `tools/check.py` | Prüfskript: hält die Zusagen der Spec als Bedingungen fest |
| `DESIGN.md` | neues Designsystem, ersetzt „Kinetic Noir" |
| `README.md` | derzeit leer; Aufbau, lokale Vorschau, Prüfung |

**Entfallen:** `leistungen.html`, `projekte.html`, `überuns.html`.

---

### Aufgabe 1: Prüfskript anlegen

Das Skript hält die Zusagen der Spec fest. Es läuft nach jeder weiteren Aufgabe und
schlägt fehl, solange etwas dagegen verstößt. Anfangs **muss** es fehlschlagen — die alte
Seite verletzt fast jede Bedingung.

**Dateien:**
- Anlegen: `tools/check.py`

**Schnittstellen:**
- Erzeugt: Kommando `python3 tools/check.py`, Rückgabewert 0 bei Erfolg, 1 bei Verstoß.
  Alle folgenden Aufgaben nutzen es als Abnahmekriterium.

- [ ] **Schritt 1: Prüfskript schreiben**

```python
#!/usr/bin/env python3
"""Prueft die Zusagen aus docs/superpowers/specs/2026-08-10-growth-lab-blueprint-design.md."""
import html
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEITEN = ["index.html", "impressum.html", "datenschutz.html", "agb.html",
          "haftungsausschluss.html"]

# Belege, die laut Auftraggeber erfunden sind und nirgends mehr auftauchen duerfen.
VERBOTEN = ["Lena", "Marco", "+133", "3.4x", "3,4x", "67 Tage", "92%", "92 %",
            "Skala", "Kinetic Noir", "Space Grotesk"]
PLATZHALTER = ["TODO", "TBD", "Lorem ipsum", "XXX", "PLATZHALTER"]
# Erlaubte externe Ziele: nur nutzerinitiiert.
ERLAUBT_EXTERN = ["calendly.com", "mailto:", "tel:"]

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
    muster = re.compile(r'href\s*=\s*["\']([^"\'#][^"\']*)["\']')
    for s in SEITEN:
        if not os.path.exists(os.path.join(WURZEL, s)):
            continue
        for ziel in muster.findall(lies(s)):
            if ziel.startswith(("http", "mailto:", "tel:", "#", "//")):
                continue
            pfad = os.path.join(WURZEL, ziel.split("#")[0].lstrip("/"))
            if not os.path.exists(pfad):
                fehler.append(f"{s}: toter Link -> {ziel}")


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
```

- [ ] **Schritt 2: Skript laufen lassen und Fehlschlag bestätigen**

Ausführen: `cd ~/Downloads/capitalcouncilmarketing && python3 tools/check.py`

Erwartet: `FEHLGESCHLAGEN` mit zahlreichen Verstößen — externe Ressourcen (Tailwind,
Google Fonts, Analytics), verbotene Inhalte („Skala", „Lena", „Marco"), noch vorhandene
Dateien `leistungen.html`, `projekte.html`, `überuns.html`. Das ist der korrekte
Ausgangszustand.

- [ ] **Schritt 3: Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git add tools/check.py
git commit -m "Prüfskript für die Zusagen der Design-Spec anlegen"
```

---

### Aufgabe 2: Schriften lokal einbinden

**Dateien:**
- Anlegen: `assets/fonts/fonts.css` und die zugehörigen `.woff2`-Dateien

**Schnittstellen:**
- Erzeugt: `assets/fonts/fonts.css` mit `@font-face`-Regeln für `Source Serif 4`
  (Gewichte 400, 600, 700) und `Inter` (400, 500, 600). Alle `url()` zeigen relativ auf
  Dateien im selben Verzeichnis. `styles.css` bindet diese Datei in Aufgabe 3 ein.

- [ ] **Schritt 1: Verzeichnis anlegen und Schrift-CSS holen**

```bash
cd ~/Downloads/capitalcouncilmarketing
mkdir -p assets/fonts assets/img tools
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
curl -s -H "User-Agent: $UA" \
  'https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&family=Inter:wght@400;500;600&display=swap' \
  -o assets/fonts/fonts.css
head -5 assets/fonts/fonts.css
```

Erwartet: `@font-face`-Blöcke mit `url(https://fonts.gstatic.com/...)` und `format('woff2')`.

- [ ] **Schritt 2: Schriftdateien herunterladen und Pfade lokal umbiegen**

```bash
cd ~/Downloads/capitalcouncilmarketing
grep -oE 'https://fonts\.gstatic\.com[^)]+' assets/fonts/fonts.css | sort -u | while read -r u; do
  curl -s "$u" -o "assets/fonts/$(basename "$u")"
done
sed -i '' -E 's#https://fonts\.gstatic\.com/[^)]*/#./#g' assets/fonts/fonts.css
ls assets/fonts/*.woff2 | wc -l
grep -c 'gstatic' assets/fonts/fonts.css || true
```

Erwartet: mindestens 6 `.woff2`-Dateien; die `grep`-Zählung auf `gstatic` ergibt `0`.

- [ ] **Schritt 3: Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git add assets/fonts
git commit -m "Source Serif 4 und Inter lokal einbinden"
```

---

### Aufgabe 3: Design-Tokens und Grundlagen in styles.css

**Dateien:**
- Anlegen: `styles.css`

**Schnittstellen:**
- Erzeugt: CSS-Custom-Properties, auf die alle späteren Abschnitte zugreifen —
  `--bg`, `--flaeche`, `--rand`, `--text`, `--text-leise`, `--primaer`, `--akzent`,
  `--breite` (1200px), `--abstand-abschnitt` (140px).
- Erzeugt: Klassen `.container`, `.label`, `.knopf`, `.knopf-primaer`, `.karte`,
  `.abschnitt`. Aufgaben 5–9 verwenden ausschließlich diese Bausteine.

- [ ] **Schritt 1: styles.css schreiben**

```css
@import url("./assets/fonts/fonts.css");

:root {
  --bg: #F7F9FC;
  --flaeche: #FFFFFF;
  --rand: #E3E8EF;
  --text: #0A2540;
  --text-leise: #5B6B7F;
  --primaer: #1B5FCC;
  --akzent: #E8F0FE;
  --breite: 1200px;
  --abstand-abschnitt: 140px;
  --radius: 12px;
  --radius-pill: 999px;
}

*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: "Inter", system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3 {
  font-family: "Source Serif 4", Georgia, serif;
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin: 0 0 0.5em;
}

h1 { font-size: clamp(2.5rem, 6vw, 4.5rem); }
h2 { font-size: clamp(1.9rem, 4vw, 3rem); }
h3 { font-size: 1.35rem; }

p { margin: 0 0 1.1em; max-width: 65ch; }
a { color: var(--primaer); }

.container {
  width: 100%;
  max-width: var(--breite);
  margin: 0 auto;
  padding: 0 24px;
}

.abschnitt { padding: var(--abstand-abschnitt) 0; }
.abschnitt--akzent { background: var(--akzent); }

.label {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--primaer);
  margin-bottom: 1rem;
  display: block;
}

.knopf {
  display: inline-block;
  padding: 14px 28px;
  border-radius: var(--radius-pill);
  border: 1px solid var(--rand);
  background: var(--flaeche);
  color: var(--text);
  text-decoration: none;
  font-weight: 500;
  transition: background 0.2s, border-color 0.2s;
}

.knopf:hover { border-color: var(--primaer); }

.knopf-primaer {
  background: var(--primaer);
  border-color: var(--primaer);
  color: #fff;
}

.knopf-primaer:hover { background: #164FA8; border-color: #164FA8; }

.karte {
  background: var(--flaeche);
  border: 1px solid var(--rand);
  border-radius: var(--radius);
  padding: 32px;
}

/* Einheitliche Bildbehandlung: laesst Stockmaterial verschiedener Herkunft
   wie eine Serie wirken. Statt die Dateien zu bearbeiten, liegt der Blaustich
   als Ueberlagerung darueber. */
.bild {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius);
}

.bild img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: saturate(0.7) contrast(1.02);
}

.bild::after {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--primaer);
  opacity: 0.16;
  mix-blend-mode: color;
  pointer-events: none;
}

@media (max-width: 720px) {
  :root { --abstand-abschnitt: 80px; }
  body { font-size: 16px; }
  .karte { padding: 24px; }
}
```

- [ ] **Schritt 2: Prüfen, dass die Schriften lokal geladen werden**

```bash
cd ~/Downloads/capitalcouncilmarketing
grep -c 'gstatic\|googleapis' styles.css assets/fonts/fonts.css
```

Erwartet: für beide Dateien `0`.

- [ ] **Schritt 3: Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git add styles.css
git commit -m "Design-Tokens und Grundbausteine in styles.css anlegen"
```

---

### Aufgabe 4: Seitengerüst und Aufräumen

Ersetzt `index.html` durch ein leeres Gerüst mit Navigation und Fuß und entfernt die drei
entfallenden Seiten. Danach steht das Grundgerüst, in das die Aufgaben 5–9 ihre
Abschnitte einsetzen.

**Dateien:**
- Ersetzen: `index.html`
- Löschen: `leistungen.html`, `projekte.html`, `überuns.html`

**Schnittstellen:**
- Erzeugt: `index.html` mit `<main>` als Einhängepunkt. Jeder spätere Abschnitt wird als
  `<section id="...">` direkt in `<main>` eingefügt, in der Reihenfolge der Spec.
- Erzeugt: Navigations-Anker `#fuer-wen`, `#methode`, `#preis`, `#ueber-uns`, `#kontakt`.

- [ ] **Schritt 1: Alte Seiten entfernen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git rm -q leistungen.html projekte.html
git rm -q "$(git ls-files | grep beruns)"
git status --short
```

Erwartet: drei Löschungen, danach meldet `git status` keine unversionierte
`überuns.html` mehr — das Unicode-Problem ist damit erledigt.

- [ ] **Schritt 2: index.html als Gerüst schreiben**

```html
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Growth Lab Blueprint | Kunden über LinkedIn für B2B-Dienstleister</title>
<meta name="description" content="Wir zeigen B2B-Dienstleistern, Beratungen und Agenturen, wie sie über LinkedIn planbar Kunden gewinnen — als Gruppencoaching oder in der Einzelbetreuung.">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<header class="kopf">
  <div class="container kopf__inner">
    <a class="marke" href="/">Growth Lab Blueprint</a>
    <nav class="nav">
      <a href="#fuer-wen">Für wen</a>
      <a href="#methode">Methode</a>
      <a href="#preis">Preis</a>
      <a href="#ueber-uns">Über uns</a>
      <a class="knopf knopf-primaer" href="#kontakt">Erstgespräch</a>
    </nav>
  </div>
</header>

<main>
  <!-- Abschnitte folgen in Aufgabe 5 bis 9 -->
</main>

<footer class="fuss">
  <div class="container">
    <p class="fuss__marke">Growth Lab Blueprint</p>
    <p class="fuss__traeger">28 Capital Council LLC · Sheridan, WY 82801 · Vereinigte Staaten</p>
    <nav class="fuss__links">
      <a href="impressum.html">Impressum</a>
      <a href="datenschutz.html">Datenschutz</a>
      <a href="agb.html">AGB</a>
      <a href="haftungsausschluss.html">Haftungsausschluss</a>
    </nav>
  </div>
</footer>

</body>
</html>
```

- [ ] **Schritt 3: Styles für Kopf und Fuß an styles.css anhängen**

```css
.kopf {
  position: sticky;
  top: 0;
  z-index: 10;
  backdrop-filter: blur(12px);
  background: rgba(247, 249, 252, 0.85);
  border-bottom: 1px solid var(--rand);
}

.kopf__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  height: 72px;
}

.marke {
  font-family: "Source Serif 4", Georgia, serif;
  font-weight: 600;
  font-size: 1.15rem;
  color: var(--text);
  text-decoration: none;
}

.nav { display: flex; align-items: center; gap: 28px; }
.nav a { color: var(--text-leise); text-decoration: none; font-size: 15px; }
.nav a:hover { color: var(--text); }
.nav .knopf { color: #fff; }

.fuss {
  border-top: 1px solid var(--rand);
  padding: 56px 0;
  color: var(--text-leise);
  font-size: 15px;
}

.fuss__marke {
  font-family: "Source Serif 4", Georgia, serif;
  color: var(--text);
  margin-bottom: 4px;
}

.fuss__links { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 16px; }

@media (max-width: 720px) {
  .nav a:not(.knopf) { display: none; }
}
```

- [ ] **Schritt 4: Favicon anlegen**

```bash
cd ~/Downloads/capitalcouncilmarketing
python3 - <<'PY'
import struct, zlib
# 32x32 PNG in Primaerblau, damit der Favicon-Verweis nicht ins Leere zeigt.
b, g, r = 0xCC, 0x5F, 0x1B
zeilen = b"".join(b"\x00" + bytes([r, g, b]) * 32 for _ in range(32))
def brocken(typ, daten):
    return (struct.pack(">I", len(daten)) + typ + daten
            + struct.pack(">I", zlib.crc32(typ + daten) & 0xFFFFFFFF))
png = (b"\x89PNG\r\n\x1a\n"
       + brocken(b"IHDR", struct.pack(">IIBBBBB", 32, 32, 8, 2, 0, 0, 0))
       + brocken(b"IDAT", zlib.compress(zeilen))
       + brocken(b"IEND", b""))
open("assets/img/favicon.png", "wb").write(png)
print("Favicon geschrieben")
PY
```

- [ ] **Schritt 5: Prüfskript laufen lassen**

Ausführen: `python3 tools/check.py`

Erwartet: Verstöße für `index.html` sind verschwunden (keine externen Ressourcen, keine
verbotenen Wörter, Marke vorhanden, Links intakt, entfallene Dateien weg). Verbleibende
Verstöße betreffen nur noch die vier Rechtsseiten — die kommen in Aufgabe 10.

- [ ] **Schritt 6: Lokal ansehen**

```bash
cd ~/Downloads/capitalcouncilmarketing && python3 -m http.server 8080
```

Im Browser `http://localhost:8080` öffnen. Erwartet: heller Hintergrund, Serifen-Marke
oben links, Navigation rechts, Fußzeile mit vier Rechtslinks. Der Inhaltsbereich ist noch
leer — das ist korrekt. Server danach mit `Strg+C` beenden.

- [ ] **Schritt 7: Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git add -A
git commit -m "Seitengerüst mit Kopf und Fuß anlegen, alte Unterseiten entfernen"
```

---

### Aufgabe 5: Bildmaterial beschaffen

**Dateien:**
- Anlegen: `assets/img/hero.jpg`, `assets/img/arbeit.jpg`, `assets/img/gespraech.jpg`

**Schnittstellen:**
- Erzeugt: drei Bilddateien mit genau diesen Namen. Aufgabe 6 bindet `hero.jpg` ein,
  Aufgabe 7 `arbeit.jpg`, Aufgabe 9 `gespraech.jpg`.
- Die einheitliche Blaufärbung übernimmt die Klasse `.bild` aus Aufgabe 3. Die Dateien
  selbst werden **nicht** bearbeitet.

- [ ] **Schritt 1: Bilder auswählen und herunterladen**

Auf [unsplash.com](https://unsplash.com) suchen. Alle Bilder unterliegen der
Unsplash-Lizenz: kommerziell nutzbar, ohne Namensnennungspflicht.

| Datei | Suchbegriff | Motiv | Format |
|---|---|---|---|
| `hero.jpg` | `office daylight desk` | ruhiger Arbeitsplatz bei Tageslicht, keine Person im Fokus | quer, mind. 2000 px breit |
| `arbeit.jpg` | `person laptop focused` | eine Person konzentriert am Laptop | quer, mind. 1600 px |
| `gespraech.jpg` | `two people meeting table` | zwei Personen im Gespräch am Tisch | quer, mind. 1600 px |

**Ausschlusskriterien:** kein Händeschütteln, keine Konferenzräume mit Zeigefinger auf
Diagramme, keine Erfolgsposen, keine sichtbaren fremden Markenlogos, keine erkennbaren
LinkedIn-Oberflächen.

Heruntergeladene Dateien nach `assets/img/` legen und exakt wie oben benennen.

- [ ] **Schritt 2: Dateigrößen prüfen und bei Bedarf verkleinern**

```bash
cd ~/Downloads/capitalcouncilmarketing
ls -lh assets/img/*.jpg
for f in assets/img/*.jpg; do
  sips -Z 2000 "$f" --out "$f" >/dev/null && sips -s format jpeg -s formatOptions 72 "$f" --out "$f" >/dev/null
done
ls -lh assets/img/*.jpg
```

Erwartet: jede Datei unter 400 KB. `sips` ist auf macOS vorinstalliert.

- [ ] **Schritt 3: Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git add assets/img
git commit -m "Stockfotos für Hero, Methode und Kontakt aufnehmen"
```

---

### Aufgabe 6: Abschnitte 1 bis 3 — Hero, Für wen, Das Problem

**Dateien:**
- Ändern: `index.html` (in `<main>` einsetzen)
- Ändern: `styles.css` (Styles anhängen)

**Schnittstellen:**
- Verbraucht: `.container`, `.label`, `.knopf`, `.knopf-primaer`, `.karte`, `.abschnitt`,
  `.bild` aus Aufgabe 3; `assets/img/hero.jpg` aus Aufgabe 5.
- Erzeugt: Anker `#fuer-wen`, auf den die Navigation aus Aufgabe 4 verweist.

- [ ] **Schritt 1: Abschnitte in `<main>` einsetzen**

Den Kommentar `<!-- Abschnitte folgen in Aufgabe 5 bis 9 -->` ersetzen durch:

```html
<section class="hero">
  <div class="container hero__inner">
    <div class="hero__text">
      <span class="label">Für B2B-Dienstleister</span>
      <h1>Kunden gewinnen, ohne auf Empfehlungen zu warten.</h1>
      <p class="hero__lead">Wir zeigen Beratungen, Agenturen und B2B-Dienstleistern, wie
      sie über LinkedIn planbar Gespräche mit passenden Kunden führen — mit einem System,
      das sie selbst bedienen können.</p>
      <a class="knopf knopf-primaer" href="#kontakt">Erstgespräch vereinbaren</a>
      <p class="hero__hinweis">Wir arbeiten ausschließlich mit Unternehmen, nicht mit
      Verbrauchern.</p>
    </div>
    <div class="bild hero__bild">
      <img src="assets/img/hero.jpg" alt="Ruhiger Arbeitsplatz bei Tageslicht" width="1200" height="800">
    </div>
  </div>
</section>

<section class="abschnitt" id="fuer-wen">
  <div class="container">
    <span class="label">Für wen</span>
    <h2>Passt zu Ihnen, wenn Sie Ihre Leistung erklären müssen.</h2>
    <div class="raster-2">
      <div class="karte">
        <h3>Das trifft zu</h3>
        <ul class="liste">
          <li>Sie verkaufen eine erklärungsbedürftige Leistung an Unternehmen.</li>
          <li>Ihre Kunden kommen bislang über Empfehlungen oder Zufall.</li>
          <li>Sie wollen den Vertrieb selbst verstehen, nicht auslagern.</li>
          <li>Sie können wöchentlich Zeit für die Umsetzung einplanen.</li>
        </ul>
      </div>
      <div class="karte karte--leise">
        <h3>Das passt nicht</h3>
        <ul class="liste">
          <li>Sie suchen jemanden, der die Akquise vollständig übernimmt.</li>
          <li>Sie verkaufen an Privatpersonen.</li>
          <li>Sie erwarten Zusagen über Umsatz oder Kundenzahlen.</li>
          <li>Sie wollen Material konsumieren, ohne es anzuwenden.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="abschnitt abschnitt--akzent">
  <div class="container">
    <span class="label">Ausgangslage</span>
    <h2>Empfehlungen sind kein Vertrieb.</h2>
    <p>Wer Aufträge über Weiterempfehlung bekommt, hat kein System, sondern Glück. Das
    trägt, solange das Netzwerk trägt — und bricht weg, sobald ein großer Kunde geht oder
    der Markt sich dreht.</p>
    <p>Kaltakquise per Telefon und E-Mail wird zugleich schwerer: Postfächer sind voll,
    Entscheider gehen nicht mehr ans Telefon. Was bleibt, ist der Ort, an dem
    B2B-Entscheider ohnehin täglich sind — und an dem sich Sichtbarkeit und direkte
    Ansprache verbinden lassen.</p>
    <p>Genau dafür bauen wir mit Ihnen ein Vorgehen auf, das Sie danach ohne uns
    weiterführen können.</p>
  </div>
</section>
```

- [ ] **Schritt 2: Styles anhängen**

```css
.hero { padding: 80px 0 var(--abstand-abschnitt); }

.hero__inner {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 56px;
  align-items: center;
}

.hero__lead { font-size: 1.2rem; color: var(--text-leise); }
.hero__hinweis { font-size: 14px; color: var(--text-leise); margin-top: 20px; }
.hero__bild { aspect-ratio: 3 / 2; }

.raster-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-top: 40px;
}

.karte--leise { background: transparent; }

.liste { margin: 0; padding-left: 20px; color: var(--text-leise); }
.liste li { margin-bottom: 10px; }

@media (max-width: 900px) {
  .hero__inner, .raster-2 { grid-template-columns: 1fr; }
}
```

- [ ] **Schritt 3: Prüfskript und Sichtprüfung**

```bash
cd ~/Downloads/capitalcouncilmarketing && python3 tools/check.py
```

Erwartet: keine neuen Verstöße für `index.html`.

Dann `python3 -m http.server 8080`, im Browser öffnen und prüfen: Hero zweispaltig mit
blaustichigem Bild rechts, darunter zwei Karten nebeneinander, dann ein hellblauer
Abschnitt. Fenster auf 600 px verschmälern — alles muss einspaltig umbrechen.

- [ ] **Schritt 4: Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git add index.html styles.css
git commit -m "Hero, Zielgruppe und Ausgangslage aufbauen"
```

---

### Aufgabe 7: Abschnitt 4 — Die Methode · **GESPERRT bis Eingabe 5**

Dieser Abschnitt trägt die Glaubwürdigkeit der gesamten Seite, weil keine Erfolgsbelege
existieren. Er darf **nicht** mit erfundenen Phasen gefüllt werden.

**Voraussetzung:** Der Auftraggeber liefert Phasen, Sitzungsanzahl, Rhythmus und
Materialien. Liegt das nicht vor, wird diese Aufgabe übersprungen und der Auftraggeber
erneut danach gefragt.

**Dateien:**
- Ändern: `index.html`, `styles.css`

**Schnittstellen:**
- Verbraucht: `.abschnitt`, `.label`, `.karte` aus Aufgabe 3; `assets/img/arbeit.jpg`
  aus Aufgabe 5.
- Erzeugt: Anker `#methode`.

- [ ] **Schritt 1: Gelieferte Angaben in dieses Gerüst eintragen**

```html
<section class="abschnitt" id="methode">
  <div class="container">
    <span class="label">Vorgehen</span>
    <h2>So arbeiten wir mit Ihnen.</h2>
    <p>Vom ersten Termin bis zu dem Punkt, an dem Sie das System allein bedienen.</p>
    <div class="phasen">
      <!-- Pro gelieferter Phase ein Block. Nur ausfüllen, was der Auftraggeber
           angegeben hat — keine Phase hinzuerfinden. -->
      <article class="karte phase">
        <span class="phase__nr">01</span>
        <h3><!-- Name der Phase --></h3>
        <p><!-- Was in dieser Phase passiert --></p>
        <ul class="liste">
          <li><!-- Konkretes Ergebnis dieser Phase --></li>
        </ul>
      </article>
    </div>
    <div class="bild methode__bild">
      <img src="assets/img/arbeit.jpg" alt="Konzentriertes Arbeiten am Laptop" width="1600" height="900">
    </div>
  </div>
</section>
```

- [ ] **Schritt 2: Styles anhängen**

```css
.phasen {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 48px 0;
}

.phase__nr {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 2rem;
  color: var(--primaer);
  display: block;
  margin-bottom: 8px;
}

.methode__bild { aspect-ratio: 16 / 9; margin-top: 48px; }
```

- [ ] **Schritt 3: Prüfen, dass keine leeren Kommentare übrig sind**

```bash
cd ~/Downloads/capitalcouncilmarketing
grep -n '<!-- ' index.html
```

Erwartet: keine Ausgabe. Jeder verbliebene Platzhalter-Kommentar bedeutet, dass eine
Angabe fehlt — dann Abschnitt zurückbauen und Auftraggeber fragen.

- [ ] **Schritt 4: Prüfskript und Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
python3 tools/check.py
git add index.html styles.css
git commit -m "Methodenabschnitt mit den gelieferten Phasen aufbauen"
```

---

### Aufgabe 8: Abschnitte 5 und 6 — Leistungsumfang und Preis · **GESPERRT bis Eingabe 1**

**Voraussetzung:** Laufzeit, Zahlungsweise und Kündigungsfrist beider Pakete liegen vor.
Die AGB-Werte taugen nicht als Ersatz — sie gelten für Agenturleistungen.

**Dateien:**
- Ändern: `index.html`, `styles.css`

**Schnittstellen:**
- Verbraucht: `.abschnitt`, `.karte`, `.label`, `.knopf` aus Aufgabe 3.
- Erzeugt: Anker `#preis`.

- [ ] **Schritt 1: Abschnitt einsetzen**

Die mit `<!--` markierten Stellen mit den gelieferten Angaben füllen. Preise sind bereits
bestätigt und werden übernommen.

```html
<section class="abschnitt abschnitt--akzent" id="preis">
  <div class="container">
    <span class="label">Leistung und Preis</span>
    <h2>Zwei Wege, beide mit Begleitung.</h2>
    <div class="raster-2">
      <div class="karte paket">
        <h3>Gruppencoaching</h3>
        <p class="paket__preis">3.000 €</p>
        <p class="paket__hinweis">zzgl. Umsatzsteuer</p>
        <ul class="liste">
          <li>Begleitung in der Gruppe</li>
          <li>Videokurs mit allen Inhalten</li>
          <li>Laufender Support über WhatsApp</li>
        </ul>
        <dl class="kondition">
          <dt>Laufzeit</dt><dd><!-- Eingabe 1 --></dd>
          <dt>Zahlung</dt><dd><!-- Eingabe 1 --></dd>
          <dt>Kündigung</dt><dd><!-- Eingabe 1 --></dd>
        </dl>
        <a class="knopf" href="#kontakt">Erstgespräch vereinbaren</a>
      </div>
      <div class="karte paket">
        <h3>Einzelbetreuung</h3>
        <p class="paket__preis">8.000 €</p>
        <p class="paket__hinweis">zzgl. Umsatzsteuer</p>
        <ul class="liste">
          <li>Betreuung eins zu eins</li>
          <li>Alle Inhalte des Gruppenprogramms</li>
          <li>Laufender Support über WhatsApp</li>
        </ul>
        <dl class="kondition">
          <dt>Laufzeit</dt><dd><!-- Eingabe 1 --></dd>
          <dt>Zahlung</dt><dd><!-- Eingabe 1 --></dd>
          <dt>Kündigung</dt><dd><!-- Eingabe 1 --></dd>
        </dl>
        <a class="knopf knopf-primaer" href="#kontakt">Erstgespräch vereinbaren</a>
      </div>
    </div>
    <p class="preis__fuss">Beide Angebote richten sich ausschließlich an Unternehmer im
    Sinne des Rechts. Ein gesetzliches Widerrufsrecht besteht daher nicht. Zahlung per
    Überweisung, SEPA-Lastschrift, PayPal oder Kreditkarte. Es werden keine Zusagen über
    Umsätze, Kundenzahlen oder sonstige Ergebnisse gegeben.</p>
  </div>
</section>
```

- [ ] **Schritt 2: Styles anhängen**

```css
.paket__preis {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 2.6rem;
  margin: 0;
}

.paket__hinweis { color: var(--text-leise); font-size: 14px; margin-top: 0; }

.kondition {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 6px 16px;
  border-top: 1px solid var(--rand);
  padding-top: 16px;
  margin: 20px 0 24px;
  font-size: 15px;
}

.kondition dt { color: var(--text-leise); }
.kondition dd { margin: 0; }

.preis__fuss {
  margin-top: 32px;
  font-size: 14px;
  color: var(--text-leise);
  max-width: 80ch;
}
```

- [ ] **Schritt 3: Prüfen, dass keine Platzhalter übrig sind**

```bash
cd ~/Downloads/capitalcouncilmarketing
grep -n 'Eingabe 1' index.html
```

Erwartet: keine Ausgabe.

- [ ] **Schritt 4: Prüfskript und Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
python3 tools/check.py
git add index.html styles.css
git commit -m "Leistungsumfang und Preise beider Pakete darstellen"
```

---

### Aufgabe 9: Abschnitt 7 — Über uns · **GESPERRT bis Eingaben 2 und 3**

**Voraussetzung:** Claudios Werdegang liegt vor **und** ein echtes Porträtfoto. Ein
Stockfoto als Bild einer namentlich genannten Person wäre eine Falschdarstellung und ist
ausgeschlossen. Liegt nur der Werdegang vor, wird der Abschnitt ohne Bild gebaut.

**Dateien:**
- Ändern: `index.html`, `styles.css`
- Anlegen: `assets/img/claudio.jpg` (vom Auftraggeber geliefert)

**Schnittstellen:**
- Verbraucht: `.abschnitt`, `.label`, `.bild` aus Aufgabe 3.
- Erzeugt: Anker `#ueber-uns`.

- [ ] **Schritt 1: Foto ablegen und verkleinern**

```bash
cd ~/Downloads/capitalcouncilmarketing
sips -Z 1200 assets/img/claudio.jpg --out assets/img/claudio.jpg
ls -lh assets/img/claudio.jpg
```

Erwartet: Datei vorhanden, unter 300 KB.

- [ ] **Schritt 2: Abschnitt einsetzen**

```html
<section class="abschnitt" id="ueber-uns">
  <div class="container ueber__inner">
    <div class="bild ueber__bild">
      <img src="assets/img/claudio.jpg" alt="Claudio Fuersatz" width="800" height="1000">
    </div>
    <div>
      <span class="label">Wer dahintersteht</span>
      <h2>Claudio Fuersatz</h2>
      <!-- Werdegang aus Eingabe 2: Herkunft, bisherige Tätigkeit, Bezug zu LinkedIn.
           Zwei bis drei Absätze, ausschließlich belegbare Angaben. -->
      <p class="ueber__haltung">Keine Erfolgsversprechen, keine gemieteten Kulissen. Wir
      arbeiten mit Unternehmen, die ihren Vertrieb selbst verstehen wollen.</p>
    </div>
  </div>
</section>
```

- [ ] **Schritt 3: Styles anhängen**

```css
.ueber__inner {
  display: grid;
  grid-template-columns: 0.8fr 1.2fr;
  gap: 56px;
  align-items: start;
}

.ueber__bild { aspect-ratio: 4 / 5; }

.ueber__haltung {
  border-left: 3px solid var(--primaer);
  padding-left: 20px;
  color: var(--text-leise);
}

@media (max-width: 900px) {
  .ueber__inner { grid-template-columns: 1fr; }
}
```

- [ ] **Schritt 4: Auf Platzhalter prüfen, Prüfskript, Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
grep -n '<!-- Werdegang' index.html
python3 tools/check.py
git add index.html styles.css assets/img/claudio.jpg
git commit -m "Über-uns-Abschnitt mit Werdegang und Porträt aufbauen"
```

Der `grep` muss ohne Ausgabe bleiben.

---

### Aufgabe 10: Abschnitte 8 und 9 — FAQ und Kontakt · **GESPERRT bis Eingabe 4**

**Voraussetzung:** Telefonnummer liegt vor. Ohne sie wird der Abschnitt mit E-Mail und
Calendly gebaut und die Nummer später ergänzt — für die Bankprüfung ist sie ein Pluspunkt,
aber kein Ausschlusskriterium.

**Dateien:**
- Ändern: `index.html`, `styles.css`

**Schnittstellen:**
- Verbraucht: `.abschnitt`, `.karte`, `.knopf-primaer` aus Aufgabe 3;
  `assets/img/gespraech.jpg` aus Aufgabe 5.
- Erzeugt: Anker `#kontakt` — Ziel aller Schaltflächen aus den Aufgaben 4, 6 und 8.

- [ ] **Schritt 1: FAQ und Kontakt einsetzen**

Die FAQ beantwortet bewusst auch die unangenehmen Fragen. Das ist für die Bankprüfung
wertvoller als Werbetext.

```html
<section class="abschnitt" id="faq">
  <div class="container">
    <span class="label">Häufige Fragen</span>
    <h2>Was Sie vorher wissen sollten.</h2>
    <div class="faq">
      <details class="faq__eintrag">
        <summary>Gibt es eine Garantie auf Ergebnisse?</summary>
        <p>Nein. Wir sichern Begleitung, Materialien und Erreichbarkeit zu — keine
        Umsätze, Kundenzahlen oder Reichweiten. Diese hängen von Ihrem Markt, Ihrem
        Angebot und Ihrer Umsetzung ab. Wer Ihnen Umsatz garantiert, verkauft Ihnen etwas
        anderes als Begleitung.</p>
      </details>
      <details class="faq__eintrag">
        <summary>Wie viel Zeit muss ich einplanen?</summary>
        <p>Die Umsetzung erfolgt durch Sie. Ohne wöchentliche Arbeitszeit an Ihrem
        eigenen Vertrieb bringt das Programm nichts.</p>
      </details>
      <details class="faq__eintrag">
        <summary>Übernehmen Sie die Akquise für mich?</summary>
        <p>Nein. Wir bilden aus und begleiten. Wenn Sie eine Dienstleistung suchen, die
        Ihnen Termine liefert, sind wir der falsche Anbieter.</p>
      </details>
      <details class="faq__eintrag">
        <summary>Kann ich kündigen?</summary>
        <!-- Antwort aus Eingabe 1: Kündigungsfrist beider Pakete, wortgleich zu den
             Angaben im Preisabschnitt und in den AGB. -->
      </details>
      <details class="faq__eintrag">
        <summary>Arbeiten Sie auch mit Privatpersonen?</summary>
        <p>Nein. Unser Angebot richtet sich ausschließlich an Unternehmer im Sinne des
        Rechts. Ein gesetzliches Widerrufsrecht besteht daher nicht.</p>
      </details>
    </div>
  </div>
</section>

<section class="abschnitt abschnitt--akzent" id="kontakt">
  <div class="container kontakt__inner">
    <div>
      <span class="label">Kontakt</span>
      <h2>Erstgespräch vereinbaren.</h2>
      <p>Dreißig Minuten, in denen wir prüfen, ob Ihr Angebot und Ihr Markt zu unserem
      Vorgehen passen. Passt es nicht, sagen wir das.</p>
      <a class="knopf knopf-primaer" href="https://calendly.com/d/dv5p-69t-5jx"
         target="_blank" rel="noopener noreferrer">Termin auswählen</a>
      <dl class="kontakt__daten">
        <dt>E-Mail</dt>
        <dd><a href="mailto:office@capitalcouncilmarketing.com">office@capitalcouncilmarketing.com</a></dd>
        <dt>Telefon</dt>
        <dd><!-- Eingabe 4 --></dd>
        <dt>Anschrift</dt>
        <dd>28 Capital Council LLC<br>Sheridan, WY 82801<br>Vereinigte Staaten</dd>
      </dl>
    </div>
    <div class="bild kontakt__bild">
      <img src="assets/img/gespraech.jpg" alt="Zwei Personen im Gespräch" width="1200" height="900">
    </div>
  </div>
</section>
```

- [ ] **Schritt 2: Styles anhängen**

```css
.faq { margin-top: 40px; border-top: 1px solid var(--rand); }

.faq__eintrag { border-bottom: 1px solid var(--rand); padding: 20px 0; }

.faq__eintrag summary {
  cursor: pointer;
  font-weight: 500;
  font-size: 1.05rem;
  list-style: none;
}

.faq__eintrag summary::-webkit-details-marker { display: none; }
.faq__eintrag summary::after { content: " +"; color: var(--primaer); }
.faq__eintrag[open] summary::after { content: " −"; }
.faq__eintrag p { margin: 14px 0 0; color: var(--text-leise); }

.kontakt__inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 56px;
  align-items: center;
}

.kontakt__daten {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 8px 20px;
  margin-top: 32px;
  font-size: 15px;
}

.kontakt__daten dt { color: var(--text-leise); }
.kontakt__daten dd { margin: 0; }
.kontakt__bild { aspect-ratio: 4 / 3; }

@media (max-width: 900px) {
  .kontakt__inner { grid-template-columns: 1fr; }
}
```

- [ ] **Schritt 3: Calendly-Verhalten prüfen**

Der Calendly-Link ist ein gewöhnlicher `<a>` — er lädt nichts, bevor der Besucher klickt.
Das erfüllt die Vorgabe „keine Übertragung ohne Zutun des Besuchers". Auf keinen Fall ein
Calendly-Einbettungsskript verwenden.

```bash
cd ~/Downloads/capitalcouncilmarketing
grep -c 'calendly.com/assets\|<script' index.html
```

Erwartet: `0`.

- [ ] **Schritt 4: Prüfskript und Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
grep -n 'Eingabe 4\|<!-- Antwort' index.html
python3 tools/check.py
git add index.html styles.css
git commit -m "FAQ und Kontaktabschnitt aufbauen"
```

Der `grep` muss ohne Ausgabe bleiben.

---

### Aufgabe 11: Rechtstexte umbauen

Die vier Rechtsseiten tragen noch das alte Design und die alte Marke. Die AGB beschreiben
zudem ein anderes Geschäft.

**Dateien:**
- Ändern: `impressum.html`, `datenschutz.html`, `agb.html`, `haftungsausschluss.html`

**Schnittstellen:**
- Verbraucht: `styles.css` und die Kopf-/Fuß-Bausteine aus Aufgabe 4.

- [ ] **Schritt 1: Alle vier Seiten auf das neue Gerüst umstellen**

In jeder der vier Dateien: den kompletten `<head>` durch den Kopf aus `index.html`
ersetzen (Titel und Beschreibung jeweils anpassen), die Tailwind- und
Analytics-Skriptblöcke entfernen, `<link rel="stylesheet" href="styles.css">` einsetzen
und Kopf- sowie Fußbereich aus `index.html` übernehmen. Der eigentliche Rechtstext bleibt
erhalten und wird in `<main><div class="container rechtstext">…</div></main>` gefasst.

```css
.rechtstext { padding: 64px 0; max-width: 80ch; }
.rechtstext h1 { font-size: 2.4rem; }
.rechtstext h2 { font-size: 1.5rem; margin-top: 2em; }
.rechtstext p, .rechtstext li { color: var(--text-leise); }
```

- [ ] **Schritt 2: Marke in allen vier Dateien ersetzen**

```bash
cd ~/Downloads/capitalcouncilmarketing
sed -i '' 's/Skala/Growth Lab Blueprint/g' impressum.html datenschutz.html agb.html haftungsausschluss.html
grep -c 'Skala' *.html || echo "keine Treffer — korrekt"
```

- [ ] **Schritt 3: Datenschutzerklärung anpassen**

Drei Änderungen, jeweils als eigener Abschnitt:

1. **Analytics streichen.** Der gesamte Abschnitt zu Google Analytics und die Erwähnung
   von Cookies zur Reichweitenmessung entfallen — es läuft kein Tracking mehr.
2. **Calendly ergänzen:** Hinweis, dass beim Klick auf die Terminvereinbarung eine
   Verbindung zu Calendly LLC (USA) aufgebaut wird, dass dabei IP-Adresse und
   Browserdaten übertragen werden und dass dies erst nach aktivem Klick geschieht.
3. **Schriften und Hosting ergänzen:** Hinweis, dass Schriftarten lokal ausgeliefert
   werden und keine Verbindung zu Google aufgebaut wird; Hosting über Vercel Inc. mit
   Server-Logdateien.

- [ ] **Schritt 4: AGB inhaltlich umschreiben**

Der Leistungsgegenstand muss von Agenturleistungen auf Coaching umgestellt werden.

| Paragraf | Heute | Neu |
|---|---|---|
| § 1 | Beschränkung auf Unternehmer | **unverändert übernehmen** |
| § 2 | Leistungen: SEO, Ads, Social Media | Coaching: Gruppenprogramm und Einzelbetreuung, Umfang wie im Preisabschnitt |
| § 3 | Preise, Werbebudget-Abgrenzung | Preise 3.000 € / 8.000 € netto, Zahlungsweise aus Eingabe 1; Werbebudget-Absatz entfällt |
| § 4 | Laufzeiten für Retainer | Laufzeit und Kündigungsfrist beider Pakete aus Eingabe 1 |
| § 5 | Zugänge zu Werbekonten | Mitwirkung: Teilnahme an Terminen, eigenständige Umsetzung |
| § 6 | keine Ergebnisgarantien | **unverändert übernehmen**, Formulierung ist gut |

- [ ] **Schritt 5: Prüfskript**

```bash
cd ~/Downloads/capitalcouncilmarketing && python3 tools/check.py
```

Erwartet: **BESTANDEN**. Dies ist die erste Aufgabe, nach der das Skript vollständig
durchläuft.

- [ ] **Schritt 6: Committen**

```bash
cd ~/Downloads/capitalcouncilmarketing
git add impressum.html datenschutz.html agb.html haftungsausschluss.html styles.css
git commit -m "Rechtstexte auf neue Marke umstellen und AGB auf Coaching umschreiben"
```

---

### Aufgabe 12: Dokumentation und Abschlussprüfung

**Dateien:**
- Ersetzen: `DESIGN.md`
- Ersetzen: `README.md`

- [ ] **Schritt 1: DESIGN.md neu schreiben**

Der Inhalt beschreibt „Kinetic Noir" und ist vollständig überholt. Ersetzen durch: die
Farbtabelle aus den globalen Vorgaben, die beiden Schriften mit Begründung, die
Layoutwerte (1200 px, 140 px, Radius 12 px), die Bildregeln (einheitliche Blaufärbung
über `.bild`, Ausschlusskriterien für Motive) sowie die Bausteine aus `styles.css`
(`.knopf`, `.karte`, `.label`, `.abschnitt`).

- [ ] **Schritt 2: README.md füllen**

```markdown
# Growth Lab Blueprint

Website der 28 Capital Council LLC für das LinkedIn-Coaching-Angebot.
Statisches HTML ohne Build-Schritt.

## Lokal ansehen

    python3 -m http.server 8080

Dann http://localhost:8080 öffnen.

## Prüfen

    python3 tools/check.py

Prüft: keine Fremdanfragen, keine erfundenen Erfolgsbelege, keine toten Links,
keine Platzhalter, Marke und Kopfangaben auf allen Seiten.

## Grundsätze

- Beim Seitenaufruf geht keine Anfrage an einen fremden Server. Schriften und
  Bilder liegen im Repo. Kein Analytics, kein CDN.
- Es werden keine Zahlen, Fallbeispiele oder Kundenstimmen dargestellt, die
  nicht belegbar sind.
- Gestaltung: siehe DESIGN.md
```

- [ ] **Schritt 3: Abschließende Sichtprüfung im Browser**

```bash
cd ~/Downloads/capitalcouncilmarketing && python3 -m http.server 8080
```

Durchgehen:
1. Alle neun Abschnitte in der Reihenfolge der Spec vorhanden
2. Alle vier Rechtslinks in der Fußzeile funktionieren und zeigen das neue Design
3. Fenster auf 600 px verschmälern — nichts läuft über den Rand
4. **Netzwerk-Tab der Entwicklerwerkzeuge öffnen, Seite neu laden:** Es darf **keine**
   Anfrage an eine fremde Domain erscheinen. Alle Einträge zeigen auf `localhost`.
5. Auf „Termin auswählen" klicken — erst jetzt öffnet sich Calendly in einem neuen Tab

- [ ] **Schritt 4: Letzte Prüfung und Commit**

```bash
cd ~/Downloads/capitalcouncilmarketing
python3 tools/check.py
git add DESIGN.md README.md
git commit -m "Designsystem und Projektdokumentation aktualisieren"
git log --oneline
git status --short
```

Erwartet: `BESTANDEN`, sauberer Arbeitsbaum, und **kein Push** — der Stand bleibt lokal,
bis der Auftraggeber freigibt.
