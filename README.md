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
