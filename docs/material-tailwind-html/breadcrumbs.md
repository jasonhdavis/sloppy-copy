### Breadcrumbs


Use our Tailwind CSS breadcrumbs component to simply create beautiful
breadcrumbs for your pages with Material Tailwind.

Breadcrumbs are website links that allow users to track where they are on a
website and how far they are from the homepage. They are highly important
elements for your search engine optimisation (SEO) and user experience.

See below our versatile breadcrumbs component example that you can use in your
Tailwind CSS project.

  

## Breadcrumbs Examples:

## Default Breadcrumbs

Use this example of responsive breadcrumbs styled with a background opacity
for visual distinction and interactive elements that change color upon hover,
improving user experience by guiding them through the website's pages.

  1. Docs/
  2. Components/
  3. Breadcrumbs

    
    
    <nav aria-label="breadcrumb" class="w-max">
      <ol class="flex w-full flex-wrap items-center rounded-md bg-slate-50 px-4 py-2">
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Docs</a>
          <span class="pointer-events-none mx-2 text-slate-800">
            /
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Components</a>
          <span class="pointer-events-none mx-2 text-slate-800">
            /
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Breadcrumbs</a>
        </li>
      </ol>
    </nav>

* * *

## Breadcrumbs with icon

You can add any type of icon for the breadcrumbs component as easily as using
icons in html.

  1. /
  2. Components/
  3. Breadcrumbs

    
    
    <nav aria-label="breadcrumb" class="w-max">
      <ol class="flex w-full flex-wrap items-center rounded-md bg-slate-50 px-4 py-2">
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path>
            </svg>
          </a>
          <span class="pointer-events-none mx-2 text-slate-800">
            /
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Components</a>
          <span class="pointer-events-none mx-2 text-slate-800">
            /
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Breadcrumbs</a>
        </li>
      </ol>
    </nav>

* * *

## Block Level Breadcrumbs

Breadcrumbs can be a block-level component that gets all the available space
in a row. You can display breadcrumbs as a block-level element using the
`w-full` class.

  1. Docs/
  2. Components/
  3. Breadcrumbs

    
    
    <nav aria-label="breadcrumb" class="w-full">
      <ol class="flex w-full flex-wrap items-center rounded-md bg-slate-50 px-4 py-2">
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Docs</a>
          <span class="pointer-events-none mx-2 text-slate-800">
            /
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Components</a>
          <span class="pointer-events-none mx-2 text-slate-800">
            /
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Breadcrumbs</a>
        </li>
      </ol>
    </nav>

* * *

## Custom Breadcrumbs Separator

You can modify the Breadcrumbs separators, check out the example below:

  1. Docs-
  2. Components-
  3. Breadcrumbs

    
    
    <nav aria-label="breadcrumb" class="w-max">
      <ol class="flex w-full flex-wrap items-center rounded-md bg-slate-50 px-4 py-2">
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Docs</a>
          <span class="pointer-events-none mx-2 text-slate-800">
            -
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Components</a>
          <span class="pointer-events-none mx-2 text-slate-800">
            -
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-slate-500 transition-colors duration-300 hover:text-slate-800">
          <a href="#">Breadcrumbs</a>
        </li>
      </ol>
    </nav>

* * *

## Breadcrumbs Custom Styles

You can add custom styles to your Breadcrumbs, check out the example below:

  1. Docs-
  2. Components-
  3. Breadcrumbs

    
    
    <nav aria-label="breadcrumb" class="w-max">
      <ol class="flex w-full flex-wrap items-center rounded-full border border-white bg-slate-800 p-1">
        <li class="flex cursor-pointer items-center text-sm text-white transition-colors duration-300">
          <a
            href="#"
            class="px-3 py-1 hover:underline"
          >
            Docs
          </a>
          <span class="pointer-events-none mx-2 text-white">
            -
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-white transition-colors duration-300">
          <a
            href="#"
            class="px-3 py-1 hover:underline"
          >
            Components
          </a>
          <span class="pointer-events-none mx-2 text-white">
            -
          </span>
        </li>
        <li class="flex cursor-pointer items-center text-sm text-white transition-colors duration-300">
          <a
            href="#"
            class="px-3 py-1 hover:underline"
          >
            Breadcrumbs
          </a>
        </li>
      </ol>
    </nav>

* * *

## Explore More Tailwind CSS Examples

Looking for more breadcrumbs examples? Check out our **[Ecommerce
Sections](https://www.material-tailwind.com/blocks/ecommerce-sections)** from
[Material Tailwind Blocks](https://www.material-tailwind.com/blocks).



