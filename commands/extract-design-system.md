---
description: Extract the design system from the existing codebase and populate DESIGN.md
allowed-tools: Read, Glob, Grep, Bash, Task, Write
---

# Extract design system from codebase

Analyze the existing codebase to discover the actual design decisions already embedded in the code. Do not invent or suggest — document what IS, including inconsistencies.

Read DESIGN.md first. If it already has content, you're updating it. If it's the blank template, you're populating it from scratch.

## Step 1 — Discover the stack

Determine what we're working with before analyzing anything:
- Framework (React, Vue, Svelte, plain HTML, Jinja, etc.)
- Styling approach (Tailwind, CSS modules, styled-components, plain CSS, SCSS, etc.)
- Component library (shadcn, Radix, MUI, Chakra, Ant, Headless UI, PicoCSS, custom, none)
- Icon set (Lucide, Heroicons, FontAwesome, custom SVGs, etc.)
- Font loading (Google Fonts, local files, system fonts)

This determines where to look for design tokens.

## Step 2 — Extract color palette

**For Tailwind projects:**
- Read tailwind.config.* for custom colors in theme.extend.colors
- Grep for bg-[], text-[], border-[] class usage across all component files
- Count frequency of each color to find primary, secondary, accent

**For CSS/SCSS projects:**
- Grep for CSS custom properties (--color-*, --*-color, etc.) in :root or theme files
- Grep for hex values (#xxx, #xxxxxx), rgb(), hsl() across all stylesheets
- Count frequency to find the actual palette vs one-off values

**For CSS-in-JS / styled-components:**
- Find theme files, design token files, or constants files
- Extract color definitions

**For all approaches:**
- Group discovered colors into: backgrounds, text, borders, accents, semantic (success/warning/error)
- Flag any colors used only once (likely inconsistencies)
- Flag any near-duplicate colors (e.g., #333 and #2d2d2d used interchangeably)

## Step 3 — Extract typography

- Find font-family declarations — in CSS, Tailwind config, or global styles
- Find font imports (Google Fonts links, @font-face declarations, font files in assets/)
- Catalog every font-size in use. Group into: heading sizes, body size, small/caption sizes
- Check font-weight usage — which weights are actually used?
- Check line-height values
- Determine if there's an intentional type scale or if sizes are ad hoc

## Step 4 — Extract spacing system

- Find the spacing scale — Tailwind config (theme.spacing), CSS custom properties, or design tokens
- Grep for padding and margin values across components
- Determine if there's a consistent base unit (4px, 8px, etc.) or if spacing is ad hoc
- Check gap values in flex/grid layouts
- Extract common container max-widths and page margins

## Step 5 — Extract component patterns

Scan the component/template directory structure. For each of these categories, find the existing pattern (or note that none exists):

- **Buttons** — what variants exist? (filled, outline, ghost, sizes, states)
- **Form inputs** — label position, error display, placeholder usage
- **Cards** — padding, radius, shadow, border patterns
- **Modals/dialogs** — how are they structured? Overlay style? Close behavior?
- **Navigation** — sidebar, top bar, bottom tabs, breadcrumbs?
- **Tables** — headers, striping, sorting, empty states?
- **Loading states** — spinners, skeletons, progress bars?
- **Empty states** — what pattern is used when there's no data?
- **Error states** — how are errors displayed to users?
- **Toasts/notifications** — position, duration, style?

For each, note the file path of the best example (becomes the reference implementation).

## Step 6 — Extract responsive breakpoints

- Find breakpoint definitions — Tailwind config, CSS media queries, or JS constants
- Check which breakpoints are actually used (vs defined but unused)
- Find the most responsive component and note what changes at each breakpoint
- Check if navigation changes between mobile and desktop

## Step 7 — Extract animation and motion

- Grep for transition, animation, @keyframes, transform across all styles
- Check for prefers-reduced-motion handling
- Catalog transition durations and easing functions in use
- Note whether motion is consistent or ad hoc

## Step 8 — Check accessibility baseline

- Grep for aria-* attributes — are they used consistently?
- Check for alt attributes on images
- Look for skip-to-content links
- Check focus styles — are they customized or browser defaults?
- Look for any a11y-related utilities, hooks, or test configs

## Step 9 — Find inconsistencies

This is the most important step. Compare everything you found:

- Colors used that aren't in the palette/theme
- Font sizes that aren't in the type scale
- Spacing values that aren't on the spacing grid
- Components that do the same thing but look different
- Patterns that are handled multiple ways (e.g., loading shown as spinner in one place, skeleton in another)

## Step 10 — Write DESIGN.md

Populate each section of DESIGN.md with what you found. For each section:

1. **Document the dominant pattern** — what the codebase does most of the time
2. **Note deviations** — where the code strays from its own patterns (as HTML comments, so they don't become instructions)
3. **Leave the anti-patterns section empty** — that's for the developer to fill in based on their intentions, not for you to assume

Use exact values from the code (hex colors, pixel values, font names). Don't round, approximate, or "clean up" — document what's actually there so the developer can see the real state and decide what to standardize.

If a section has no discernible pattern (e.g., spacing is completely ad hoc), say so explicitly and list the values in use.

End with a summary of the top 5 inconsistencies that would have the most impact if standardized.
