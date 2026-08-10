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

## Fotos nachtragen

Die `.bild`-Container in `index.html` (Hero, Methode, Kontakt) zeigen bis auf Weiteres
nur den Verlaufs-Hintergrund aus `styles.css` — die Fotos liefert der Auftraggeber
später nach. Zum Einsetzen:

1. Datei nach `assets/img/` legen (z. B. `assets/img/hero.jpg`).
2. Im jeweiligen `.bild`-Container ein `<img>`-Element ergänzen, zum Beispiel:

       <div class="bild hero__bild">
         <img src="assets/img/hero.jpg" alt="Ruhiger Arbeitsplatz bei Tageslicht" width="1200" height="800">
       </div>

   Die anderen beiden Container heißen `methode__bild` (`arbeit.jpg`) und
   `kontakt__bild` (`gespraech.jpg`).

## Grundsätze

- Beim Seitenaufruf geht keine Anfrage an einen fremden Server. Schriften und
  Bilder liegen im Repo. Kein Analytics, kein CDN.
- Es werden keine Zahlen, Fallbeispiele oder Kundenstimmen dargestellt, die
  nicht belegbar sind.
- Gestaltung: siehe DESIGN.md
