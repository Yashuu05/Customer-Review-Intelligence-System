# Admin Dashboard - UI/UX Design Specification

## 1. Design Philosophy
The Admin Dashboard requires a highly functional, data-heavy interface. The design focuses on **information density, clarity, and utilitarianism**. It avoids modern web trends like floating cards, heavy drop shadows, neon accents, and dark modes. Instead, it draws inspiration from classic, robust enterprise software and print typography. The interface should feel like a serious administrative tool, ensuring that data and analytics are the central focus.

## 2. Color Palette
The color palette uses muted, professional colors that prevent visual fatigue during long periods of manual analysis.

* **Background:** Light Gray (`#F0F0F0`) - Provides a solid, neutral canvas.
* **Panels & Modules:** Pure White (`#FFFFFF`) - Used for the main content areas, tables, and metric blocks to separate them from the background.
* **Primary Text:** Black (`#000000`) or very Dark Gray (`#111111`) - High contrast for maximum readability of dense data.
* **Secondary Text (Table Headers, Meta Info):** Medium Gray (`#666666`).
* **Borders & Dividers:** Ash Gray (`#D9D9D9`) - Used extensively to define grids, tables, and sections.
* **Action Buttons (Primary):** Navy Blue (`#1A365D`) or Deep Slate (`#3A4A5A`) - A conservative, authoritative color for primary actions.
* **Action Buttons (Secondary/Destructive):** Muted Crimson (`#8B0000`) or simple transparent buttons with solid borders.

## 3. Typography
The dashboard prioritizes scannability and precise alignment.

* **Primary Font Family:** `Roboto`, `Helvetica`, `Arial`, sans-serif.
* **Monospace Font (for numerical data/IDs):** `Courier New`, `Consolas`, or `Roboto Mono` to ensure numbers align perfectly in tables.
* **Dashboard Title:** 28px, Bold, Black.
* **Widget/Section Titles:** 18px, Semi-bold, Dark Gray. Uppercase with slight letter-spacing can be used for section headers to create a structured feel.
* **Data Text / Table Content:** 14px, Regular, Black.

## 4. UI Elements & Styling Guidelines
* **Layout Structure:** A rigid, block-based grid system (like a classic CSS grid layout). Elements span defined columns without overlapping.
* **Cards & Panels:** No border-radius (sharp corners: `0px`) and no drop shadows. Panels are distinguished strictly by a `1px` solid border (`#D9D9D9`) and a white background.
* **Tables:** 
  * Striped rows (alternating white and very light gray `#FAFAFA`) for easy reading across wide screens.
  * Clear, solid borders separating rows and columns.
  * Left-align text, right-align numbers.
* **Buttons:** Flat rectangles. Solid background color, sharp corners. Changes to a slightly darker shade on hover. No transitions or animations.

## 5. Layout & Wireframe Structure
The dashboard is a full-width layout (using `100vw`), divided into distinct logical sections.

### Top Navigation / Header
* **Left:** Project Title ("Customer Review Intelligence - Admin Panel").
* **Right:** Logged-in User Info and **Logout Button**.
* **Bottom Border:** A thick, solid horizontal line separating the header from the dashboard content.

### Action Bar (Sub-header)
A dedicated row directly beneath the header containing system-level controls:
* **Launch Feedback Form Button** (Primary action)
* **Close Form Button**
* **Refresh Button** (Secondary action)

### Main Dashboard Grid
The main area is divided into a dashboard-style grid to showcase analytics and the data table.

**Row 1: High-Level Analytics (Key Performance Indicators)**
A row of equally sized metric blocks.
* Total Feedbacks (Large number)
* Average Rating (e.g., "4.2 / 5")
* Feedback Results (e.g., Positive: 1,200 | Negative: 340)

**Row 2: Visual Analytics (Charts & Graphs)**
* **Left Panel:** Age Distribution & Role Count (Simple bar charts or tabular lists, avoiding 3D effects or excessive colors).
* **Center Panel:** Gender Count & Geographic Locations (List format or a very minimal flat map/table showing top states/cities).

**Row 3: LLM Insights (Text Analysis)**
Divided into two distinct, side-by-side text panels.
* **Left Panel: Feedback Summary**
  * Title: "Feedback Summary (LLM)"
  * Content area (scrollable if needed).
  * Action: **Generate Feedback Summary Button** placed neatly at the top or bottom of this panel.
* **Right Panel: Business Solution**
  * Title: "Recommended Business Solutions (LLM)"
  * Content area showing actionable insights.
  * Action: **Generate Solution Button**.

**Row 4: Raw Customer Information Table**
A full-width section at the bottom to view the raw data.
* **Table Columns:** ID | Age | Gender | Role | State | City | Rating | Feedback | Sentiment | Probability Score.
* Features pagination or a vertical scrollbar.

## 6. Responsiveness
While Admin Dashboards are typically used on desktop monitors, the grid should cleanly reflow into a single column for tablet or smaller screens. The data table should allow horizontal scrolling on smaller viewports to prevent data truncation.
