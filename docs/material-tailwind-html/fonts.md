### Fonts


Customize the default font families for @material-tailwind/html and add your
own custom fonts that you like to have for your project.

  
  

## Default Font Families

@material-tailwind/html provides a set of default font families that you can
use.

    
    
    const fontFamily = {
      sans: ["Roboto", "sans-serif"],
      serif: ["Roboto Slab", "serif"],
      body: ["Roboto", "sans-serif"],
      mono: [
        "SFMono-Regular",
        "Menlo",
        "Monaco",
        "Consolas",
        "Liberation Mono",
        "Courier New",
        "monospace",
      ],
    };

* * *

## Customizing Font Families

You can customize the default font families for @material-tailwind/html very
easy and straightforward, it's the same as customizing font families for
tailwindcss.

You just need to customize the font family that you like through the
`fontFamily` object for `tailwind.config.js` file.

    
    
    module.exports = withMT({
      theme: {
        fontFamily: {
          sans: ["Open Sans", "sans-serif"],
        },
      },
    });

  
  
  

For more information about tailwindcss font families customization, please
check the [TailwindCSS Documentation](https://tailwindcss.com/docs/font-
family?ref=material-tailwind)



