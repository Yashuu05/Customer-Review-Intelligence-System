# Customer Feedback Form - UI/UX Design Specification

## 1. Design Philosophy
The design approach for the Customer Feedback Form follows a **clean, minimalist, and utilitarian** aesthetic. It completely avoids the common "AI-generated" look (no dark mode, no gradients, no emojis, no excessive box shadows, and no vibrant blue/purple palettes). Instead, it focuses on high contrast, clear typography, and a structured layout that feels professional, trustworthy, and industry-standard.

## 2. Color Palette
The color scheme is neutral and grounded, using earthy and industrial tones to convey reliability.

* **Background:** Off-White (`#F9F9F9`) - Keeps the interface bright but reduces eye strain compared to pure white.
* **Form Container:** Pure White (`#FFFFFF`) - Creates a natural separation from the background without needing drop shadows.
* **Primary Text:** Charcoal (`#222222`) - For all headings and body text to ensure maximum readability.
* **Secondary Text (Labels & Hints):** Slate Gray (`#555555`)
* **Primary Accent (Submit Button):** Forest Green (`#2C5E43`) - A mature, professional green that indicates success/submission.
* **Secondary Accent (Clear Button / Borders):** Steel Gray (`#88929A`)
* **Borders & Dividers:** Light Gray (`#E0E0E0`)

## 3. Typography
The typography relies on standard, highly legible geometric or neo-grotesque sans-serif fonts to maintain a timeless and enterprise-ready look.

* **Primary Font Family:** `Inter`, `Helvetica Neue`, `Arial`, sans-serif.
* **Headings (H1):** 24px, Bold, Charcoal. Left-aligned.
* **Labels:** 14px, Semi-bold, Slate Gray.
* **Input Text:** 16px, Regular, Charcoal.

## 4. UI Elements & Styling Guidelines
* **Borders:** Sharp corners or very subtle rounding (max `2px` border-radius). All form fields have a solid `1px` Light Gray border.
* **Shadows:** Absolutely **NO** box shadows. Depth is created through layout structure and border lines (flat design).
* **States:** 
  * *Focus:* When an input is focused, the border color changes to Charcoal (`#222222`). No glow effects.
  * *Hover:* Buttons darken slightly on hover (e.g., Forest Green `#2C5E43` to `#1F422F`).

## 5. Layout & Wireframe Structure
The form is centered on the screen, constrained to a maximum width (e.g., `600px`) to ensure the inputs do not stretch uncomfortably on large screens.

### Header
* **Title:** "Customer Feedback Form"
* **Subtitle:** A brief, professional instruction (e.g., "Please provide your details and feedback below to help us improve our services.")

### Section 1: Personal Information (Grid Layout)
* **Row 1:** 
  * Age (Number input, half-width)
  * Gender (Dropdown/Select, half-width)
* **Row 2:** 
  * Role (Dropdown/Select or Text input, full-width)

### Section 2: Geographic Information (Grid Layout)
* **Row 3:** 
  * State (Dropdown/Select, half-width)
  * City (Text input, half-width)

### Section 3: Feedback & Rating
* **Row 4:** 
  * Rating (Radio buttons or a clean 1-5 dropdown. No star emojis. Simple numbered blocks or a standard select menu).
* **Row 5:** 
  * Customer Feedback (Textarea, full-width, minimum 4 rows height. Resize restricted to vertical only).

### Footer / Actions
* Aligned to the right.
* **Clear Form Button:** Flat design, Steel Gray text, transparent background with a solid Steel Gray border.
* **Submit Button:** Flat design, Solid Forest Green background, White text. Placed to the right of the Clear button.

## 6. Responsiveness
* On mobile devices (below `768px`), all multi-column grid layouts (like Age/Gender) stack vertically to become 100% width for ease of interaction. Padding is reduced to maximize screen real estate.
