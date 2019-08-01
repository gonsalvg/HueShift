#Created by gonsalvg 2019

from PIL import Image, ImageChops, ImageColor

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

def worker(image, hue, itr, sub_itr):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.

    set to create and save two blended images, one leaning
    towards the hue, and one leaning toward the original 
    so they can be interpolated for a nice color shifting img
    """
    img = image.convert('RGBA')
    img2 = image.convert('RGBA')
    #img3 = image.convert('RGBA')

    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')
    img2 = Image.blend(img2, new_img, .65)
    #img3 = Image.blend(img3, new_img, .2 )

    img2.save("output/blend" + str(itr) + "_" + str(sub_itr) + "_1" + ".png")
    #img3.save("output/blend" + str(itr) + "_" + str(sub_itr) + "_2" + ".png")

    return

def processImages():

    fileDir = os.getcwd()
    filename = os.path.join(fileDir, 'wallpapers')
    pool = mp.Pool(processes=4)
    itr = 0
    hue = 30
    for root, dirs, files in os.walk(filename):
        for file in files:
            itr += 1
            sub_itr = 1
            hue = 30

            imgpath = root + os.sep + file
            curImg = Image.open(imgpath)

            filename = ("output/original" + str(itr) + ".png")
            curImg.save(filename)

            for sub_itr in range(1, 13):
                pool.apply_async(
                worker, (curImg, hue, itr, sub_itr))
                hue += 30

        pool.close()
        pool.join()
        print("finished hue shifting " + str(itr) + " images!")
        return

if __name__ == '__main__':        
        mp.set_start_method('spawn')

        processImages()
        
