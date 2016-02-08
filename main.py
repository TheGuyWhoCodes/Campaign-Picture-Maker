import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw        
import PIL.Image
from Tkinter import *

bg_size   = [1080,1920]
logo_size = [255,1000]

root = Tk()
root.title("Campaign photo editor")
root.geometry("500x500")

root.mainloop()

def test():
    background = PIL.Image.open("photo.png")
    logo = PIL.Image.open("66.png")

    background_small = logo.resize(bg_size)
    logo_small = logo.resize(logo_size)
    
    background.paste(logo_small, (0, 600), logo_small)
    background.show()
    
    background.save('out.png')
