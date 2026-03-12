### Button Group


The Tailwind CSS Button groups are used to organize related buttons or button-
like elements together in a visually cohesive and functional manner.

For users, it’s easier to find related actions in one place. Button groups can
improve usability by reducing the time and effort needed to locate and
interact with multiple related functions.

They are especially useful for navigation menus, toolbars, filters, and other
situations where multiple buttons are presented together.

We created a series of button group examples to help you build easier your
application or website. All these examples are styled with Tailwind CSS and
based on Material Design.

## Button Group Examples:

## Default Button Group

This component example showcases a responsive button group with detailed
control over appearance and layout. The use of utility classes makes it easy
to customize each aspect of the button group's design.

  

OneTwoThree

    
    
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-slate-800 py-2 px-4 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>

  

The first and last buttons in the group have `rounded-r-none` and `rounded-l-
none`, respectively. This removes the rounded corners and right border of the
first button and the left rounded corner of the last button, creating a great
group appearance.

* * *

## Button Group Variants

Get inspired by this series of button groups, each with different styling,
arranged in a vertical stack.

OneTwoThree

OneTwoThree

OneTwoThree

OneTwoThree

    
    
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-slate-800 py-2 px-4 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-gradient-to-tr from-slate-800 to-slate-700 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-gradient-to-tr from-slate-800 to-slate-700 py-2 px-4 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-gradient-to-tr from-slate-800 to-slate-700 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>
     
     
    <div class="row flex">
      <button class="rounded-md rounded-r-none border border-r-0 border-slate-300 py-2 px-4 text-center text-sm transition-all shadow-sm hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 hover:border-slate-800 focus:text-white focus:bg-slate-800 focus:border-slate-800 active:border-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        One
      </button>
      <button class="rounded-md rounded-r-none rounded-l-none border border-slate-300 py-2 px-4 text-center text-sm transition-all shadow-sm hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 hover:border-slate-800 focus:text-white focus:bg-slate-800 focus:border-slate-800 active:border-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Two
      </button>
      <button class="rounded-md rounded-l-none border border-l-0 border-slate-300 py-2 px-4 text-center text-sm transition-all shadow-sm hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 hover:border-slate-800 focus:text-white focus:bg-slate-800 focus:border-slate-800 active:border-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none py-2 px-4 text-center text-sm transition-all hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 focus:text-white focus:bg-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none border-l border-r border-slate-300 py-2 px-4 text-center text-sm transition-all hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 hover:border-slate-800 focus:text-white focus:bg-slate-800 focus:border-slate-800 active:border-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none py-2 px-4 text-center text-sm transition-all hover:shadow-lg text-slate-600 hover:text-white hover:bg-slate-800 focus:text-white focus:bg-slate-800 active:text-white active:bg-slate-800 disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>

  

The first component variant features a classic and straightforward design with
solid gray backgrounds (`bg-slate-800`) and white text.  
The second variant stands out with a gradient background (`bg-gradient-to-tr
from-slate-800 to-slate-700`), transitioning from dark gray to slightly
lighter gray.  
The third variant adopts a more minimalistic approach, featuring a border
(`border border-slate-300`) around each button and slate text.  
The fourth button group is the most simplistic, with no explicit background
color but a subtle hover background effect (`hover:bg-slate-800`).  

Using Tailwind CSS's utility classes and Material Tailwind's design as a
starting point, you can create diverse designs while maintaining a cohesive
user interface.

* * *

## Button Group Sizes

This button group component example shows you how to create responsive and
scalable UI components with varied dimensions and emphasis.

OneTwoThree

OneTwoThree

OneTwoThree

OneTwoThree

OneTwoThree

    
    
    <div class="row flex">
      <button class="rounded-md rounded-r-none bg-slate-800 py-1 px-2.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        One
      </button>
      <button class="rounded-none bg-slate-800 py-1 px-2.5 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Two
      </button>
      <button class="rounded-md rounded-l-none bg-slate-800 py-1 px-2.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button class="rounded-md rounded-r-none bg-slate-800 py-1.5 px-3 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        One
      </button>
      <button class="rounded-none bg-slate-800 py-1.5 px-3 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Two
      </button>
      <button class="rounded-md rounded-l-none bg-slate-800 py-1.5 px-3 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button class="rounded-md rounded-r-none bg-slate-800 py-2 px-4 border border-transparent border-r-0 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        One
      </button>
      <button class="rounded-none bg-slate-800 py-2 px-4 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Two
      </button>
      <button class="rounded-md rounded-l-none bg-slate-800 py-2 px-4 border border-transparent border-l-0 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button class="rounded-md rounded-r-none bg-slate-800 py-2.5 px-5 border border-transparent text-center text-base text-white transition-all shadow-sm hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        One
      </button>
      <button class="rounded-none bg-slate-800 py-2.5 px-5 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Two
      </button>
      <button class="rounded-md rounded-l-none bg-slate-800 py-2.5 px-5 border border-transparent text-center text-base text-white transition-all shadow-sm hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button class="rounded-lg rounded-r-none bg-slate-800 py-3.5 px-6 border border-transparent text-center text-base text-white transition-all shadow hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        One
      </button>
      <button class="rounded-none bg-slate-800 py-3.5 px-6 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Two
      </button>
      <button class="rounded-lg rounded-l-none bg-slate-800 py-3.5 px-6 border border-transparent text-center text-base text-white transition-all shadow hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
        Three
      </button>
    </div>

  

