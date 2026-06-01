---
name: Standard Administrative
colors:
  surface: '#FFFFFF'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#43474e'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#455f88'
  primary: '#002045'
  on-primary: '#ffffff'
  primary-container: '#1a365d'
  on-primary-container: '#86a0cd'
  inverse-primary: '#adc7f7'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfdf'
  on-secondary-container: '#626262'
  tertiary: '#4a0000'
  on-tertiary: '#ffffff'
  tertiary-container: '#730000'
  on-tertiary-container: '#ff7360'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f7'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffdad4'
  tertiary-fixed-dim: '#ffb4a8'
  on-tertiary-fixed: '#410000'
  on-tertiary-fixed-variant: '#920703'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
  border: '#D9D9D9'
  text-primary: '#000000'
  table-stripe: '#FAFAFA'
  action-slate: '#3A4A5A'
typography:
  headline-lg:
    fontFamily: Roboto
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-md:
    fontFamily: Roboto
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0.05em
  body-md:
    fontFamily: Roboto
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  label-sm:
    fontFamily: Roboto
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
spacing:
  margin-page: 24px
  gutter: 16px
  padding-panel: 20px
  row-height-md: 40px
  header-height: 64px
---

## Brand & Style

The design system is built upon a **Minimalist / Brutalist** hybrid aesthetic, prioritizing functional density over decorative flair. It is designed for high-stakes enterprise environments where data clarity and speed of information retrieval are paramount. 

The personality is authoritative, transparent, and strictly utilitarian. By removing modern embellishments like gradients, rounded corners, and shadows, the system ensures that the UI never competes with the data it presents. Every pixel is intentional, every border serves as a structural guide, and the aesthetic reflects a "serious tool" for serious work.

## Colors

The color strategy uses a high-contrast neutral palette to ensure maximum legibility for long-duration analysis.

- **Backgrounds:** The primary application canvas uses a light gray background to reduce eye strain, while active modules and panels use pure white to pop against the canvas.
- **Accents:** Navy Blue (#1A365D) is reserved strictly for primary system-level actions, providing a sense of stability and authority.
- **Feedback:** Destructive actions and critical alerts use a muted crimson to signal importance without being visually jarring.
- **System Borders:** Ash Gray is used for all structural delineations. Use 1px solid lines for all container boundaries.

## Typography

Typography is the primary driver of hierarchy in this design system. 

- **Primary Interface:** Roboto is used for all UI labels, headers, and standard text. It provides a clean, neutral tone that stays legible at small sizes.
- **Data Display:** For all IDs, timestamps, and numerical metrics, use a monospaced font. This ensures character-width consistency, allowing columns of numbers to align vertically for easier scanning.
- **Emphasis:** Section headers should use semi-bold weight with uppercase styling and slight letter spacing to create a distinctive visual anchor for different dashboard modules.

## Layout & Spacing

This design system employs a **Rigid Fixed Grid** model based on a 12-column system.

- **Grid:** Layouts are full-width (`100vw`). Elements should span 1-12 columns with 16px gutters.
- **Structure:** Modules do not float; they are tethered to the grid with 1px solid borders. 
- **Density:** Padding within panels is kept tight (20px) to maximize the amount of information visible above the fold. 
- **Responsive:** On viewports below 1024px, the grid collapses into a single-column stack. Tables must be wrapped in a container that allows horizontal overflow scrolling to preserve data integrity.

## Elevation & Depth

This system avoids all forms of perceived physical depth. There are no shadows, z-axis translations, or blurred overlays.

- **Flat Hierarchy:** Depth is conveyed through **Tonal Separation** and **1px Solid Outlines**. 
- **Focus:** Selection or focus states are indicated by a 2px solid border or a change in background color (using the #FAFAFA stripe color) rather than a shadow.
- **Dividers:** Use consistent 1px #D9D9D9 borders for all separation. Use a thicker 3px solid border only for the primary header-to-content separation to anchor the page.

## Shapes

The shape language is strictly **Sharp (0px radius)**. Every UI element—including buttons, input fields, panels, and dropdowns—must feature 90-degree corners. This reinforces the "block-based" architectural feel and ensures visual consistency across the entire grid.

## Components

- **Buttons:** Rectangular blocks with solid fills. Use #1A365D for primary actions and #FFFFFF with a 1px #D9D9D9 border for secondary actions. Hover states should result in a 10% darker background with no transition timing.
- **Tables:** The core component of the system. Implement row striping (alternating #FFFFFF and #FAFAFA). Column headers are #666666, semi-bold, and 12px. Cell borders are mandatory (1px #D9D9D9).
- **Metric Blocks (KPIs):** Simple containers with a label at the top and a large monospaced number in the center. High contrast (Black on White).
- **Input Fields:** 1px #D9D9D9 solid border, 0px radius. Use #000000 for typed text and #666666 for placeholder text.
- **Analytics Panels:** Charts should use flat colors from the primary and secondary palette. Avoid 3D effects, shadows, or rounded bar caps.
- **Action Bar:** A specialized horizontal container below the main header that houses system-wide triggers, strictly aligned to the left and right margins of the grid.