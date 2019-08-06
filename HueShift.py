#Created by gonsalvg 2019

from PIL import Image

import os.path
import numpy as np
import colorsys
import time
import multiprocessing as mp

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def worker(image, hue, itr, subItr):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.

    set to create and save two blended images, one leaning
    towards the hue, and one leaning toward the original 
    so they can be interpolated for a nice color shifting img
    """
    img = image.convert('RGBA')
    img2 = image.convert('RGBA')

    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')
    img2 = Image.blend(img2, new_img, .50)

    img2.save("output/blend" + str(itr) + "_" + str(subItr) + ".png", optimize=True)
    img3 = img2.convert('RGB')
    img3.mode = 'RGB'
    img3.save("output/blend" + str(itr) + "_" + str(subItr) + ".jpg", quality=95, optimize=True)

    return

def process_images():

    fileDir = os.getcwd()
    filename = os.path.join(fileDir, 'wallpapers')
    pool = mp.Pool(processes=4)
    itr = 0
    hue = 30
    for root, dirs, files in os.walk(filename):
        for file in files:
            itr += 1
            subItr = 1
            hue = 30

            imgpath = root + os.sep + file
            curImg = Image.open(imgpath)

            filename = ("output/original" + str(itr) + ".jpg")
            curImg.save(filename, "JPEG")

            for subItr in range(1, 13):
                pool.apply_async(
                        worker, (curImg, hue, itr, subItr))
                hue += 30

        pool.close()
        pool.join()
        print("finished hue shifting " + str(itr) + " images!")
        return

if __name__ == '__main__':        
        mp.set_start_method('spawn')

        process_images()
        
