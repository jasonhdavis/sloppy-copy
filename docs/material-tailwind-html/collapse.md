### Collapse


Use our Tailwind CSS collapse component to allow the user to show and hide
sections of related content on a page.

There are many ways to use this component, like displaying a list of FAQs,
showing various menus and submenus, displaying the locations of a particular
company, and so on.

See below our simple and versatile collapse example that you can use in your
Tailwind CSS projects. We also included some collapse props that are
available.

  

## Collapse Example:

## Default Collapse

Save valuable screen space and allow users to control their interaction with
the content using our collapse component example. Copy-paste the code directly
to your project.

Open Collapse

Use our Tailwind CSS collapse for your website. You can use if for accordion,
collapsible items and much more.

    
    
    <button 
      data-collapse-target="collapse"
      class="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
      Open Collapse
    </button>
    <div
      data-collapse="collapse"
      class="block h-0 w-full basis-full overflow-hidden transition-all duration-300 ease-in-out"
    >
      <div class="relative mx-auto flex w-8/12 flex-col rounded-lg bg-white border border-slate-200 shadow-sm mt-4">
        <div class="p-4">
          <p class="text-slate-600 font-light">
            Use our Tailwind CSS collapse for your website. You can use if for
            accordion, collapsible items and much more.
          </p>
        </div>
      </div>
    </div>

  

The button from this collapse component is styled with Tailwind CSS to have a
dark background, white text, rounded corners; and interactive feedback (shadow
effects on hover, focus, and active states). The content inside the
collapsible area is a simple paragraph.

The styling (` text-slate-600 font-light `) ensures the text is readable and
aesthetically pleasing.

* * *

## Collapse Trigger Data Attributes

The following data attributes are available for collapse trigger element.

Attribute| Description  
---|---  
`data-collapse-target`| Set the collapse target element, it should be the same
as the  
`data-collapse` data attribute.  
  
* * *

## Collapse Data Attributes

The following data attributes are available for collapse element.

Attribute| Description  
---|---  
`data-collapse`| Set the collapse element, it should be the same as the  
`data-collapse-target` data attribute.  
  
* * *

## Required Scripts

The collapse component needs a required script file to work, you just need to
add the below script file to the bottom of your html file.

    
    
    <!-- from node_modules -->
    <script src="node_modules/@material-tailwind/html/scripts/collapse.js"></script>
     
    <!-- from cdn -->
    <script src="https://unpkg.com/@material-tailwind/html@latest/scripts/collapse.js"></script>

* * *

  

* * *

## Explore More Tailwind CSS Examples

Check out more collapse components examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks).

* * *

## Collapse Component Best Practice for Developers

• Apply smooth animations and transitions when expanding or collapsing
content.  
• Build collapsible components in a way that they work without JavaScript
enabled.  
• Keep the content within the collapsible section well-structured. Use
appropriate heading levels (`<h2>`, `<h3>`, etc.) for section titles to
maintain a logical document outline.  
• Consider using clear and intuitive toggle icons (e.g., "+" and "-") next to
the trigger element to indicate the open/close state.



