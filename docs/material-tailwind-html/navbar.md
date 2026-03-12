### Navbar


Use our responsive Tailwind CSS navbar for your website. It is a navigation
tool, that helps users to easily access different sections or pages of a
website or application.

The navbar is usually located at the top of a webpage or along the side and it
can be static (remains in the same position regardless of page scrolling), or
dynamic (changes in response to user interactions). You can add links, icons,
links with icons, search bars, and brand text.

See below our simple navbar example that you can use in your Tailwind CSS
project.

  

## Navbar Examples:

## Simple Navbar with Icons

Use this simple navbar example with navigational links and buttons that get
the user's attention to perform specific actions, like "Log in".

Material Tailwind

  * Pages
  * Account
  * Blocks
  * Docs

    
    
    <nav class="block w-full max-w-screen-lg px-4 py-2 mx-auto bg-white shadow-md rounded-md lg:px-8 lg:py-3 mt-10">
      <div class="container flex flex-wrap items-center justify-between mx-auto text-slate-800">
        <a href="#" class="mr-4 block cursor-pointer py-1.5 text-base text-slate-800 font-semibold">
          Material Tailwind
        </a>
     
        <div class="hidden lg:block">
          <ul class="flex flex-col gap-2 mt-2 mb-4 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 0 0 2.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 0 0-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75 2.25 2.25 0 0 0-.1-.664m-5.8 0A2.251 2.251 0 0 1 13.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25ZM6.75 12h.008v.008H6.75V12Zm0 3h.008v.008H6.75V15Zm0 3h.008v.008H6.75V18Z" />
              </svg>
     
              <a href="#" class="flex items-center">
                Pages
              </a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
              </svg>
     
              <a href="#" class="flex items-center">
                Account
              </a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 7.125C2.25 6.504 2.754 6 3.375 6h6c.621 0 1.125.504 1.125 1.125v3.75c0 .621-.504 1.125-1.125 1.125h-6a1.125 1.125 0 0 1-1.125-1.125v-3.75ZM14.25 8.625c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v8.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 0 1-1.125-1.125v-8.25ZM3.75 16.125c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 0 1-1.125-1.125v-2.25Z" />
              </svg>
     
              <a href="#" class="flex items-center">
                Blocks
              </a>
            </li>
            <li
            class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.438 60.438 0 0 0-.491 6.347A48.62 48.62 0 0 1 12 20.904a48.62 48.62 0 0 1 8.232-4.41 60.46 60.46 0 0 0-.491-6.347m-15.482 0a50.636 50.636 0 0 0-2.658-.813A59.906 59.906 0 0 1 12 3.493a59.903 59.903 0 0 1 10.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0 1 12 13.489a50.702 50.702 0 0 1 7.74-3.342M6.75 15a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm0 0v-3.675A55.378 55.378 0 0 1 12 8.443m-7.007 11.55A5.981 5.981 0 0 0 6.75 15.75v-1.5" />
              </svg>
     
              <a href="#" class="flex items-center">
                Docs
              </a>
            </li>
          </ul>
        </div>
        <button class="relative ml-auto h-6 max-h-[40px] w-6 max-w-[40px] select-none rounded-lg text-center align-middle text-xs font-medium uppercase text-inherit transition-all hover:bg-transparent focus:bg-transparent active:bg-transparent disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none lg:hidden" type="button">
          <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </span>
        </button>
      </div>
    </nav>

* * *

## Sticky Navbar

This component example presents a cleaner design navbar styled with `sticky
top-0`, making it stick to the top of the viewport as the page scrolls down.
Users can easily navigate through the website while engaging with the content,
and the sticky navbar makes sure that navigation options are always within
reach.

Material Tailwind

  * Pages
  * Account
  * Blocks
  * Docs

