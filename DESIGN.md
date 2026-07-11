---
name: Kinetic Noir
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

This design system embodies a high-octane, tech-forward marketing aesthetic. It leverages a "Dark Tech" style that prioritizes deep immersion, high contrast, and cinematic energy. The mood is authoritative yet innovative, designed to evoke feelings of precision, speed, and premium quality.

The visual narrative is built on the tension between an expansive, near-black void and surgical strikes of vibrant red-orange light. It utilizes spacious layouts, generous negative space, and "glow-morphism" to create depth without relying on traditional skeuomorphism. The target audience expects a cutting-edge partner that balances raw power with sophisticated execution.

## Colors

The palette is strictly controlled to maintain a high-end, focused atmosphere. The background is a deep, singular black to maximize the luminance of the accent colors. 

- **Primary:** A high-vibrancy red-orange used for calls to action, progress indicators, and critical highlights.
- **Accents:** Gradients between the primary shades are used to create "light leaks" and glows, simulating a high-tech hardware interface.
- **Neutrals:** Dark grey surfaces create structural hierarchy, while light grey text ensures readability without the harshness of pure white on black.

## Typography

Typography is a primary structural element. **Space Grotesk** provides a technical, geometric edge for headlines, utilizing tight letter-spacing and massive scales for a "display" feel. **Inter** handles all functional and body copy, chosen for its extreme legibility and neutral, systematic character.

Large display type should often use a slight "inner glow" or white-to-light-grey gradient to feel integrated into the dark environment. Labels and overlines should always be uppercase with increased tracking to denote technical metadata.

## Layout & Spacing

The layout follows a 12-column fluid grid system with significant vertical "breathing room" between sections (120px+). Content should feel uncrowded, mimicking the premium feel of a high-end editorial or luxury tech brand.

- **Desktop:** 12 columns, 24px gutters, max-width of 1280px.
- **Tablet:** 8 columns, 24px gutters, fluid width.
- **Mobile:** 4 columns, 20px gutters, fluid width.

Elements within cards use a tight 8px-based spacing system to maintain a "dense information" feel inside an otherwise "spacious" layout.

## Elevation & Depth

This system avoids traditional drop shadows in favor of **Tonal Layering** and **Luminescence**. 

1.  **Base Layer:** The `#0a0a0a` background.
2.  **Surface Layer:** Dark grey cards (`#1a1a1a`) with a subtle `1px` border in `#2a2a2a`.
3.  **Accent Depth:** High-priority cards or buttons feature a "Red Glow"—a soft, diffused outer shadow using the primary color at 15-20% opacity.
4.  **Glassmorphism:** Navigation bars and floating controls use a 20px backdrop blur with a 10% white overlay to feel like precision-machined glass.

## Shapes

The shape language is "Sophisticated Geometric." We use a consistent `0.5rem` (8px) base radius for standard inputs and small UI elements, but significantly larger radii for structural containers.

- **Standard Cards:** `1.5rem` (24px) to create a friendly but professional "modern tech" silhouette.
- **Buttons:** Fully pill-shaped (`999px`) to distinguish interactive elements from informational cards.
- **Icons:** Lean, 2px stroke-width icons with slightly rounded caps to match the typography.

## Components

### Buttons
- **Primary:** Pill-shaped, Primary Gradient background, white text. Features a 10px blurred red glow on hover.
- **Secondary:** Pill-shaped, ghost style with a 1px border (`#2a2a2a`), white text. Background shifts to a subtle dark grey on hover.

### Cards
- **Feature Cards:** `#1a1a1a` background, 24px padding, `rounded-2xl`. Borders are `#2a2a2a`. 
- **Stats Cards:** Minimalist, featuring large Space Grotesk numbers and the primary color for the metric value.

### Input Fields
- Dark backgrounds (`#050505`), 1px subtle borders. On focus, the border turns to the primary red and a soft red outer glow is applied.

### Chips & Tags
- Small, uppercase text within a `#2a2a2a` container. For "Active" or "Live" status, a small 8px pulsing red dot is included to the left of the text.