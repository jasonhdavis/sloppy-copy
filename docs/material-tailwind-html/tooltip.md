### Tooltip


Customize your web projects with an easy-to-use and responsive Tailwind CSS
tooltip!

A tooltip is a small pop-up element that appears while the user moves the
mouse pointer over an element. Use it when you want to specify extra
information about something when the user moves the mouse pointer over an
element.

See below our examples that will help you create a simple tooltip for your
project.

  

## Tooltip Examples:

## Default Tooltip

You can initialize a new tooltip by adding the `data-tooltip-
target="`{tooltipName}`"` data attribute to the trigger element and the `data-
tooltip="`{tooltipName}`"` to the element that you want to use as the tooltip.

Show Tooltip

Material Tailwind

    
    
      <button data-ripple-light="true" data-tooltip-target="tooltip"
        class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
        Show Tooltip
      </button>
      <div data-tooltip="tooltip"
        class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
        Material Tailwind
      </div>

* * *

## Tooltip Placement

You can change the position of the tooltip relative to it's trigger element by
adding the `data-tooltip-placement="`{top}`"` data attribute to the tooltip
element by default it set's to `top`.  
Check the placement values for tooltip here.

Top

Material Tailwind

Top Start

Material Tailwind

Top End

Material Tailwind

Right

Material Tailwind

Right Start

Material Tailwind

Right End

Material Tailwind

Bottom

Material Tailwind

Bottom Start

Material Tailwind

Bottom End

Material Tailwind

Left

Material Tailwind

Left Start

Material Tailwind

Left End

Material Tailwind

    
    
      <div class="flex gap-3 mb-3">
        <button data-ripple-light="true" data-tooltip-target="tooltip-top"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Top
        </button>
        <div data-tooltip="tooltip-top" data-tooltip-placement="top"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-top-start"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Top Start
        </button>
        <div data-tooltip="tooltip-top-start" data-tooltip-placement="top-start"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-top-end"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Top End
        </button>
        <div data-tooltip="tooltip-top-end" data-tooltip-placement="top-end"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
      </div>
      <div class="flex gap-3 mb-3">
        <button data-ripple-light="true" data-tooltip-target="tooltip-right"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Right
        </button>
        <div data-tooltip="tooltip-right" data-tooltip-placement="right"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-right-start"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Right Start
        </button>
        <div data-tooltip="tooltip-right-start" data-tooltip-placement="right-start"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-right-end"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Right End
        </button>
        <div data-tooltip="tooltip-right-end" data-tooltip-placement="right-end"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
      </div>
      <div class="flex gap-3 mb-3">
        <button data-ripple-light="true" data-tooltip-target="tooltip-bottom"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Bottom
        </button>
        <div data-tooltip="tooltip-bottom" data-tooltip-placement="bottom"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-bottom-start"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Bottom Start
        </button>
        <div data-tooltip="tooltip-bottom-start" data-tooltip-placement="bottom-start"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-bottom-end"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Bottom End
        </button>
        <div data-tooltip="tooltip-bottom-end" data-tooltip-placement="bottom-end"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
      </div>
      <div class="flex gap-3 mb-3">
        <button data-ripple-light="true" data-tooltip-target="tooltip-left"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Left
        </button>
        <div data-tooltip="tooltip-left" data-tooltip-placement="left"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-left-start"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Left Start
        </button>
        <div data-tooltip="tooltip-left-start" data-tooltip-placement="left-start"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
        <button data-ripple-light="true" data-tooltip-target="tooltip-left-end"
          class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
          Left End
        </button>
        <div data-tooltip="tooltip-left-end" data-tooltip-placement="left-end"
          class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
          Material Tailwind
        </div>
      </div>

* * *

## Custom Tooltip Animation

You can modify the open/close state animation for tooltip by adding the `data-
tooltip-mount="`{opacity-100}`"`, `data-tooltip-unmount="`{opacity-0}`"` and
`data-tooltip-transition="`{transition-opacity}`"` data attributes to the
tooltip element. You can pass tailwind css classnames for those data
attributes for animation the tooltip.  
Check more about animation data attributes for tooltip here.

Show Tooltip

Material Tailwind

    
    
      <button data-ripple-light="true" data-tooltip-target="tooltip-animation"
        class="select-none rounded-lg bg-gray-900 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-gray-900/10 transition-all hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
        Show Tooltip
      </button>
      <div data-tooltip="tooltip-animation" data-tooltip-mount="opacity-100 scale-100"
        data-tooltip-unmount="opacity-0 scale-0 pointer-events-none"
        data-tooltip-transition="transition-all duration-200 origin-bottom"
        class="absolute z-50 whitespace-normal break-words rounded-lg bg-black py-1.5 px-3 font-sans text-sm font-normal text-white focus:outline-none">
        Material Tailwind
      </div>

* * *

## Tooltip Trigger Data Attributes

The following data attributes are available for tooltip trigger element.

Attribute| Description  
---|---  
`data-tooltip-target`| Set the tooltip target element, it should be the same
as the `data-tooltip` data attribute.  
  
* * *

## Tooltip Data Attributes

The following data attributes are available for tooltip element.

Attribute| Description| Default  
---|---|---  
`data-tooltip`| Set the name of the tooltip and reference it to the  
tooltip trigger element.|  
`data-tooltip-offset`| Set the offset between the tooltip and the tooltip
trigger element.| 5  
`data-tooltip-placement`| Set the position of the tooltip relative to it's
trigger element.| `top`  
`data-tooltip-mount`| Set the classnaes that should be used when the  
tooltip is visible.| `opacity-1`  
`data-tooltip-unmount`| Set the classnaes that should be used when the  
tooltip is hidden.| `opacity-0`  
`pointer-events-none`  
`data-tooltip-transition`| Set the classnaes that should be used for  
transition of the tooltip.| `transition-opacity`  
`duration-300`  
  
* * *

## Required Scripts

The tooltip component needs a required script file to work, you just need to
add the below script file to the bottom of your html file.

    
    
    <!-- from node_modules -->
    <script
      type="module"
      src="node_modules/@material-tailwind/html@latest/scripts/tooltip.js"
    ></script>
     
    <!-- from cdn -->
    <script
      type="module"
      src="https://unpkg.com/@material-tailwind/html@latest/scripts/tooltip.js"
    ></script>



