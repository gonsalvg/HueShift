# HueShift

* Takes all images from folder titled `wallpapers` in same directory and generates 6 hue shifted images to directory `output` based on the original. 

* Useful for color changing wallpapers and smoothly color shifting backgrounds for the OBS(Open Broadcaster Software) image widget, or any other time delayed slideshow/background

* This is just a small exploratory project. I edit photos for fun quite a bit- this mostly came about from wanting to see if I could automate some work.

### Some notes

* ***Images must be JPG or PNG!***

* PNG seems to work better as input(and output) due to transparency layer but outputs very large sized PNGs.

* Tested on Linux and Windows

* *It will overwrite whatever is in output if run again, even with new input.*

* It is set to use 3 processor cores to speed up the processing(since python only runs in 1 process normally)
