### Chip


Get started on your web projects with our Tailwind CSS Chip (also known as
Pills or Tags) which is a compact element that represents an input, attribute,
or action. This element appears dynamically as a group of multiple interactive
elements and allows users to enter information, make selections, filter
content, or trigger actions.

They often come with the capability to be removed or interacted with, allowing
users to manipulate the data or selection represented by the chip.

See below our responsive chip component examples styled with Tailwind CSS that
you can use for your web or mobile projects.

  

## Chip Examples:

## Default Chip

Use this simple chip with slate background as a starting point for your
application.

Chip

    
    
    <div class="rounded-md bg-slate-800 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
      Chip
    </div>

* * *

## Chips Variants

This example presents 4 different styles of chip components styled with
Tailwind CSS, showcasing the versatility of chip design for different UI use
cases.

Chip Filled

Chip Gradient

Chip Outlined

Chip Ghost

    
    
    <div class="flex gap-2">
      <div class="rounded-md bg-slate-800 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Chip Filled
      </div>
      <div class="rounded-md bg-gradient-to-tr from-slate-800 to-slate-700 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Chip Gradient
      </div>
      <div class="rounded-md border border-slate-300 py-0.5 px-2.5 text-center text-sm transition-all shadow-sm text-slate-600">
        Chip Outlined
      </div>
      <div class="rounded-md bg-slate-100 py-0.5 px-2.5 border border-transparent text-sm text-slate-600 transition-all shadow-sm">
        Chip Ghost
      </div>
    </div>

* * *

  

Each chip is contained within a `<div>` element and designed with a consistent
structure but different visual styles: filled, gradient, outlined, and ghost.

## Chips Sizes

Check out this example to see how you can implement chips with different
sizes. The differences in size are primarily achieved through varying the
padding values.

Small Chip

Medium Chip

Large Chip

    
    
    <div class="rounded-md bg-slate-800 py-0.5 px-2.5 border border-transparent text-xs text-white transition-all shadow-sm">
      Small Chip
    </div>
    <div class="rounded-md bg-slate-800 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
      Medium Chip
    </div>
    <div class="rounded-md bg-slate-800 py-1 px-3 border border-transparent text-sm text-white transition-all shadow-sm">
      Large Chip
    </div>

  

The varying sizes allow web designers to cater to different spatial and
functional requirements within an interface.

* * *

## Chips Colors

The Chip component comes with 19 different colors like blue, red, green, and
amber that you can change using the color class. Check out below some of the
available colors in action.

Blue

Red

Green

Amber

Pink

Indigo

Purple

Teal

Cyan

    
    
    <div class="flex gap-2">
      <div class="rounded-md bg-blue-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Blue 
      </div>
      <div class="rounded-md bg-red-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Red 
      </div>
      <div class="rounded-md bg-green-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Green 
      </div>
      <div class="rounded-md bg-amber-600 py-0.5 px-2.5 border border-transparent text-sm text-slate-800 transition-all shadow-sm">
        Amber 
      </div>
      <div class="rounded-md bg-pink-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Pink 
      </div>
      <div class="rounded-md bg-indigo-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Indigo 
      </div>
      <div class="rounded-md bg-purple-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Purple 
      </div>
      <div class="rounded-md bg-teal-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Teal 
      </div>
      <div class="rounded-md bg-cyan-600 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Cyan 
      </div>
    </div>

* * *

## Chips with Icon

The icons, in this example, add a visual element that can improve user
understanding or interaction with the chip, such as representing user
accounts, settings, notifications, etc.

Chip Filled

Chip Gradient

Chip Outlined

Chip Ghost

    
    
    <div class="flex gap-2">
      <div class="rounded-md flex items-center bg-slate-800 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 mr-1.5">
          <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
        </svg>
     
        Chip Filled
      </div>
      <div class="rounded-md flex items-center bg-gradient-to-tr from-slate-800 to-slate-700 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 mr-1.5">
          <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
        </svg>
        
        Chip Gradient
      </div>
      <div class="rounded-md flex items-center border border-slate-300 py-0.5 px-2.5 text-center text-sm transition-all shadow-sm text-slate-600">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 mr-1.5">
          <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
        </svg>
     
        Chip Outlined
      </div>
      <div class="rounded-md flex items-center bg-slate-100 py-0.5 px-2.5 border border-transparent text-sm text-slate-600 transition-all shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 mr-1.5">
          <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
        </svg>
     
        Chip Ghost
      </div>
    </div>

* * *

## Chips Dismissible

You can make a chip dismissible by adding the `data-dismissible="chipName"`
data attribute to the chip element and the `data-dismissible-
target="chipName"` data attribute to the element that you want to close the
chip with.

Dismissible

    
    
    <div id="chip" class="relative rounded-md flex bg-slate-800 py-0.5 pl-2.5 pr-8 border border-transparent text-sm text-white transition-all shadow-sm">
      Dismissible 
     
      <button
        class="flex items-center justify-center transition-all p-1 rounded-md text-white hover:bg-white/10 active:bg-white/10 absolute top-0.5 right-0.5"
        type="button"
        onclick="closeAlert()"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
          <path d="M5.28 4.22a.75.75 0 0 0-1.06 1.06L6.94 8l-2.72 2.72a.75.75 0 1 0 1.06 1.06L8 9.06l2.72 2.72a.75.75 0 1 0 1.06-1.06L9.06 8l2.72-2.72a.75.75 0 0 0-1.06-1.06L8 6.94 5.28 4.22Z" />
        </svg>
      </button>
    </div>
     
    <script>
      function closeAlert() {
        const chipElement = document.getElementById('chip');
        chipElement.style.display = 'none'; // Hide the chip
      }
    </script>

  

