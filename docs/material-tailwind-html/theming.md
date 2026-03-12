### Theming


Customize @material-tailwind/html with your own theme. You can change the base
styles like the colors, typography, box-shadows and breakpoints as well as the
components style.

@material-tailwind/html is customizable using the `tailwind.config.js` and you
can set your own theme and styles through the Tailwind CSS configurations for
all of the components.

* * *

## The `class` Attribute

Each component has a `class` attribute that you can use to add tailwindcss
classnames or your own custom classnames.

The `class` attribute overrides the tailwindcss classnames for a component and
sometimes you need to use the `!` modifier before the tailwindcss classnames
to override the classnames for a component.

e.g. `!text-blue-500`

    
    
    <button class="button button-pink !bg-blue-500 px-4" data-ripple-light="true">
      Button
    </button>



