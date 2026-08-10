# Designsystem — Growth Lab Blueprint

Dieses Dokument beschreibt das Designsystem, wie es tatsächlich in `styles.css`
gebaut ist. Es beschreibt keine Wunschliste — jede hier genannte Regel hat eine
Entsprechung im Stylesheet.

Anlass des Systems: Die Website wird einer Bank zur Prüfung vorgelegt, damit
das Geschäftskonto der 28 Capital Council LLC nicht wiederholt gesperrt wird.
Entsprechend ruhig, seriös und zurückhaltend ist die Gestaltung angelegt —
kein „high-octane"-Look, keine Coaching-Ästhetik.

## Farben

Sieben Tokens, definiert in `:root` in `styles.css`:

| Token | Wert | Rolle (Selektoren in `styles.css`) |
|---|---|---|
| `--bg` | `#F7F9FC` | Seitenhintergrund (`body`, Zeile 21) |
| `--flaeche` | `#FFFFFF` | Flächen von Knöpfen und Karten (`.knopf`, Zeile 69; `.karte`, Zeile 87) |
| `--rand` | `#E3E8EF` | Ränder von Knöpfen, Karten, Kopf- und Fußzeile (`.knopf`, Zeile 68; `.karte`, Zeile 88; `.kopf`, Zeile 135; `.fuss`, Zeile 160) |
| `--text` | `#0A2540` | Textfarbe von `body` (Zeile 22) — davon erben `h1`–`h3` ihre Farbe, da sie keine eigene setzen. Zusätzlich explizit bei `.knopf` (Zeile 70), `.marke` (Zeile 150), `.nav a:hover` (Zeile 156), `.fuss__marke` (Zeile 168) |
| `--text-leise` | `#5B6B7F` | Nebentext: `.nav a` (Zeile 155), `.fuss` (Zeile 162), `.hero__lead` (Zeile 187), `.hero__hinweis` (Zeile 188), `.liste` (Zeile 200), `.rechtstext p`/`.rechtstext li` (Zeile 210) |
| `--primaer` | `#1B5FCC` | `a` (Zeile 42), `.label` (Zeile 59), Randfarbe von `.knopf:hover` (Zeile 76), Hintergrund/Rand von `.knopf-primaer` (Zeile 79–80), Verlauf-Endfarbe und Überlagerung von `.bild` (Zeile 102, 117) |
| `--akzent` | `#E8F0FE` | Hintergrund von `.abschnitt--akzent` (Zeile 52), Verlauf-Startfarbe von `.bild` (Zeile 102) |

**Kopfzeile — Sonderfall, kein Token:** `.kopf` (Zeile 129–136) sitzt als
klebende Leiste über dem Inhalt (`position: sticky; top: 0`) mit
`backdrop-filter: blur(12px)`. Ihr Hintergrund läuft **nicht** über ein
Farb-Token, sondern ist hart codiert: `background: rgba(247, 249, 252, 0.85)`
(Zeile 134) — das ist `--bg` (`#F7F9FC`) mit 85 % Deckkraft, aber direkt als
Zahlenwert geschrieben statt als `var(--bg)`. Wer die Kopfzeile farblich
anpassen will, findet die wirksame Regel also nicht über `--bg` oder
`--flaeche`, sondern muss Zeile 134 in `styles.css` direkt bearbeiten.

Wichtig: LinkedIns exaktes Markenblau `#0A66C2` wird bewusst **nicht** verwendet.
`--primaer` (`#1B5FCC`) liegt nah genug an dieser Farbfamilie, um die gewünschte
Assoziation mit einer professionellen, plattformnahen Beratung auszulösen —
unterscheidet sich aber deutlich genug, dass keine offizielle Partnerschaft mit
LinkedIn suggeriert wird.

## Schriften

- **Source Serif 4** für Überschriften (`h1`, `h2`, `h3`, `.marke`, `.fuss__marke`).
- **Inter** für Fließtext (`body`).

Beide sind variable Schriften und lokal eingebunden über `assets/fonts/fonts.css`
(per `@import` in `styles.css`), mit Gewichtsspannen statt einzelner Schnitte:
Inter deckt `font-weight: 100 900` ab, Source Serif 4 `font-weight: 200 900`.
Keine externen Font-Anfragen — passend zur Vorgabe, dass beim Seitenaufruf
keine Fremdanfragen entstehen.

Begründung für die Serifenschrift bei Überschriften: Serifen signalisieren
Beständigkeit — aus demselben Grund setzen Beratungen, Kanzleien und
Wirtschaftsmedien auf sie. Zugleich grenzt das von der Coaching-Branche ab,
die fast durchweg geometrische Sans-Schriften verwendet.

## Layoutwerte

Als CSS-Variablen in `:root`:

- `--breite: 1200px` — maximale Breite von `.container`
- `--abstand-abschnitt: 140px` — vertikales Padding von `.abschnitt` (auf
  Viewports bis 720px auf `80px` reduziert)
- `--radius: 12px` — Eckenradius von `.karte` und `.bild`
- `--radius-pill: 999px` — Eckenradius von `.knopf` (Pill-Form)

## Bildregeln

`.bild` sorgt für eine einheitliche Blaufärbung, damit Stockmaterial
unterschiedlicher Herkunft wie eine zusammenhängende Bildserie wirkt, statt wie
zusammengewürfelte Fotos verschiedener Quellen. Umgesetzt über ein `::after`-
Overlay in `--primaer` mit `opacity: 0.16` und `mix-blend-mode: color`, dazu
ein `filter: saturate(0.7) contrast(1.02)` auf dem `img`-Element selbst.

