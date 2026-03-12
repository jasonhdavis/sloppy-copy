# Material Tailwind Style Guide — NYT Aesthetic

## Core Philosophy
The "New York Times" look is defined by high-contrast typography, generous whitespace, and a "paper-like" feel. We use Material Tailwind components but strip away heavy shadows and rounded corners to achieve a more traditional editorial aesthetic.

## Typography
- **Headlines**: `font-serif` (Playfair Display or Georgia). Bold, high contrast.
- **Body Text**: `font-serif` for articles. `font-sans` (Inter/Roboto) for UI labels and metadata.
- **Scale**:
  - Main Headline: `text-4xl` to `text-5xl`
  - Section Header: `text-2xl`
  - Body: `text-lg` with `leading-relaxed`

## Color Palette
- **Primary**: `#000000` (Black) - Text and borders.
- **Secondary**: `#666666` (Gray) - Metadata and deks.
- **Background**: `#FFFFFF` (White) - Main content.
- **Accent**: `#326891` (NYT Blue) - Links and interactive elements.

## Component Styling (Material Tailwind)

### Cards
- **Base**: `shadow-none border-b border-gray-300 rounded-none bg-transparent`
- **Padding**: `py-6 px-0` (Vertical stacking like a newspaper)

### Buttons
- **Primary**: `variant="filled" class="bg-black rounded-none shadow-none hover:shadow-none"`
- **Secondary**: `variant="outlined" class="border-black text-black rounded-none"`
- **Text**: `variant="text" class="text-blue-gray-900 hover:bg-gray-100"`

### Navigation
- **Header**: Centered logo, thin black borders top and bottom.
- **Links**: `font-sans uppercase text-xs tracking-widest font-bold`

### Badges (Status)
- **Style**: `variant="ghost" class="rounded-none border border-gray-400 text-gray-700 text-[10px] uppercase"`

## Layout Patterns
- **The "Front Page" Grid**: 3-column layout on desktop.
- **The "Article" View**: Single column, centered, max-width `max-w-3xl`.
- **Borders**: Use `border-t` and `border-b` to separate sections rather than boxes.

## Example: NYT-Style Article Card
```html
<div class="flex flex-col py-6 border-b border-gray-200">
  <span class="font-sans text-xs font-bold uppercase tracking-tighter text-gray-600 mb-1">
    Technology
  </span>
  <h2 class="font-serif text-2xl font-bold text-black leading-tight mb-2 hover:text-gray-700 cursor-pointer">
    AI Pipeline Achieves Human-Like Editorial Standards
  </h2>
  <p class="font-serif text-base text-gray-800 leading-snug mb-3">
    New developments in agentic workflows allow for sophisticated content generation that mirrors the tone of major publications...
  </p>
  <div class="flex items-center gap-2">
    <span class="font-sans text-[10px] text-gray-500">By THE TREND DECODER</span>
    <span class="text-gray-300">|</span>
    <span class="font-sans text-[10px] text-gray-500">MARCH 12, 2026</span>
  </div>
</div>
```