![nature](https://images.unsplash.com/photo-1485470733090-0aae1788d5af?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2717&q=80)

## What is Material Tailwind

Can you help me out? you will get a lot of free exposure doing this can my
website be in english?. There is too much white space do less with more, so
that will be a conversation piece can you rework to make the pizza look more
delicious other agencies charge much lesser can you make the blue bluer?. I
think we need to start from scratch can my website be in english?, yet make it
sexy i'll pay you in a week we don't need to pay upfront i hope you understand
can you make it stand out more?. Make the font bigger can you help me out? you
will get a lot of free exposure doing this that's going to be a chunk of
change other agencies charge much lesser. Are you busy this weekend? I have a
new project with a tight deadline that's going to be a chunk of change. There
are more projects lined up charge extra the next time.

    
    
    <nav class="block w-full max-w-screen-lg px-4 py-2 mx-auto bg-white bg-opacity-90 sticky top-3 shadow lg:px-8 lg:py-3 backdrop-blur-lg backdrop-saturate-150 z-[9999]">
      <div class="container flex flex-wrap items-center justify-between mx-auto text-slate-800">
        <a href="#"
          class="mr-4 block cursor-pointer py-1.5 text-base text-slate-800 font-semibold">
          Material Tailwind
        </a>
        <div class="hidden lg:block">
          <ul class="flex flex-col gap-2 mt-2 mb-4 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <a href="#" class="flex items-center">Pages</a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <a href="#" class="flex items-center">Account</a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <a href="#" class="flex items-center">Blocks</a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <a href="#" class="flex items-center">Docs</a>
            </li>
          </ul>
        </div>
        <button
          class="relative ml-auto h-6 max-h-[40px] w-6 max-w-[40px] select-none rounded-lg text-center align-middle text-xs font-medium uppercase text-inherit transition-all hover:bg-transparent focus:bg-transparent active:bg-transparent disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none lg:hidden"
          type="button">
          <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </span>
        </button>
      </div>
    </nav>

* * *

## Navbar With Search

This navbar component example includes an interactive search input field and a
corresponding search button, alowing users to search content directly from the
navbar. This feature helps users to quickly access information without
navigating away from the current view.

Material Tailwind

  * Pages
  * Account
  * Blocks
  * Docs

Search

    
    
    <nav class="block w-full max-w-screen-lg px-4 py-2 mx-auto bg-white shadow-md rounded-md lg:px-8 lg:py-3 mt-10">
      <div class="container flex flex-wrap items-center justify-between mx-auto text-slate-800">
        <a href="#" class="mr-4 block cursor-pointer py-1.5 text-base text-slate-800 font-semibold">
          Material Tailwind
        </a>
     
        <div class="hidden lg:block">
          <ul class="flex flex-col gap-2 mt-2 mb-4 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 0 0 2.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 0 0-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75 2.25 2.25 0 0 0-.1-.664m-5.8 0A2.251 2.251 0 0 1 13.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25ZM6.75 12h.008v.008H6.75V12Zm0 3h.008v.008H6.75V15Zm0 3h.008v.008H6.75V18Z" />
              </svg>
     
              <a href="#" class="flex items-center">
                Pages
              </a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
              </svg>
     
              <a href="#" class="flex items-center">
                Account
              </a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 7.125C2.25 6.504 2.754 6 3.375 6h6c.621 0 1.125.504 1.125 1.125v3.75c0 .621-.504 1.125-1.125 1.125h-6a1.125 1.125 0 0 1-1.125-1.125v-3.75ZM14.25 8.625c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v8.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 0 1-1.125-1.125v-8.25ZM3.75 16.125c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 0 1-1.125-1.125v-2.25Z" />
              </svg>
     
              <a href="#" class="flex items-center">
                Blocks
              </a>
            </li>
            <li
            class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6 text-slate-500">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.438 60.438 0 0 0-.491 6.347A48.62 48.62 0 0 1 12 20.904a48.62 48.62 0 0 1 8.232-4.41 60.46 60.46 0 0 0-.491-6.347m-15.482 0a50.636 50.636 0 0 0-2.658-.813A59.906 59.906 0 0 1 12 3.493a59.903 59.903 0 0 1 10.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0 1 12 13.489a50.702 50.702 0 0 1 7.74-3.342M6.75 15a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm0 0v-3.675A55.378 55.378 0 0 1 12 8.443m-7.007 11.55A5.981 5.981 0 0 0 6.75 15.75v-1.5" />
              </svg>
     
              <a href="#" class="flex items-center">
                Docs
              </a>
            </li>
          </ul>
        </div>
        <div class="items-center hidden gap-x-2 lg:flex">
          <div class="w-full max-w-sm min-w-[200px]">
            <div class="relative">            
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="absolute w-5 h-5 top-2.5 left-2.5 text-slate-600">
                <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
              </svg>
              <input type="text" class="w-full pl-10 pr-3 py-2 bg-transparent placeholder:text-slate-400 text-slate-600 text-sm border border-slate-200 rounded-md transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
            </div>
          </div>
          <button class="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
            Search
          </button>
        </div>
        <button class="relative ml-auto h-6 max-h-[40px] w-6 max-w-[40px] select-none rounded-lg text-center align-middle text-xs font-medium uppercase text-inherit transition-all hover:bg-transparent focus:bg-transparent active:bg-transparent disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none lg:hidden" type="button">
          <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </span>
        </button>
      </div>
    </nav>

  

The search input is styled with Tailwind CSS classes that focus on
transitions, borders, placeholders, and responsiveness. A unique aspect is the
use of a custom label and SVG icon to visually indicate the search area, along
with transition effects for focus states that change border and text color to
guide user interaction.

* * *

## Dark Navbar

In this example, the navbar uses a gradient background styled with Tailwind
CSS (`bg-slate-900`), creating a dark mode design.

CryptoExchange

  * Markets
  * Wallet
  * Exchange
  * Support

    
    
    <nav class="block w-full max-w-screen-lg px-4 py-2 mx-auto text-white bg-slate-900 shadow-md rounded-md lg:px-8 lg:py-3 mt-10">
      <div class="container flex flex-wrap items-center justify-between mx-auto text-gray-100">
        <a href="#"
          class="mr-4 block cursor-pointer py-1.5 text-base text-gray-200 font-semibold">
          CryptoExchange
        </a>
        <div class="hidden lg:block">
          <ul class="flex flex-col gap-2 mt-2 mb-4 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
            <li class="flex items-center p-1 text-sm gap-x-2 text-gray-200">
              <a href="#" class="flex items-center">
                Markets
              </a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-gray-200">
              <a href="#" class="flex items-center">
                Wallet
              </a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-gray-200">
              <a href="#" class="flex items-center">
                Exchange
              </a>
            </li>
            <li class="flex items-center p-1 text-sm gap-x-2 text-gray-200">
              <a href="#" class="flex items-center">
                Support
              </a>
            </li>
          </ul>
        </div>
        <button
          class="relative ml-auto h-6 max-h-[40px] w-6 max-w-[40px] select-none rounded-lg text-center align-middle text-xs font-medium uppercase text-inherit transition-all hover:bg-transparent focus:bg-transparent active:bg-transparent disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none lg:hidden"
          type="button">
          <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </span>
        </button>
      </div>
    </nav>

  

The navbar incorporates a search input field with a unique label animation.
The label ("Type here...") is styled to appear within the search field when
it's not focused and moves above the search field when it is focused,
providing a clear, interactive cue for users.

* * *

## Simple Navbar

Use this minimalist navbar that can be used across a wide range of websites
and web applications where navigation clarity is important.

Material Tailwind

  * Pages
  * Account
  * Blocks
  * Docs

    
    
    <nav class="block w-full max-w-screen-lg px-4 py-2 mx-auto text-white bg-white shadow-md rounded-md lg:px-8 lg:py-3 mt-10">
      <div class="container flex flex-wrap items-center justify-between mx-auto text-slate-800">
        <a href="#"
          class="mr-4 block cursor-pointer py-1.5 text-base text-slate-800 font-semibold">
          Material Tailwind
        </a>
        <div class="hidden lg:block">
          <ul class="flex flex-col gap-2 mt-2 mb-4 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
            <li
              class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
     
     
              <a href="#" class="flex items-center">
                Pages
              </a>
            </li>
            <li
              class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
     
     
              <a href="#" class="flex items-center">
                Account
              </a>
            </li>
            <li
              class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
     
     
              <a href="#" class="flex items-center">
                Blocks
              </a>
            </li>
            <li
              class="flex items-center p-1 text-sm gap-x-2 text-slate-600">
     
     
              <a href="#" class="flex items-center">
                Docs
              </a>
            </li>
          </ul>
        </div>
        <button
          class="relative ml-auto h-6 max-h-[40px] w-6 max-w-[40px] select-none rounded-lg text-center align-middle text-xs font-medium uppercase text-inherit transition-all hover:bg-transparent focus:bg-transparent active:bg-transparent disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none lg:hidden"
          type="button">
          <span class="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </span>
        </button>
      </div>
    </nav>

* * *

## Required Scripts

The navbar component needs a required script file to work, you just need to
add the below script file to the bottom of your html file.

    
    
    <!-- from node_modules -->
    <script src="node_modules/@material-tailwind/html/scripts/collapse.js"></script>
    <!-- from cdn -->
    <script src="https://unpkg.com/@material-tailwind/html@latest/scripts/collapse.js"></script>

  

* * *

## Explore More Tailwind CSS Examples

Check out more navigation bar examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks):

• [Hero Blocks](https://www.material-tailwind.com/blocks/hero-sections)  
• [Navbar Blocks](https://www.material-tailwind.com/blocks/navbars)  

* * *

## Navbar Best Practices for Developers

• Avoid cluttering it with too many links and use clear, descriptive labels
for navigation links.  
• Maintain consistency in the navbar's design across different pages of the
website.  
• Use size, color, and placement to establish a visual hierarchy in your
navbar.  
• Consider using a sticky or fixed navbar that remains visible as the user
scrolls down the page.  
• For websites with extensive content or products, include a search bar within
the navbar.



