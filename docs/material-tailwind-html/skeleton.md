### Skeleton


The skeleton component is a minimal version of a component that can be used as
an alternative loading indicator to the spinner by imitating the content that
will be loaded such as text, images, or video.

The skeleton can help developers visualize the layout and functionality of a
system before implementing more intricate features.

See below our Skeleton examples styled with Tailwind CSS that you can use in
your HTML projects.

  

## Skeleton Examples:

## Simple Skeleton

Use this versatile skeleton example to provide a visual indication of where
content will appear on your webpage.

    
    
    <div class="max-w-full animate-pulse">
      <div
        class="block w-56 h-3 mb-4 font-sans text-5xl antialiased font-semibold leading-tight tracking-normal bg-gray-300 rounded-full text-inherit">
        &nbsp;
      </div>
      <div
        class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
        &nbsp;
      </div>
      <div
        class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
        &nbsp;
      </div>
      <div
        class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
        &nbsp;
      </div>
      <div
        class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
        &nbsp;
      </div>
    </div>

* * *

## Image placeholder Skeleton

Instead of just placeholder text, this example includes an SVG icon
representing an image or an action. This adds a visual cue to users about the
type of content that might be expected in that section.

    
    
    <div class="flex flex-wrap items-center gap-8 animate-pulse">
      <div class="grid bg-gray-300 rounded-lg h-36 w-36 place-items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
          class="w-12 h-12 text-gray-500">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z">
          </path>
        </svg>
      </div>
      <div class="w-max">
        <div
          class="block w-56 h-3 mb-4 font-sans text-5xl antialiased font-semibold leading-tight tracking-normal bg-gray-300 rounded-full text-inherit">
          &nbsp;
        </div>
        <div
          class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
          &nbsp;
        </div>
        <div
          class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
          &nbsp;
        </div>
        <div
          class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
          &nbsp;
        </div>
        <div
          class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
          &nbsp;
        </div>
        <div
          class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
          &nbsp;
        </div>
        <div
          class="block h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit w-72">
          &nbsp;
        </div>
      </div>
    </div>

* * *

## Video placeholder Skeleton

Similar to the previous example, this skeleton includes an SVG icon
representing a video. The container is animated with a pulsating effect
(`animate-pulse` class), signifying that content is loading or being fetched.

    
    
    <div
      class="grid h-full max-h-[300px] min-h-[160px] w-full max-w-xs animate-pulse place-items-center rounded-lg bg-gray-300">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
        class="w-12 h-12 text-gray-500">
        <path stroke-linecap="round" stroke-linejoin="round"
          d="m15.75 10.5 4.72-4.72a.75.75 0 0 1 1.28.53v11.38a.75.75 0 0 1-1.28.53l-4.72-4.72M4.5 18.75h9a2.25 2.25 0 0 0 2.25-2.25v-9a2.25 2.25 0 0 0-2.25-2.25h-9A2.25 2.25 0 0 0 2.25 7.5v9a2.25 2.25 0 0 0 2.25 2.25Z">
        </path>
      </svg>
    </div>

* * *

## Card placeholder Skeleton

This example showcases a more complex skeleton, including an image
placeholder, text placeholder, and button placeholder. It can be used if you
want to prototype a blog card, for example.

    
    
    <div class="relative flex flex-col mt-6 text-gray-700 bg-white shadow-md bg-clip-border rounded-xl w-96 animate-pulse">
      <div
        class="relative grid h-56 mx-4 mt-4 overflow-hidden text-gray-700 bg-gray-300 bg-clip-border rounded-xl place-items-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
          class="w-12 h-12 text-gray-500">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z">
          </path>
        </svg>
      </div>
      <div class="p-6">
        <div
          class="block w-56 h-3 mb-4 font-sans text-5xl antialiased font-semibold leading-tight tracking-normal bg-gray-300 rounded-full text-inherit">
          &nbsp;
        </div>
        <div
          class="block w-full h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit">
          &nbsp;
        </div>
        <div
          class="block w-full h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit">
          &nbsp;
        </div>
        <div
          class="block w-full h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit">
          &nbsp;
        </div>
        <div
          class="block w-full h-2 mb-2 font-sans text-base antialiased font-light leading-relaxed bg-gray-300 rounded-full text-inherit">
          &nbsp;
        </div>
      </div>
      <div class="p-6 pt-0">
        <button disabled="" tabindex="-1"
          class="align-middle select-none font-sans font-bold text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 px-6 rounded-lg text-white shadow-gray-900/10 hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none h-8 w-20 bg-gray-300 shadow-none hover:shadow-none"
          type="button">
          &nbsp;
        </button>
      </div>
    </div>

* * *

## Explore More Tailwind CSS Examples

Check out more skeleton examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks).

* * *

## Skeleton Best Practices for Developers

• Only implement skeleton screens for content that takes a noticeable time to
load.  
• Keep the design and layout of skeleton screens consistent with the final
content.  
• Skeleton screens should be simple and easy to understand.  
• Make sure that the duration of the skeleton animation matches the expected
loading time of the content.



