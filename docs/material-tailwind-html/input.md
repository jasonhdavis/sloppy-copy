### Input


Easily create inputs with different statuses and sizes using our components
based on Tailwind CSS.

Input fields are an essential user interface design element, providing users
with the means to enter non-standardized responses. Input components are
critical for gathering user input in a structured format, facilitating
interaction between the user and the application.

They are used extensively in forms for registrations, logins, searches, and
data entry tasks across various platforms. The design and functionality of
input components can significantly impact the usability and user experience of
an application, making it important for developers and designers to choose the
appropriate type of input for the data they wish to collect from users.

See below Material Tailwind's input component examples.

  


## Simple Text Input

Use our input example to get started easily. It is perfect for forms requiring
text input, such as user registration, login forms, or any form where users
need to input a username.

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here...">
    </div>

* * *

## Input Variants

Learn how to create 2 distinct styled input components using Material Tailwind
framework. Each input style serves different aesthetic preferences and
usability considerations, from the minimalist Static and Standard inputs to
the more visually distinct Outlined input.

Type Here...

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>
     
    <div class="w-full max-w-sm min-w-[200px]">
      <div class="relative">
        <input
          class="peer w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
        />
        <label class="absolute cursor-text bg-white px-1 left-2.5 top-2.5 text-slate-400 text-sm transition-all transform origin-left peer-focus:-top-2 peer-focus:left-2.5 peer-focus:text-xs peer-focus:text-slate-400 peer-focus:scale-90">
          Type Here...
        </label>
      </div>
    </div>

* * *

## Input Sizes

Check out this coded snippet to see how you can implement inputs with
different sizes. The first input has a height of 34 px, the second one 38px
while the third example has a height of 46px, slightly taller, providing a
larger interaction area.

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-1.5 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>
     
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>
     
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-3 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>

* * *

## Input Colors

The 4 examples of input components showcased below are HTML snippets styled
with Tailwind CSS, each designed to highlight a different focus color theme:
Blue, Purple, Indigo, and Teal. They share a common structure and styling with
slight variations in color to differentiate them.

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-blue-500 hover:border-blue-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>
     
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-purple-500 hover:border-purple-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>
     
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-indigo-500 hover:border-indigo-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>
     
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-teal-500 hover:border-teal-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>

* * *

## Input Validations

These input examples styled with Tailwind CSS are structured to visually
communicate feedback to the user through color-coded cues. Each example
represents different states or feedback contexts for user interaction: an
error state (red-themed - `border-red-500, text-red-500`) and a success state
(green-themed - `border-green-500, text-green-500`).

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-red-400 text-red-700 text-sm border border-red-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-red-500 hover:border-red-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>
     
    <div class="w-full max-w-sm min-w-[200px]">
      <input class="w-full bg-transparent placeholder:text-green-400 text-green-700 text-sm border border-green-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-green-500 hover:border-green-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>

* * *

## Input With Icon

Use this example of input with icon element if you want to add a friendly
touch and make it more interactive.

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <div class="relative">            
        <input type="text" class="w-full pl-3 pr-10 py-2 bg-transparent placeholder:text-slate-400 text-slate-600 text-sm border border-slate-200 rounded-md transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
     
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="absolute w-5 h-5 top-2.5 right-2.5 text-slate-600">
          <path d="M4.5 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM14.25 8.625a3.375 3.375 0 1 1 6.75 0 3.375 3.375 0 0 1-6.75 0ZM1.5 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM17.25 19.128l-.001.144a2.25 2.25 0 0 1-.233.96 10.088 10.088 0 0 0 5.06-1.01.75.75 0 0 0 .42-.643 4.875 4.875 0 0 0-6.957-4.611 8.586 8.586 0 0 1 1.71 5.157v.003Z"></path>
        </svg>
      </div>
    </div>

* * *

## Input With Helper Text

Use this example of password input field designed with a focus on security and
user guidance. It is styled using Tailwind CSS and includes an accompanying
label and a hint message with an icon, aimed at enhancing user experience by
providing clear instructions for creating a strong password.

Use at least 8 characters, one uppercase, one lowercase and one number.

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <div class="relative">
        <input type="password" class="w-full pl-3 pr-3 py-2 bg-transparent placeholder:text-slate-400 text-slate-600 text-sm border border-slate-200 rounded-md transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Your password" />
        <p class="flex items-start mt-2 text-xs text-slate-400">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5 mr-1.5">
            <path fill-rule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12ZM12 8.25a.75.75 0 0 1 .75.75v3.75a.75.75 0 0 1-1.5 0V9a.75.75 0 0 1 .75-.75Zm0 8.25a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Z" clip-rule="evenodd" />
          </svg>
     
          Use at least 8 characters, one uppercase, one lowercase and one number.
        </p>    
      </div>
    </div>

