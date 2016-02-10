import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw        
import PIL.Image
from Tkinter import *

bg_size   = [1080,1920]
logo_size = [200,200]

##root = Tk()
##root.title("Campaign photo editor")
##root.geometry("500x500")

##root.mainloop()




def test():
    background = PIL.Image.open("photo.png")
    png = PIL.Image.open("banner.png")
    png.load()

    alpha = png.split()[.2]
    png.putalpha(alpha)
    png.split()[3]
    
    new_png = png.resize((1000, 500), PIL.Image.ANTIALIAS)
    background.resize(bg_size)
    
    background.paste(new_png, (0,600), new_png) # 3 is the alpha channel
    
    background.save('poop.jpg', 'JPEG', quality=100)
    
    background.show()
