---
name: Industrial Precision
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#414943'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0ef'
  outline: '#717972'
  outline-variant: '#c0c9c0'
  surface-tint: '#36684c'
  primary: '#11462d'
  on-primary: '#ffffff'
  primary-container: '#2c5e43'
  on-primary-container: '#a0d5b3'
  inverse-primary: '#9dd3b0'
  secondary: '#566067'
  on-secondary: '#ffffff'
  secondary-container: '#dae4ed'
  on-secondary-container: '#5c666d'
  tertiary: '#612e33'
  on-tertiary: '#ffffff'
  tertiary-container: '#7d4449'
  on-tertiary-container: '#ffb7bb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b8efcc'
  primary-fixed-dim: '#9dd3b0'
  on-primary-fixed: '#002111'
  on-primary-fixed-variant: '#1d5036'
  secondary-fixed: '#dae4ed'
  secondary-fixed-dim: '#bec8d0'
  on-secondary-fixed: '#131d23'
  on-secondary-fixed-variant: '#3e484f'
  tertiary-fixed: '#ffdadb'
  tertiary-fixed-dim: '#feb3b7'
  on-tertiary-fixed: '#370c12'
  on-tertiary-fixed-variant: '#6d373c'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e5e2e1'
  background-surface: '#F9F9F9'
  container-fill: '#FFFFFF'
  slate-gray: '#555555'
  light-gray: '#E0E0E0'
  forest-hover: '#1F422F'
typography:
  h1:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  helper-text:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  button-text:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
spacing:
  container-max-width: 600px
  margin-page: 2rem
  gutter: 1.5rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
  stack-lg: 2rem
---

## Brand & Style

This design system is defined by a **Minimalist and Utilitarian** philosophy. It prioritizes clarity, efficiency, and professional trust over decorative trends. The aesthetic is intentionally "un-designed" to evoke a sense of institutional reliability and industry-standard functionality.

The visual language follows **Flat Design** principles with a focus on high-contrast borders and structured whitespace rather than depth or gradients. It is designed for high-stakes environments like enterprise SaaS, logistics, and data collection where the user's focus must remain entirely on the task at hand.

- **Minimalism:** Use generous internal padding within containers while maintaining a compact overall layout.
- **Utilitarian:** Every element serves a specific function; if an element does not assist in data entry or legibility, it is removed.
- **Flat UI:** Depth is communicated through color-blocking and 1px strokes.

## Colors

The palette uses grounded, earthy, and industrial tones. The primary objective is readability and clear state differentiation.

- **Primary (Forest Green):** Reserved exclusively for successful actions and primary "Submit" buttons.
- **Neutral (Charcoal):** Used for primary text and high-emphasis borders to ground the interface.
- **Secondary (Steel Gray):** Used for secondary actions and non-critical UI elements.
- **Functional Layers:** The background uses an off-white tint to reduce glare, while the white container-fill provides a crisp workspace for data entry.

## Typography

The system utilizes **Inter** for its neutral, highly legible neo-grotesque qualities. 

- **Hierarchy:** Contrast is established through weight and color rather than drastic size changes.
- **Labels:** Set in semi-bold Slate Gray to differentiate from user input while maintaining accessibility.
- **Body:** The standard 16px size ensures comfortable reading for long-form feedback or data review.
- **Alignment:** All text is strictly left-aligned to maintain a strong vertical axis for the eye to follow.

## Layout & Spacing

This design system uses a **Fixed Grid** approach for form layouts to prevent inputs from becoming excessively wide and difficult to read.

- **Structure:** Content is centered in a 600px container. 
- **Grid:** A standard 12-column logic is applied within the container, typically split into 2-column (half-width) or 1-column (full-width) rows.
- **Vertical Rhythm:** Elements are stacked using a 4px-based scale. Inputs are separated by 24px (stack-md), while labels are pinned to their inputs with 8px (stack-sm) spacing.
- **Mobile Adaptation:** At breakpoints below 768px, all multi-column layouts reflow into a single column. Margin-page is reduced to 1rem to maximize input space.

## Elevation & Depth

This system avoids all box shadows and blurs. Depth is achieved entirely through **Tonal Layers** and **1px Borders**.

- **Background:** The base layer is `#F9F9F9`.
- **Surface:** Form containers are `#FFFFFF` with a 1px `#E0E0E0` border.
- **Focus States:** When an element is active, the border shifts to Charcoal `#222222`. This provides a high-contrast visual cue without the need for glowing effects or "pop-out" shadows.
- **Dividers:** Horizontal rules should be used sparingly, only to separate distinct logical sections (e.g., Personal Info vs. Feedback).

## Shapes

The shape language is **Sharp and Rigid**. 

- **Radius:** A maximum border-radius of 2px may be applied to buttons and input fields to prevent a "needle-sharp" feel on high-density displays, but the visual intent should remain effectively square.
- **Consistency:** All components—inputs, buttons, and container cards—must share the same corner treatment.

## Components

### Buttons
- **Primary:** Solid Forest Green `#2C5E43` background, White text. No border. Darkens to `#1F422F` on hover.
- **Secondary/Clear:** Transparent background, Steel Gray `#88929A` 1px border and text.

### Input Fields
- **Default:** 1px Light Gray `#E0E0E0` border, White background.
- **Focus:** 1px Charcoal `#222222` border.
- **Text:** 16px Charcoal text.
- **Textarea:** Minimum height of 4 rows, vertical-only resize restricted.

### Selection Controls
- **Select/Dropdown:** Standard appearance with a 1px border. Avoid custom animated arrows; use a simple 10px chevron.
- **Radio/Checkbox:** Square containers to match the shape language. Selected state uses Forest Green.
- **Numbered Blocks:** For ratings (1-5), use adjacent square blocks with 1px borders. The selected block fills with Charcoal or Forest Green.

### Cards & Sections
- **Form Container:** Pure white background, 1px Light Gray border, 0px or 2px radius. Internal padding should be a minimum of 32px (stack-lg).