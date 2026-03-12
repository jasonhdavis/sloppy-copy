### Switch


Use our Tailwind CSS toggle switch component to let users adjust settings
on/off. The option that the switch controls, as well as the state it's in,
should be made clear from the corresponding inline label.

Switch components are used in various scenarios in web development, including
settings options, feature toggles, form inputs, interactive controls,
accessibility options, and more.

Use the following examples to create a simple and easy-to-use switch component
for your Tailwind CSS project.

  

## Toggle Switch Examples:

## Default Toggle Switch

Use this simple component example that changes the background color, border
color, and shadow of the switch when it is in the "checked" state.

    
    
    <div class="relative inline-block w-11 h-5">
      <input checked id="switch-component" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-slate-800 cursor-pointer transition-colors duration-300" />
      <label for="switch-component" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer">
      </label>
    </div>

* * *

## Checked Toggle Switch

In this example, you can see how to implement your switch to be checked by
default.

    
    
    <div class="relative inline-block w-11 h-5">
      <input checked checked id="switch-component-1" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-slate-800 cursor-pointer transition-colors duration-300" />
      <label for="switch-component-1" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer">
      </label>
    </div>

* * *

## Toggle Switch Colors

Check out this toggle example to see how you can create a colored diverse set
of toggle switches that can be used for various settings or options in a web
application.

    
    
    <div class="flex w-max gap-6">
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-blue" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-blue-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-blue" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-blue-600 cursor-pointer">
        </label>
      </div>
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-red" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-red-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-red" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-red-600 cursor-pointer">
        </label>
      </div>
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-green" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-green-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-green" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-green-600 cursor-pointer">
        </label>
      </div>
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-amber" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-amber-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-amber" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-amber-600 cursor-pointer">
        </label>
      </div>
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-teal" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-teal-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-teal" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-teal-600 cursor-pointer">
        </label>
      </div>
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-indigo" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-indigo-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-indigo" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-indigo-600 cursor-pointer">
        </label>
      </div>
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-purple" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-purple-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-purple" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-purple-600 cursor-pointer">
        </label>
      </div>
      <div class="relative inline-block w-11 h-5">
        <input checked id="switch-component-pink" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-pink-600 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-pink" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-pink-600 cursor-pointer">
        </label>
      </div>
    </div>

* * *

## Toggle Switch with Label

See below how to create a custom switch component with a clear, descriptive
label, making it suitable for settings pages, forms, or anywhere else where
users need to make a binary choice.

Off

On

    
    
    <div class="inline-flex items-center gap-2">
      <label for="switch-component-on" class="text-slate-600 text-sm cursor-pointer">Off</label>
     
      <div class="relative inline-block w-11 h-5">
        <input id="switch-component-on" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-slate-800 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-on" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer">
        </label>
      </div>
     
      <label for="switch-component-on" class="text-slate-600 text-sm cursor-pointer">On</label>
    </div>

* * *

## Toggle Switch Ripple Effect

This example showcases a pair of switch components arranged vertically, each
designed to toggle the state of a "Ripple Effect" feature, one for turning it
on and the other for turning it off.

Ripple Effect On

Ripple Effect Off

    
    
    <div class="flex flex-col gap-6">
      <div class="relative inline-flex gap-2">
        <div class="w-11 h-5">
          <input id="switch-component-ripple-on" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-slate-800 cursor-pointer transition-colors duration-300" />
     
          <label
            for="switch-component-ripple-on"
            class="absolute top-0 left-0 h-5 w-5 cursor-pointer rounded-full border border-slate-300 bg-white shadow-sm transition-all duration-300 before:absolute before:top-2/4 before:left-2/4 before:block before:h-10 before:w-10 before:-translate-y-2/4 before:-translate-x-2/4 before:rounded-full before:bg-slate-400 before:opacity-0 before:transition-opacity hover:before:opacity-10 peer-checked:translate-x-6 peer-checked:border-slate-800"
          >
            <div
              class="top-2/4 left-2/4 inline-block -translate-x-2/4 -translate-y-2/4 rounded-full p-5"
              data-ripple-dark="true"
            ></div>
          </label>
        </div>
     
        <label for="switch-component-ripple-on" class="text-slate-600 text-sm cursor-pointer">
          Ripple Effect On
        </label>
      </div>
     
      <div class="inline-flex items-center gap-2">
        <div class="relative inline-block w-11 h-5">
          <input id="switch-component-ripple-off" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-slate-800 cursor-pointer transition-colors duration-300" />
          <label for="switch-component-ripple-off" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer">
          </label>
        </div>
     
        <label for="switch-component-ripple-off" class="text-slate-600 text-sm cursor-pointer">
          Ripple Effect Off</label>
      </div>
    </div>

* * *

## Toggle Switch Disabled

This example illustrates a switch component designed to appear disabled and
non-interactive. The key features indicating its disabled state include the
use of the disabled attribute on the input element, as well as Tailwind CSS
classes `opacity-50` and `pointer-events-none` applied to the parent `div` to
visually and functionally disable the entire switch component.

    
    
    <div class="relative inline-block w-11 h-5 pointer-events-none">
      <input disabled id="switch-component-disabled" type="checkbox" class="peer appearance-none disabled:opacity-50 w-11 h-5 bg-slate-100 rounded-full checked:bg-slate-800 cursor-pointer transition-colors duration-300" />
      <label for="switch-component-disabled" class="absolute opacity-50 top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer">
      </label>
    </div>

* * *

## Toggle Switch with Description

A switch component like the "Remember Me" example below is typically used in
login forms or authentication pages on websites and applications.

Remember Me

You'll be able to login without password for 24 hours.

    
    
    <div class="inline-flex gap-2">
      <div class="relative inline-block w-11 h-5">
        <input id="switch-component-desc" type="checkbox" class="peer appearance-none w-11 h-5 bg-slate-100 rounded-full checked:bg-slate-800 cursor-pointer transition-colors duration-300" />
        <label for="switch-component-desc" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer">
        </label>
      </div>
     
      <label for="switch-component-desc" class="text-slate-600 text-sm cursor-pointer">
        <div>
          <p class="font-medium">
            Remember Me
          </p>
          <p class="text-slate-500">
            You&apos;ll be able to login without password for 24 hours.
          </p>
        </div>
      </label>
    </div>

* * *

## Toggle Switch with Custom Styles

Check out this example to see how you can implement custom styles to your
switch component.

    
    
    <div class="relative inline-block w-11 h-5">
      <input id="switch-component-custom" type="checkbox" class="peer appearance-none w-11 h-4 bg-slate-100 border border-slate-300 rounded-full checked:bg-slate-800 checked:border-slate-800 cursor-pointer transition-colors duration-300" />
      <label for="switch-component-custom" class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer">
      </label>
    </div>

* * *

## Required Scripts

The toggle switch component needs a required script file for the ripple effect
to work, you just need to add the script file to the bottom of your html file.

    
    
    <!-- from node_modules -->
    <script src="node_modules/@material-tailwind/html@latest/scripts/ripple.js"></script>
     
    <!-- from cdn -->
    <script src="https://unpkg.com/@material-tailwind/html@latest/scripts/ripple.js"></script>

* * *

## Explore More Tailwind CSS Examples

Looking for more switch examples? Check out our **[Account
Sections](https://www.material-tailwind.com/blocks/account)** from [Material
Tailwind Blocks](https://www.material-tailwind.com/blocks).



