### Screens


Customize the default breakpoints for @material-tailwind/html and add your own
custom breakpoints that you like to have for your project.

  
  

## Default Screens

@material-tailwind/html provides a set of default breakpoints for different
screen sizes that you can use.

    
    
    const screens = {
      sm: "540px",
      md: "720px",
      lg: "960px",
      "lg-max": { max: "960px" },
      xl: "1140px",
      "2xl": "1320px",
    };

* * *

## Customize the Default Breakpoints

You can customize the default breakpoints for @material-tailwind/html very
easy and straightforward, it's the same as customizing breakpoints for
tailwindcss.

You just need to customize the breakpoint that you like through the `screens`
object for `tailwind.config.js` file.

    
    
    module.exports = withMT({
      theme: {
        screens: {
          sm: "640px",
          // rest of the breakpoints
        },
      },
    });

* * *

## Adding New Breakpoint

You can add new breakpoint for @material-tailwind/html very easy and
straightforward, it's the same as adding new breakpoint for tailwindcss.

You just need to add your own breakpoint to the `extend` and `screens` object
for `tailwind.config.js` file.

    
    
    module.exports = withMT({
      theme: {
        extend: {
          screens: {
            "3xl": "1600px",
          },
        },
      },
    });

  
  
  

For more information about tailwindcss breakpoints customization, please check
the [TailwindCSS
Documentation](https://tailwindcss.com/docs/screens?ref=material-tailwind)



## Components