The example offers users the ability to remove or dismiss the chip from the
UI, typically used in scenarios where users can select and then opt to remove
choices, such as tags, filters, or selections.

* * *

## Chips with Avatar

Use the example below for a chip component containing an avatar. It
incorporates visual identity alongside textual information, making it ideal
for user interfaces where user recognition is key, such as in social media
platforms, messaging apps, or user dashboards.

![Tania
Andrew](https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80)

Tania Andrew

    
    
    <div class="rounded-full flex items-center bg-slate-800 py-0.5 pr-2.5 pl-1.5 border border-transparent text-sm text-white transition-all shadow-sm">
      <div class="h-5 w-5 mr-2">
        <img
          alt="Tania Andrew"
          src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=1480&amp;q=80"
          class="h-full w-full rounded-full object-cover object-center"
        />
      </div>
      
      Tania Andrew 
    </div>

* * *

## Chip Pills

Use this example of chip if you want to implement a pill-like shape for your
component - fully rounded ends (`rounded-full` in Tailwind CSS).

Chip Filled

Chip Gradient

Chip Outlined

Chip Ghost

    
    
     <div class="flex gap-2">
      <div class="rounded-full bg-slate-800 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Chip Filled
      </div>
      <div class="rounded-full bg-gradient-to-tr from-slate-800 to-slate-700 py-0.5 px-2.5 border border-transparent text-sm text-white transition-all shadow-sm">
        Chip Gradient
      </div>
      <div class="rounded-full border border-slate-300 py-0.5 px-2.5 text-center text-sm transition-all shadow-sm text-slate-600">
        Chip Outlined
      </div>
      <div class="rounded-full bg-slate-100 py-0.5 px-2.5 border border-transparent text-sm text-slate-600 transition-all shadow-sm">
        Chip Ghost
      </div>
    </div>

* * *

## Chip with Status

This example showcases 2 status indicator chips: one indicating "Online"
status and the other indicating "Offline" status. These chips use color
coding, text, and a visual marker to convey the status clearly and concisely.

Online

Offline

    
    
    <div class="flex gap-2">
      <div class="rounded-md flex items-center bg-green-100 py-0.5 px-2.5 border border-transparent text-sm text-green-800 transition-all shadow-sm">
        <div class="mx-auto block h-2 w-2 rounded-full bg-green-800 mr-2"></div>
        Online 
      </div>
     
      <div class="rounded-md flex items-center bg-red-100 py-0.5 px-2.5 border border-transparent text-sm text-red-800 transition-all shadow-sm">
        <div class="mx-auto block h-2 w-2 rounded-full bg-red-800 mr-2"></div>
        Offline 
      </div>
    </div>

* * *

## Chip with Checkbox

This example showcases 2 interactive status indicator chips featuring "Online"
and "Offline" statuses, each with a toggleable checkbox to change the status.

Online

Offline

    
    
    <div class="flex gap-2">
    <div class="rounded-md flex items-center bg-green-100 py-0.5 pr-2.5 pl-1.5 border border-transparent text-sm text-green-800 transition-all shadow-sm">
      <div class="inline-flex items-center mr-2">
        <label class="flex items-center cursor-pointer relative">
          <input type="checkbox" class="peer h-5 w-5 cursor-pointer transition-all appearance-none rounded border border-green-300 checked:bg-green-600 checked:border-green-600" id="check4" />
          <span class="absolute text-white opacity-0 peer-checked:opacity-100 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="1">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
            </svg>
          </span>
        </label>
      </div>
     
      Online 
    </div>
     
    <div class="rounded-md flex items-center bg-red-100 py-0.5 pr-2.5 pl-1.5 border border-transparent text-sm text-red-800 transition-all shadow-sm">
      <div class="inline-flex items-center mr-2">
        <label class="flex items-center cursor-pointer relative">
          <input type="checkbox" class="peer h-5 w-5 cursor-pointer transition-all appearance-none rounded border border-red-300 checked:bg-red-600 checked:border-red-600" id="check5" />
          <span class="absolute text-white opacity-0 peer-checked:opacity-100 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="1">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
            </svg>
          </span>
        </label>
      </div>
     
      Offline 
    </div>
    </div>

* * *

## Explore More Tailwind CSS Examples

Check out more chip components examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks).

* * *

## Similar Components

Similar components to the chip include: **[badges](https://www.material-
tailwind.com/docs/html/badge), tags, pills, [buttons](https://www.material-
tailwind.com/docs/html/button), [tooltips](https://www.material-
tailwind.com/docs/html/tooltip)**.

* * *

  

## Chip Components Best Practices for Developers  

• Chips should have concise and descriptive labels that clearly convey their
purpose or the information they represent.  
• Keep a consistent look and feel for chips across your application to
maintain a cohesive user interface.  
• For chips that perform actions (e.g., deletable or selectable chips), make
it clear that they are interactive.  
• Ensure that chips are large enough to be easily tapped on touch devices,
following recommended touch target sizes.  
• Avoid overwhelming users with too many chips at once.