* * *

## Input With Button

Use the example below for an input containing a button inside. It is useful
for forms where users can enter an email address and then take an action, such
as inviting a user to a platform or sending a notification.

Invite

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <div class="relative">
        <input type="email" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pl-3 pr-16 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Email Address" />
        <button
          class="absolute right-1 top-1 rounded bg-slate-800 py-1 px-2.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
          type="button"
        >
          Invite
        </button>
      </div>
    </div>

* * *

## Input with Label

Use this input example with placeholder text "Enter your text," guiding the
user to input their name. The label is positioned above the input field to
obtain clarity on what information is required.

Add Members

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <label class="block mb-2 text-sm text-slate-600">
          Add Members
      </label>
      <input class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>

* * *

## Input with Label and Icon Button

Try this text input field with a search icon button on the left. The second
variant includes an additional icon button on the right, allowing for more
interactive options.

Your Name

Your Name

    
    
    <div class="w-full max-w-sm min-w-[200px] relative mt-4">
      <label class="block mb-2 text-sm text-slate-600">
        Your Name
      </label>
     
      <div class="relative">
        <input type="email" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pr-3 pl-10 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Enter your text" />
        <button class="absolute left-1 top-1 rounded bg-slate-800 p-1.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
            <path fill-rule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>
    </div>
     
    <div class="w-full max-w-sm min-w-[200px] relative mt-4">
      <label class="block mb-2 text-sm text-slate-600">
        Your Name
      </label>
     
      <div class="relative">
        <input type="email" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pl-3 pr-10 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Enter your text" />
        <button class="absolute right-1 top-1 rounded bg-slate-800 p-1.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
            <path fill-rule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>
    </div>

* * *

## Input with Label and Text Button

Use this input example with a text button labeled "Search" positioned either
on the left or the right of the input field. This button can be clicked to
initiate a search.

Your Name

Search

Your Name

Search

    
    
    <div class="w-full max-w-sm min-w-[200px] relative mt-4">
      <label class="block mb-2 text-sm text-slate-600">
        Your Name
      </label>
     
      <div class="relative">
        <input type="email" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pr-3 pl-20 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Enter your text" />
        <button class="absolute left-1 top-1 rounded bg-slate-800 py-1 px-2.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
          Search
        </button>
      </div>
    </div>
     
    <div class="w-full max-w-sm min-w-[200px] relative mt-4">
      <label class="block mb-2 text-sm text-slate-600">
        Your Name
      </label>
     
      <div class="relative">
        <input type="email" class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pl-3 pr-20 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Enter your text" />
        <button class="absolute right-1 top-1 rounded bg-slate-800 py-1 px-2.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">
          Search
        </button>
      </div>
    </div>

* * *

## Input with Dropdown

This text input field includes a dropdown menu either on the left or right
side of the input. Use this Tailwind CSS component to allow users to select
from predefined options while entering text.

Your Name

Dropdown 1

Your Name