Rückfallebene: Solange ein Foto fehlt, zeigt `.bild` einen Verlauf in den
Markenfarben (`linear-gradient(135deg, var(--akzent) 0%, #C9DBF7 55%,
var(--primaer) 100%)`) statt eines kaputten Bildsymbols.

Ausschlusskriterien für Bildmotive:
- kein Händeschütteln
- keine Konferenzräume mit Zeigefinger auf Diagramme
- keine Erfolgsposen
- keine fremden Markenlogos
- keine erkennbaren LinkedIn-Oberflächen

## Bausteine

Aus `styles.css`:

- `.container` — zentrierter Layoutrahmen, `max-width: var(--breite)`, `padding: 0 24px`
- `.label` — Versal-Label: 12px, fett, `letter-spacing: 0.14em`, `text-transform: uppercase`, in `--primaer`
- `.knopf` — Grundknopf: Pill-Form, weiße Fläche, Rand in `--rand`, färbt den Rand bei Hover in `--primaer`
- `.knopf-primaer` — gefüllte Variante von `.knopf`: Hintergrund und Rand in `--primaer`, weiße Schrift
- `.karte` — weiße Fläche mit Rand und `--radius`, 32px Innenabstand (24px unter 720px)
- `.abschnitt` — Abschnitts-Wrapper mit vertikalem Padding `var(--abstand-abschnitt)`
- `.abschnitt--akzent` — Abschnitt mit Hintergrund `--akzent`
- `.bild` — einheitliche Bildbehandlung, siehe oben
- `.raster-2` — zweispaltiges Grid (`1fr 1fr`, 24px Abstand), fällt unter 900px auf eine Spalte
- `.karte--leise` — Modifikator zu `.karte`: transparenter Hintergrund statt Weiß
- `.liste` — Aufzählung ohne Standard-Margin, Text in `--text-leise`, 10px Abstand zwischen Einträgen

Kopf- und Fußzeile (`.kopf`, `.kopf__inner`, `.marke`, `.nav`, `.fuss`,
`.fuss__marke`, `.fuss__traeger`, `.fuss__links`) sowie die Hero-Klassen
(`.hero`, `.hero__inner`, `.hero__lead`, `.hero__hinweis`, `.hero__bild`) und
`.rechtstext` für die Rechtsseiten runden das System ab, folgen aber denselben
Tokens und Bausteinen oben — mit der einen Ausnahme, dass `.kopf` seinen
Hintergrund hart codiert statt über ein Token setzt (siehe Abschnitt „Farben"
oben). `.fuss__traeger` (Zeile 172) setzt lediglich `font-size: 14px` und
`margin: 0` für die Rechtsträgerzeile unter der Marke im Footer.

## Methode-Abschnitt: Phasen und Begleitung

- `.phasen` — Grid für die fünf Vorgehens-Karten, `repeat(auto-fit,
  minmax(280px, 1fr))`, 24px Abstand, 48px vertikaler Außenabstand
- `.phase__nr` — die Phasennummer (01–05) in Source Serif 4, 2rem, `--primaer`,
  8px Abstand zur Überschrift darunter
- `.begleitung` — Wrapper für die Liste „Womit wir Sie begleiten“, oberer Rand
  in `--rand`, 32px Innenabstand oben, 48px Außenabstand oben

## Preis-Abschnitt

- `.paket__preis` — der Preis in großer Source Serif 4, 2.6rem, ohne
  Standard-Margin
- `.paket__hinweis` — Zusatzhinweis unter dem Preis (z. B. „zzgl.
  Umsatzsteuer“), `--text-leise`, 14px
- `.kondition` — Definitionsliste für Laufzeit/Zahlung/Kündigung: zweispaltiges
  Grid (`auto 1fr`), oberer Rand in `--rand`, 16px Innenabstand oben
- `.preis__fuss` — Fußnotentext unter den Paketen, 14px, `--text-leise`,
  `max-width: 80ch`, 32px Außenabstand oben

## Über-uns-Abschnitt

- `.ueber__inner` — begrenzt den Fließtext auf `max-width: 70ch`
- `.ueber__haltung` — hervorgehobener Absatz mit linkem Rahmen in `--primaer`,
  20px Innenabstand links, `--text-leise`, 32px Außenabstand oben

## FAQ

- `.faq` — Wrapper der FAQ-Liste, oberer Rand in `--rand`, 40px Außenabstand
  oben
- `.faq__eintrag` — einzelnes `<details>`-Element: unterer Rand in `--rand`,
  20px vertikaler Innenabstand. Das native Dreieck von `<summary>` wird über
  `list-style: none` bzw. `::-webkit-details-marker { display: none }`
  entfernt und durch ein eigenes `+`/`−`-Zeichen (`::after`) ersetzt, das beim
  geöffneten Zustand (`[open]`) wechselt

## Kontakt-Abschnitt

- `.kontakt__inner` — zweispaltiges Grid (`1fr 1fr`), 56px Abstand, fällt
  unter 900px auf eine Spalte
- `.kontakt__daten` — Definitionsliste für E-Mail/Anschrift: zweispaltiges
  Grid (`auto 1fr`), 32px Außenabstand oben, 15px Schriftgröße
