### Video


Use our Tailwind CSS video examples to add video player to your web project.
This component displays media content (video) on your website.

Our component encapsulates all the functionalities needed to play videos,
including but not limited to playback controls (like play/pause, volume
control, fullscreen toggle), loading of video sources, display of video
metadata (such as duration and current time).

Check out below our component examples.

  

## Video Examples:

## Simple Video Player

Add videos to your website using our component that comes with rounded corners
and playback controls.

Your browser does not support the video tag.

    
    
        <video class="h-full w-full rounded-lg" controls>
          <source
            src="https://docs.material-tailwind.com/demo.mp4"
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>

* * *

## Autoplay Video

This example includes the autoPlay attribute on the `<video>` tag making the
video start playing automatically as soon as it is loaded, without requiring
the user to initiate playback manually.

Your browser does not support the video tag.

    
    
        <video class="h-full w-full rounded-lg" controls autoPlay>
          <source src="/demo.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>

* * *

## Muted Video

By adding `muted` to the <video> tag, the video will play without sound by
default when the page loads. This attribute is particularly important in
conjunction with autoPlay, as many modern web browsers restrict autoplay
functionality for videos with sound to prevent disrupting the user experience.

Your browser does not support the video tag.

    
    
        <video class="h-full w-full rounded-lg" controls autoPlay muted>
          <source src="/demo.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>

  

Videos that autoplay with sound can be intrusive, so this restriction aims to
improve the overall browsing experience.

However, videos that are muted are typically allowed to autoplay, making this
combination useful for background videos, promotional content, or any scenario
where immediate engagement is desired without audio disruption.

* * *

## Explore More Tailwind CSS Examples

Check out more video component examples from [Material Tailwind
Blocks](https://www.material-tailwind.com/blocks).



## Plugins


Content not found.

