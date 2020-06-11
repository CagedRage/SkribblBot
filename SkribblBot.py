from PIL import Image #importing library for image processing
import sys
import pyautogui
#from webcolors import rgb_to_name
#import webcolors
#from colour import Color
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
    skribblImg = Image.open("skribbl.jpg") #image in same folder as py file
except IOError:
    print("bruh ur image is bad like u") #error called if image is not found or something else
    sys.exit(1)
skribblImg.show() #shows the image because YOU MUST SEE THE POOOP

width, height = skribblImg.size #getting width and height allows us to iterate over each pixel
selected_color = "white"
for x in range(width):
    for y in range(heighgt):
        #will iterate over each pixel
        r, g, b = skribblImg.getpixel((x, y))
        #will get the specific r g and b value for each pixel
        if r == 255 and g == 255 and b == 255: #checks if the color is white
            if selected_color != "white": #if the color is not already selected as white on skribbl, click on the white button on skribbl and change var selected color
                selected_color = "white"
                pyautogui.moveTo(586, 935, 0.2)
                pyautogui.click(586, 935, 1, 0.2, 'left')
            pyautogui.moveTo(485+x, 300+y, 0.2) #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click(485+x, 300+y, 1, 0.2, 'left')
        else:
            if selected_color != "black": #if the color is not already selected as wblack on skribbl, click on the black button on skribbl and change var selected color
                selected_color = "black"
                pyautogui.moveTo(586, 953, 0.2)
                pyautogui.click(586, 953, 1, 0.2, 'left')
            pyautogui.moveTo(485+x, 300+y, 0.2)  #moves to the top left of the skribbl drawing board + the specific x and y value we are on
            pyautogui.click(485+x, 300+y, 1, 0.2, 'left')




pyautogui.FAILSAFE = False #hope this doesnt brick my computer

#White: Point(x=587, y=935)
#Black: Point(x=586, y=953)
#pyautogui.moveTo(586, 935, 1)
#pyautogui.moveTo(586, 953, 1)
#print(pyautogui.position())
#Point(x=485, y=300) FOR SKRIBBL TOP LEFT
