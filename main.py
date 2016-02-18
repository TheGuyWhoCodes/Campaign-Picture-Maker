import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw        
import PIL.Image
from Tkinter import *

bg_size   = [1080,1920]
logo_size = [200,200]
seal_size = [200,200]

##root = Tk()
##root.title("Campaign photo editor")
##root.geometry("500x500")

##root.mainloop()

seal = 0


def test(seal, main_image, logo_image):
    logo_image = PIL.Image.open('seal.png')
    main_image = PIL.Image.open('photo.png')
    img_w, img_h = main_image.size
    
    if seal == 0:
        print("We converting a banner its lit")
        offset = (0,780)
        main_image.paste(logo_image, offset)
        main_image.save('out.png')
        main_image.show()
    else:
        logo_image.resize(seal_size)
        offset = (0,600)
        print("We are converting a seal over here")
    
