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

| Token | Wert | Rolle |
|---|---|---|
| `--bg` | `#F7F9FC` | Seitenhintergrund |
| `--flaeche` | `#FFFFFF` | Flächen: Karten, Knöpfe, Kopfzeile |
| `--rand` | `#E3E8EF` | Ränder von Karten, Knöpfen, Kopf- und Fußzeile |
| `--text` | `#0A2540` | Fließtext, Überschriften, Marke |
| `--text-leise` | `#5B6B7F` | Nebentext: Hero-Lead, Navigation, Fußzeile, Listen |
| `--primaer` | `#1B5FCC` | Primärfarbe: Labels, Links, Primärknopf, Bild-Überlagerung |
| `--akzent` | `#E8F0FE` | Hell-Akzent: `.abschnitt--akzent`, Verlauf-Rückfallebene für Bilder |

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

- `.container` — zentrierter Layoutrahmen, `max-width: var(--breite)`, seitliches Padding 24px
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
`.fuss__marke`, `.fuss__links`) sowie die Hero-Klassen (`.hero`, `.hero__inner`,
`.hero__lead`, `.hero__hinweis`, `.hero__bild`) und `.rechtstext` für die
Rechtsseiten runden das System ab, folgen aber denselben Tokens und Bausteinen
oben.
