### Progress Bar


Our Tailwind CSS progress component can be used to show a user how far along
he is in a process. The progress can be determinate or indeterminate. Use the
Progress Bar to show an ongoing process that takes a noticeable time to
finish.

Below we are presenting our examples of progress components that you can use
in your Tailwind CSS project. They come in different styles so you can adapt
them easily to your needs.

  

## Progress Bar Examples:

## Simple Progress Bar

Use this example of a versatile dark gray progress bar with a rounded design
and responsive sizing to indicate progress.

    
    
     <div className="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
          <div className="flex h-full w-1/2 items-center justify-center overflow-hidden break-all rounded-full bg-gray-900 text-white"></div>
        </div>

* * *

## Progress Bar Variants

Below there are 2 different variants of progress bar that you can use: simple
and with gradient.

    
    
       <div class="flex flex-col w-full gap-4">
          <div class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
            <div class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full"></div>
          </div>
          <div class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
            <div class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all rounded-full bg-gradient-to-tr from-gray-900 to-gray-800"></div>
          </div>
        </div>

* * *

## Progress Bar Sizes

The Progress component comes with 3 different sizes that you can change.

    
    
      <div class="flex flex-col w-full gap-4">
      <div
        class="flex-start flex h-1.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/4 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/3 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-3.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
        </div>
      </div>
    </div>

* * *

## Progress Bar Colors

See below how you can implement varying fill colors to represent different
progress states or categories.

    
    
      <div class="flex flex-col w-full gap-4">
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-blue-500 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-red-500 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-green-500 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-black break-all rounded-full bg-amber-500">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-teal-500 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-indigo-500 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-purple-500 rounded-full">
        </div>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-pink-500 rounded-full">
        </div>
      </div>
    </div>

* * *

## Progress Bar with Label

This progress bar example includes text within the filled portion, explicitly
stating "50% Completed." This addition improves user accessibility and
understanding by directly communicating the progress level.

50% Completed

    
    
      <div class="flex w-full h-4 overflow-hidden font-sans text-xs font-medium rounded-full flex-start bg-blue-gray-50">
          <div class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
            50% Completed
          </div>
        </div>  

* * *

## Progress Bar Sizes Label

This example showcases a set of three progress bars, each with a different
completion percentage and size, organized vertically within a flex container.

25% Small

50% Medium

75% Large

    
    
    <div class="flex flex-col w-full gap-4">
      <div
        class="flex-start flex h-3.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/4 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
          25% Small
        </div>
      </div>
      <div
        class="flex w-full h-4 overflow-hidden font-sans text-xs font-medium rounded-full flex-start bg-blue-gray-50">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
          50% Medium
        </div>
      </div>
      <div
        class="flex w-full h-5 overflow-hidden font-sans text-xs font-medium rounded-full flex-start bg-blue-gray-50">
        <div
          class="flex items-center justify-center w-3/4 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
          75% Large
        </div>
      </div>
    </div>

* * *

## Progress Bar Label Outside

Use the example below to add the label outside the progress bar.

###### Completed

###### 50%

    
    
    <div class="w-full">
      <div class="flex items-center justify-between gap-4 mb-2">
        <h6
          class="block font-sans text-base antialiased font-semibold leading-relaxed tracking-normal text-blue-gray-900">
          Completed
        </h6>
        <h6
          class="block font-sans text-base antialiased font-semibold leading-relaxed tracking-normal text-blue-gray-900">
          50%
        </h6>
      </div>
      <div
        class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
        <div
          class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full">
        </div>
      </div>
    </div>

* * *

## Progress Bar Custom Styles

Use the example below to customize the progress bar.

    
    
     <div class="flex-start flex h-3.5 w-full overflow-hidden rounded-full border border-gray-900/10 bg-gray-900/5 p-1 font-sans text-xs font-medium">
          <div class="flex items-center justify-center w-1/2 h-full overflow-hidden text-white break-all bg-gray-900 rounded-full"></div>
        </div>

* * *

## Explore More Tailwind CSS Examples

Check out more progress bar examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks).



