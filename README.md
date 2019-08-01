# HueShift

* Takes all images from folder titled `wallpapers` in same directory and generates 6 hue shifted images to directory `output` based on the original. 

* Useful for color changing wallpapers and smoothly color shifting backgrounds for the OBS image widget, or any other time delayed slideshow/background

* This is just a small exploratory project. I edit photos for fun quite a bit- this mostly came about from wanting to see if I could automate some work.

### Some notes

* ***Images must be JPG or PNG!***

* *It will overwrite whatever is in output if run again, even with new input.*

* It is set to use 4 processor cores to speed up the processing(since python only runs in 1 process normally)

* It is *very* performance hungry, will max out CPU/RAM so use at your own risk. If you are worried about choking your system out, change the amount of processes in the pool to your CPU count -1. :)
