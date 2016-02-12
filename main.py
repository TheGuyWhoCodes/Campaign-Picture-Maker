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

seal = 0


def test():
    img = PIL.Image.open('seal.png')
    img2 = PIL.Image.open('photo.png')
    img_w, img_h = img.size
    
    if seal == 0:
        print("We converting a banner its lit")
    else:
        print("We are converting a seal over here")
    
    offset = (0,780)
    img2.paste(img, offset)
    img2.save('out.png')
