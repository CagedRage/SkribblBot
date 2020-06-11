from PIL import Image #importing library for image processing, instead of using pillow fork
import sys
import pyautogui
from time import sleep
import numpy as np
# from webcolors import rgb_to_name
# import webcolors
# from colour import Color
np.set_printoptions(threshold=sys.maxsize)
"""
dont mind all of this is doesnt matter anymore but it could help in the future if we do color tracking
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

"""
try:
    skribblImg = Image.open("skribbl.jpg") # image in same folder as py file
except IOError:
    print("bruh ur image is bad like u") # error called if image is not found or something else
    sys.exit(1)
# skribblImg.show() #shows the image because YOU MUST SEE THE POOOP
def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

width, height = skribblImg.size # getting width and height allows us to iterate over each pixel
selected_color = "black"
# sleep(10)
imagepixel = np.zeros((height//5, width//5))
for x in range(0, width):
    for y in range(0, height):
        r, g, b = skribblImg.getpixel((x, y))
        if r > 200 and b > 200 and g > 200:
            pass
        else:
            imagepixel[y//5-1, x//5-1] = 1.0 #TODO: find out if this is actually -1
matprint(imagepixel)
sleep(5)

matprint(imagepixel)
for y in range(height//5):
    for x in range(width//5):
        pixel = imagepixel[y, x]
        if pixel == 1 or pixel == 1.0:
            pyautogui.moveTo(485+x, 300+y) #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click(485+x, 300+y, 1, 0, 'left')


"""SS
for x in range(0, width, 10):#this will iterate over every 10th pixel in the image
    for y in range(0, height, 10):
        #will iterate over each pixel
        r, g, b = skribblImg.getpixel((x, y))
        #will get the specific r g and b value for each pixel
        if r == 255 and g == 255 and b == 255: #checks if the color is white

            if selected_color != "white": #if the color is not already selected as white on skribbl, click on the white button on skribbl and change var selected color
                selected_color = "white"
                pyautogui.moveTo(586, 935)
                pyautogui.click(586, 935, 1, 0 'left')
            pyautogui.moveTo(485+x, 300+y) #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click(485+x, 300+y, 1, 0, 'left')


        else:
            if selected_color != "black": #if the color is not already selected as wblack on skribbl, click on the black button on skribbl and change var selected color
                selected_color = "black"
                pyautogui.moveTo(586, 953)
                pyautogui.click(586, 953, 1, 0, 'left')
            pyautogui.moveTo(485+x, 300+y)  #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click(485+x, 300+y, 1, 0, 'left')

#convert /home/cagedrage/Code/Python/RandomProjects/SkribblBot/skribbl.jpg -resize 300x300 /home/cagedrage/Code/Python/RandomProjects/SkribblBot/skribbl.jpg
"""

pyautogui.FAILSAFE = False # hope this doesnt brick my computer

# White: Point(x=587, y=935)
# Black: Point(x=586, y=953)
# pyautogui.moveTo(586, 935, 1)
# pyautogui.moveTo(586, 953, 1)

# Point(x=485, y=300) FOR SKRIBBL TOP LEFT
