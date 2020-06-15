from PIL import Image  # importing library for image processing, instead of using pillow fork
import sys
import pyautogui
from time import sleep
import numpy as np
# from webcolors import rgb_to_name
# import webcolors
# from colour import Color


# Prints out a 2d ndarray in a readable and presentable format
def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:" + fmt + "}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:" + str(col_maxes[i]) + fmt + "}").format(y), end="  ")
        print("")


# Converts an image to a black-and-white 2d ndarray representation
# Color version WIP
def drawpictureasarray(image):
    width, height = image.size  # getting width and height allows us to iterate over each pixel
    imageasarray = np.zeros((height // 10, width // 10))
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = image.getpixel((x, y))
            if not (r == 255 and b == 255 and g == 255):
                imageasarray[y // 10 - 1, x // 10 - 1] = 1.0

    return imageasarray


# Make numpy not truncate when printing out arrays to display
np.set_printoptions(threshold=sys.maxsize)

# Open the image - image is now variable skribblImg
try:
    skribblImg = Image.open("skribbl.jpg")  # image in same folder as py file
except IOError:
    print("bruh ur image is bad like u")  # error called if image is not found or something else
    sys.exit(1)

# skribblImg.show() # uncomment this if you want to display the image 

imagepixel = drawpictureasarray(skribblImg)

matprint(imagepixel)  # aaaa

# selected_color variable keeps track of currently selected color
selected_color = "black"
pyautogui.FAILSAFE = False  # hope this doesnt brick my computer
sleep(5)

rows = len(imagepixel) 
columns = len(imagepixel[0]) 
# WIP MAIN LOOP FOR DRAWING THE IMAGE
for x in range(0,rows): # this will iterate over every 10th pixel in the image
    for y in range(0, columns):
        if imagepixel[y][x]==0:
            next
        else:            
            pyautogui.moveTo(485+(x*10), 300+(y*10))  #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click()
# No longer necessary in this exact format because we have a pre-calculated array to draw
# However, this can still maybe serve as a framework in the future
"""
for x in range(0, width, 10): # this will iterate over every 10th pixel in the image
    for y in range(0, height, 10):
        #will iterate over each pixel
        r, g, b = skribblImg.getpixel((x, y))
        #will get the specific r g and b value for each pixel
        if r == 255 and g == 255 and b == 255: #checks if the color is white

            if selected_color != "white": #if the color is not already selected as white on skribbl, click on the white button on skribbl and change var selected color
                selected_color = "white"
                pyautogui.moveTo(x=889, y=110)
                pyautogui.click()
            pyautogui.moveTo(485+x, 300+y) #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click()


        else:
            if selected_color != "black": #if the color is not already selected as wblack on skribbl, click on the black button on skribbl and change var selected color
                selected_color = "black"
                pyautogui.moveTo(x=889, y=68)
                pyautogui.click()
            pyautogui.moveTo(485+x, 300+y)  #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click()

# convert /home/cagedrage/Code/Python/RandomProjects/SkribblBot/skribbl.jpg -resize 300x300 /home/cagedrage/Code/Python/RandomProjects/SkribblBot/skribbl.jpg

"""
"""
# Potential design for color "rounding" - unused currently, but could work in the future
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css21_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

    def get_color_name(requested_color):
        try:
        closest_name = rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_colour(requested_color)
    return closest_name
def print_color()
        width, height = image.size  # getting width and height allows us to iterate over each pixel
    imageasarray = np.zeros((height // 10, width // 10))
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = image.getpixel((x, y))
"""
            
# White: Point(x=587, y=935)
# Black: Point(x=586, y=953)
# pyautogui.moveTo(586, 935, 1)
# pyautogui.moveTo(586, 953, 1)

# Point(x=485, y=300) FOR SKRIBBL TOP LEFT

