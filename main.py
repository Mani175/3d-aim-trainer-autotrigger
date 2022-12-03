import pyautogui
import time
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

def convert_rgb_to_names(rgb_tuple): # a system for converting rgb to normal color names...
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'{names[index]}'

time.sleep(2) # A little delay for switching between the code and the game.

while True:
    x,y = pyautogui.position() # getting mouse position
    px = pyautogui.pixel(x, y) # getting position's pixel color.
    if "blue" in convert_rgb_to_names(px) or "green" in convert_rgb_to_names(px) or "olivedrab" in convert_rgb_to_names(px): # seeing if our mouse is being pointed at a blue or green pixel...
        pyautogui.click(pyautogui.position().x, pyautogui.position().y) # we dont normally pyautgui.click(), because in some cpu's it may have some delay so we make sure we're clicking where the ball is.
        time.sleep(.2) # little delay so it doesn't shoot the ball's blue/green FX.

        

    
