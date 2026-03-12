# STYLE_GUIDE.md

## Aesthetic: The New York Times (Digital)
The goal is to create a "credible" and "authoritative" look using Material Tailwind components.

## Typography
- **Headlines**: Serif (e.g., Playfair Display or Georgia). High contrast, bold.
- **Body**: Serif for articles, Sans-serif (Inter/Roboto) for UI elements.
- **Scale**: Large, impactful headlines; generous line-height for readability.

## Color Palette
- **Primary**: `#000000` (Black)
- **Secondary**: `#666666` (Gray)
- **Background**: `#FFFFFF` (White) or `#F9F9F9` (Off-white)
- **Accents**: Minimal use of `#326891` (NYT Blue) for links.

## Layout Patterns
- **Header**: Centered logo/title, thin black borders (top/bottom).
- **Cards**: No shadows, thin borders (`border-gray-300`), generous padding.
- **Grid**: Standard multi-column layout for dashboards.

## Material Tailwind Components
- **Buttons**: Use `variant="outlined"` or `variant="text"` for a cleaner look. Avoid heavy shadows.
- **Cards**: Use `shadow-none border border-blue-gray-100`.
- **Typography**: Use `font-serif` for content and `font-sans` for metadata.

## HTMX Interactions
- **Modals**: Use for quick edits or detail views.
- **Inline Edits**: Prefer inline status changes over separate pages.
- **Loading States**: Use subtle progress bars or spinners.

## Example Card Structure
```html
<div class="relative flex flex-col mt-6 text-gray-700 bg-white border border-blue-gray-100 shadow-none bg-clip-border rounded-none w-96">
  <div class="p-6">
    <h5 class="block mb-2 font-serif text-xl antialiased font-semibold leading-snug tracking-normal text-blue-gray-900">
      Headline Goes Here
    </h5>
    <p class="block font-serif text-base antialiased font-light leading-relaxed text-inherit">
      The body text should be serif and easy to read...
    </p>
  </div>
  <div class="p-6 pt-0">
    <button class="select-none rounded-none bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-none transition-all hover:shadow-none focus:opacity-[0.85] active:opacity-[0.85]" type="button">
      Read More
    </button>
  </div>
</div>
```