Dropdown 1

    
    
    <div class="w-full max-w-sm min-w-[200px] mt-4 ">
      <label class="block mb-1 text-sm text-slate-600">
        Your Name
      </label>
      <div class="relative mt-2">
          <div class="absolute top-2 left-0 flex items-center pl-3">
          <button id="dropdownButton" class="h-full text-sm flex justify-center items-center bg-transparent text-slate-700 focus:outline-none">
            Dropdown
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-4 w-4 ml-1">
              <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
            </svg>
          </button>
          <div class="h-6 border-l border-slate-200 ml-2"></div>
          <div id="dropdownMenu" class="min-w-[150px] overflow-hidden absolute left-0 w-full mt-10 hidden w-full bg-white border border-slate-200 rounded-md shadow-lg z-10">
            <ul id="dropdownOptions">
              <li class="px-4 py-2 text-slate-600 hover:bg-slate-50 text-sm cursor-pointer">Dropdown 1</li>
              <li class="px-4 py-2 text-slate-600 hover:bg-slate-50 text-sm cursor-pointer">Dropdown 2</li>
              <li class="px-4 py-2 text-slate-600 hover:bg-slate-50 text-sm cursor-pointer">Dropdown 3</li>
            </ul>
          </div>
        </div>
        <input
          type="text"
          class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pl-32 pr-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
          placeholder="Enter your text" />
      </div>   
    </div>
     
     
    <div class="w-full max-w-sm min-w-[200px] mt-4 relative">
      <label class="block mb-1 text-sm text-slate-600">
        Your Name
      </label>
     
      <div class="relative mt-2">
        <div class="absolute top-2 right-0 flex items-center pr-3">
        <div class="h-6 border-l border-slate-200 mr-3"></div>
                <button id="dropdownButton2" class="h-full text-sm flex justify-center items-center bg-transparent text-slate-700 focus:outline-none">
          Dropdown
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-4 w-4 ml-1">
            <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
          </svg>
        </button>
        <div id="dropdownMenu2" class="min-w-[150px] overflow-hidden absolute left-0 w-full mt-10 hidden w-full bg-white border border-slate-200 rounded-md shadow-lg z-10">
          <ul id="dropdownOptions2">
            <li class="px-4 py-2 text-slate-600 hover:bg-slate-50 text-sm cursor-pointer">Dropdown 1</li>
            <li class="px-4 py-2 text-slate-600 hover:bg-slate-50 text-sm cursor-pointer">Dropdown 2</li>
            <li class="px-4 py-2 text-slate-600 hover:bg-slate-50 text-sm cursor-pointer">Dropdown 3</li>
          </ul>
        </div>
      </div>
      <input
        type="text"
        class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pr-32 pl-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
        placeholder="Enter your text" />
      </div>
    </div>
     
    <script>
      document.getElementById('dropdownButton').addEventListener('click', function() {
        var dropdownMenu = document.getElementById('dropdownMenu');
        if (dropdownMenu.classList.contains('hidden')) {
          dropdownMenu.classList.remove('hidden');
        } else {
          dropdownMenu.classList.add('hidden');
        }
      });
     
      document.getElementById('dropdownOptions').addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
          document.getElementById('dropdownButton').textContent = event.target.textContent;
          document.getElementById('dropdownMenu').classList.add('hidden');
        }
      });
     
      document.addEventListener('click', function(event) {
        var isClickInside = document.getElementById('dropdownButton').contains(event.target) || document.getElementById('dropdownMenu').contains(event.target);
        var dropdownMenu = document.getElementById('dropdownMenu');
     
        if (!isClickInside) {
          dropdownMenu.classList.add('hidden');
        }
      });
    </script>
     
    <script>
      document.getElementById('dropdownButton2').addEventListener('click', function() {
        var dropdownMenu = document.getElementById('dropdownMenu2');
        if (dropdownMenu.classList.contains('hidden')) {
          dropdownMenu.classList.remove('hidden');
        } else {
          dropdownMenu.classList.add('hidden');
        }
      });
     
      document.getElementById('dropdownOptions2').addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
          document.getElementById('dropdownButton2').textContent = event.target.textContent;
          document.getElementById('dropdownMenu2').classList.add('hidden');
        }
      });
     
      document.addEventListener('click', function(event) {
        var isClickInside = document.getElementById('dropdownButton2').contains(event.target) || document.getElementById('dropdownMenu').contains(event.target);
        var dropdownMenu = document.getElementById('dropdownMenu2');
     
        if (!isClickInside) {
          dropdownMenu.classList.add('hidden');
        }
      });
    </script>

* * *

## Disabled Input

Use this example if you want to clearly indicate to users that the input field
is currently not interactive, employing visual cues and styling to convey its
disabled state.

    
    
    <div class="w-full max-w-sm min-w-[200px]">
      <input disabled class="w-full bg-slate-200 pointer-events-none placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
    </div>

  

The input is explicitly marked as disabled (`disabled` attribute), which
prevents user interaction. The styling reflects this state by altering the
border and background color (`disabled:border-0 disabled:bg-blue-gray-50`),
making it visually distinct from active input fields. This design choice helps
users recognize that the input is not currently available for interaction.

* * *

## Input for Dark Surface

Use this example for using contrast and visibility on a dark background (`bg-
gray-900`), making it suitable for interfaces with dark modes or themes.

    
    
    <div class="flex w-72 flex-col">
      <div class="w-full max-w-sm min-w-[200px]">
        <input class="w-full bg-transparent placeholder:text-slate-300 text-white text-sm border border-slate-400 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-50 hover:border-slate-300 shadow-sm focus:shadow" placeholder="Type here..." />
      </div>
    </div>

* * *

## Input Custom Styles (Input with Shadow)

Check out this input with shadow example and learn how to implement custom
styles for your input components with Material Tailwind.

    
    
    <input
      type="email"
      placeholder="Type Here..."
      class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-500 hover:border-slate-300 shadow-lg shadow-gray-100 ring-4 ring-transparent focus:ring-slate-100"
    />

* * *

## Explore More Tailwind CSS Examples

Check out more input component examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks):

• [Newsletter Blocks](https://www.material-tailwind.com/blocks/newsletter-
sections)  
• [Authentification Blocks](https://www.material-
tailwind.com/blocks/authentication)  
• [Contact Blocks](https://www.material-tailwind.com/blocks/contact-sections)  

* * *



