---
name: Skala — Kinetic Noir
colors:
  surface: '#1f0f0d'
  surface-dim: '#1f0f0d'
  surface-bright: '#493431'
  surface-container-lowest: '#190a08'
  surface-container-low: '#291715'
  surface-container: '#2d1b18'
  surface-container-high: '#392522'
  surface-container-highest: '#44302d'
  on-surface: '#fcdbd6'
  on-surface-variant: '#e7bdb7'
  inverse-surface: '#fcdbd6'
  inverse-on-surface: '#402b29'
  outline: '#ad8883'
  outline-variant: '#5d3f3b'
  surface-tint: '#ffb4aa'
  primary: '#ffb4aa'
  on-primary: '#690003'
  primary-container: '#ff5545'
  on-primary-container: '#5c0002'
  inverse-primary: '#c0000a'
  secondary: '#ffb4aa'
  on-secondary: '#680203'
  secondary-container: '#891d16'
  on-secondary-container: '#ff9a8c'
  tertiary: '#68d3fc'
  on-tertiary: '#003545'
  tertiary-container: '#1d9cc3'
  on-tertiary-container: '#002e3c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#930005'
  secondary-fixed: '#ffdad5'
  secondary-fixed-dim: '#ffb4aa'
  on-secondary-fixed: '#410001'
  on-secondary-fixed-variant: '#891d16'
  tertiary-fixed: '#bbe9ff'
  tertiary-fixed-dim: '#68d3fc'
  on-tertiary-fixed: '#001f29'
  on-tertiary-fixed-variant: '#004d63'
  background: '#1f0f0d'
  on-background: '#fcdbd6'
  surface-variant: '#44302d'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  display-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 24px
  margin-mobile: 20px
  section-gap: 120px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

**Skala** ist ein Coaching für Gründer von Social Media Agenturen. Das Design folgt einem
ruhigen, zentrierten "Dark Studio"-Stil: fast schwarzer Hintergrund, ein großer, weich
verlaufender Farbnebel (Aurora) hinter der Hero-Sektion und viel Leerraum.

Die Farbwelt der Vorgänger-Website bleibt unverändert: Primär `#ff3b30` mit
`#ff5545` / `#ff8c00` in den Verläufen, Hintergrund `#0a0a0a`, Text `#fcdbd6`.
Neu ist die Anwendung: statt vieler roter Akzentflächen wird die Farbe fast
ausschließlich im Aurora-Glow, in Icons, in Mikrolabels und im Primär-Button eingesetzt.

## Typografie

**Space Grotesk** für alle Displays und Headlines, sehr eng gesetzt (-0.045em),
Gewicht 500, Zeilenhöhe 0.95 — der Wortmarken-Look aus dem Hero.
**Inter** für Fließtext, meist in `text-white/60` für ruhige Lesbarkeit.
Mikrolabels (`.mono-label`) sind 11px, uppercase, 0.18em Laufweite.

## Layout

Zentrierte Hero-Sektionen mit voller Viewport-Höhe, danach linksbündige
Sektions-Header (Mikrolabel + große Headline) und Karten-Grids.
Container max 1200px, Sektionsabstand 140px.

## Komponenten

- **Pill-Nav:** zentriert schwebend, 20px Backdrop-Blur, aktiver Link mit `bg-white/10`.
- **Aurora:** `.aurora` erzeugt zwei animierte, weich geblurrte Farbkreise; mit
  `.vignette` darüber blendet der Rand sauber ins Schwarz aus.
- **Ghost-Word:** riesiger Markenname bei 3,5% Deckkraft als Sektionshintergrund.
- **Buttons:** `.btn-ghost` (Glas, 1px Weißrand) und `.btn-primary` (Rot mit Glow bei Hover), beide vollständig pill-förmig.
- **Karten:** `#141414`, 1px Weißrand bei 6%, Radius 1.5rem, Rand färbt sich bei Hover rot.