In this example: • The buttons in the first group are the smallest, with
`text-xs` for font size and `py-2 px-4` for padding. This makes the buttons
more compact.  
• The buttons in the second group are slightly larger than the first group,
with the same `text-xs` font size but increased padding `py-3 px-6` making the
buttons more prominent.  
• The third group features the largest buttons, with `text-sm` for slightly
larger font size and `py-3.5 px-7` for padding.

* * *

## Button Group Colors

This example showcases four distinct button groups, each differentiated by
color to represent various actions or states within an application or website.

OneTwoThree

OneTwoThree

OneTwoThree

OneTwoThree

    
    
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-blue-600 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-blue-700 focus:shadow-none active:bg-blue-700 hover:bg-blue-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-blue-600 py-2 px-4 border-l border-r border-blue-400 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-blue-700 focus:shadow-none active:bg-blue-700 hover:bg-blue-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-blue-600 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-blue-700 focus:shadow-none active:bg-blue-700 hover:bg-blue-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-red-600 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-red-700 focus:shadow-none active:bg-red-700 hover:bg-red-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-red-600 py-2 px-4 border-l border-r border-red-400 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-red-700 focus:shadow-none active:bg-red-700 hover:bg-red-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-red-600 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-red-700 focus:shadow-none active:bg-red-700 hover:bg-red-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-green-600 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-green-700 focus:shadow-none active:bg-green-700 hover:bg-green-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-green-600 py-2 px-4 border-l border-r border-green-400 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-green-700 focus:shadow-none active:bg-green-700 hover:bg-green-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-green-600 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-green-700 focus:shadow-none active:bg-green-700 hover:bg-green-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>
     
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-amber-600 py-2 px-4 border border-transparent text-center text-sm text-slate-800 transition-all shadow-md hover:shadow-lg focus:bg-amber-700 focus:shadow-none active:bg-amber-700 hover:bg-amber-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-amber-600 py-2 px-4 border-l border-r border-amber-400 text-center text-sm text-slate-800 transition-all shadow-md hover:shadow-lg focus:bg-amber-700 focus:shadow-none active:bg-amber-700 hover:bg-amber-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-amber-600 py-2 px-4 border border-transparent text-center text-sm text-slate-800 transition-all shadow-md hover:shadow-lg focus:bg-amber-700 focus:shadow-none active:bg-amber-700 hover:bg-amber-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>

* * *

## Block Level Button Group

This example illustrates a single row of three buttons optimized for a full-
width layout within a container that allows for horizontal scrolling on
smaller screens and becomes fully visible on larger screens.

OneTwoThree

    
    
    <div class="row flex w-full">
      <button
        class="rounded-md w-full rounded-r-none bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none w-full bg-slate-800 py-2 px-4 border-l border-r border-slate-700 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md w-full rounded-l-none bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>

* * *

## Button Group Custom Style

The button group is encapsulated within a grid container that ensures the
buttons are centrally placed. The shadow (`shadow-md shadow-gray-900/10`) adds
depth to the buttons, making them stand out against the light blue background.

OneTwoThree

    
    
    <div class="row flex">
      <button
        class="rounded-md rounded-r-none bg-slate-800 py-2 px-4 border-2 border-slate-500 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        One
      </button>
      <button
        class="rounded-none bg-slate-800 py-2 px-4 border-2 border-l-0 border-r-0 border-slate-500 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Two
      </button>
      <button
        class="rounded-md rounded-l-none bg-slate-800 py-2 px-4 border-2 border-slate-500 text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        type="button"
      >
        Three
      </button>
    </div>

* * *

## Explore More Tailwind CSS Examples

Check out more button group examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks).



