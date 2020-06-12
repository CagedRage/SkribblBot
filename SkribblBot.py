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
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            if x == 150 and y == 150:
                print("owo?")
            r, g, b = image.getpixel((x, y))
            imageasarray[y // 10 - 1, x // 10 - 1] = getcolorrgb([r, g, b])

    return imageasarray


# FORMAT: index is color code, 2d list of R G B respectively
def recordskribblpalette():  # records the RGB values of the skribbl color palette using color codes in getcolorrgb
    return [[255, 255, 255], [193, 193, 193], [239, 19, 11], [255, 113, 0], [255, 228, 0], [0, 204, 0], [0, 178, 255],
            [35, 31, 211], [163, 0, 186], [211, 124, 170], [160, 82, 45],  # end of row 1
            [0, 0, 0], [76, 76, 76], [116, 11, 7], [194, 56, 0], [232, 162, 0], [0, 85, 16], [0, 86, 158], [14, 8, 101],
            [85, 0, 105], [167, 85, 116], [99, 48, 13]]  # end of row 2
    pass


# "color" parameter is [r, g, b]
# returns color code with least distance
def getcolorrgb(color):  # "Rounds" to nearest color in skribbl based on RGB values using simpler form of 3d distance
    global skribblcolorpalette  # used from recordskribblpalette function
    # r, g, b arguments should be color of pixel in image
    # skribbl color palette https://cdn.discordapp.com/attachments/674087507260080142/721115804917301249/unknown.png

    # the color codes are, in the same grid,
    # 0  1  2  3  4  5  6  7  8  9  10
    # 11 12 13 14 15 16 17 18 19 20 21

    # closestcolor stores the closest color in skribbl palette to the color argument
    # index 0 is the "distance", index 1 is the index (color code)
    # default to distance 99999 so it hopefully doesn't stick with r=69, g=69, b=69
    closestcolor = [99999, -1]

    for x in range(len(skribblcolorpalette)):
        # for each color in skribbl's color palette
        # if the distance between current color and color in image is less than the previous closest color's distance
        # then store the current color as the new closest color
        # and new least distance as current distance
        # and color code as current color code
        dist = getdistance(color, skribblcolorpalette[x])
        if dist < closestcolor[0]:
            closestcolor[0] = dist
            closestcolor[1] = x

    return closestcolor[1]


# gets the distance between two colors, [r, g, b] and [r, g, b]
# it's just the sum of (r-r2)^2, (g-g2)^2, and (b-b2)^2
def getdistance(color, color2):  # Finds the 3d distance between two colors: [r, g, b] and [r, g, b]
    # _dist is "_ distance" in english
    rdist = abs(color[0] - color2[0])
    gdist = abs(color[1] - color2[1])
    bdist = abs(color[2] - color2[2])

    return rdist + gdist + bdist


skribblcolorpalette = recordskribblpalette()  # Store skribbl colors RGB values using the color codes in getcolorrgb
np.set_printoptions(threshold=sys.maxsize)  # Make numpy not truncate when printing out arrays to display
try:
    skribblImg = Image.open("skribbl.jpg")  # image in same folder as py file is now stored as skribblImg
except IOError:
    print("bruh ur image is bad like u")  # error called if image is not found or something else
    sys.exit(1)
# skribblImg.show() # uncomment this if you want to display the image
imagepixel = drawpictureasarray(skribblImg)  # Generate the 2d ndarray for the skribblImg
matprint(imagepixel)  # Print the array
selected_color = "black"  # selected_color variable keeps track of currently selected color
pyautogui.FAILSAFE = False  # hope this doesnt brick my computer

"""
# WIP MAIN LOOP FOR DRAWING THE IMAGE
# No longer necessary in this exact format because we have a pre-calculated array to draw
# However, this can still maybe serve as a framework in the future

for x in range(0, width, 10): # this will iterate over every 10th pixel in the image
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
"""

# White: Point(x=587, y=935)
# Black: Point(x=586, y=953)
# pyautogui.moveTo(586, 935, 1)
# pyautogui.moveTo(586, 953, 1)

# Point(x=485, y=300) FOR SKRIBBL TOP LEFT
