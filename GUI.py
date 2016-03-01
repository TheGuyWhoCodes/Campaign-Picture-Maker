import Tkinter
from Tkinter import *
import subprocess
import sys
import tkFileDialog
import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw        
import PIL.Image

bg_size   = [1080,1920]
logo_size = [200,200]
seal_size = [200,200]


seal = 0


class TheGui:
    global wow
    global wink

    wow = ""
    wink = ""

    global in_path
    global in_path1
    def __init__(self, parent):
        #------- frmSetup ----------#
        self.frmSetup = Frame(parent, bd=5)
        self.frmSetup.pack()

        self.inChoices = ('Text', 'Midi')
        self.varRadio = IntVar()

        self.r1 = Radiobutton(self.frmSetup, text="Convert a logo",
            variable=self.varRadio, value=0, command=self.logo)
        self.r1.pack(anchor=W)

        self.r2 = Radiobutton(self.frmSetup, text="Convert a banner", 
            variable=self.varRadio, value=1, command=self.banner)
        self.r2.pack(anchor=W)
        #------- frmSetup ----------#

        sep = Frame(parent, width=1, bd=5, bg='black')
        sep.pack(fill=X, expand=1)

        #------- frmIn ----------#
        # http://effbot.org/tkinterbook/tkinter-widget-styling.htm
        self.frmIn = Frame(parent, bd=5)         
        self.frmIn.pack()

        self.lblIn = Label(self.frmIn, text='Campaign Background', width=20)
        self.lblIn.pack(side=LEFT) 

        self.inFilePath = StringVar() # http://effbot.org/tkinterbook/entry.htm
        self.entIn = Entry(self.frmIn, width=20, textvariable=self.inFilePath)
        self.entIn.pack(side=LEFT)


        self.btnIn = Button(self.frmIn, text='Browse', command=self.OpenExplorer)
        self.btnIn.pack(side=LEFT) 
        #------- frmIn ----------#


        #------- frmOut ----------#
        self.frmOut = Frame(parent, bd=5)
        self.frmOut.pack()

        self.lblOut = Label(self.frmOut, text='Logo Path', width=20)
        self.lblOut.pack(side=LEFT) 

        self.outFilePath = StringVar()
        self.entOut = Entry(self.frmOut, width=20, textvariable=self.outFilePath)
        self.entOut.pack(side=LEFT) 

        self.btnOut = Button(self.frmOut, text='Browse', command=self.OpenExplorer1)
        self.btnOut.pack(side=LEFT) 
        #------- frmOut ----------#

        sep = Frame(parent, width=1, bd=5, bg='black')
        sep.pack(fill=X, expand=1)

        #------- frmButtons ----------#
        self.frmOut = Frame(parent, bd=5)
        self.frmOut.pack()

        self.btnConvert = Button(self.frmOut, 
            text='Convert', command=lambda: self.test(self.wow, self.wink))
        self.btnConvert.pack() 

    #------- All of the commands are here ----------#


    def logo(self):
        self.seal = 1
        print self.seal
    def banner(self):
        self.seal = 0
        print self.seal
    def OpenExplorer(self):
        self.entIn.insert(END,"")
        Tkinter.Tk().withdraw() # Close the root window
        in_path = tkFileDialog.askopenfilename()
        self.wow = in_path
        ##self.outFilePath.insert(1.0, self.wow)
        self.entIn.insert(END, self.wow)
        print self.wow , "\n"
    
    def OpenExplorer1(self):
        self.entOut.insert(END,"")
        Tkinter.Tk().withdraw() # Close the root window
        in_path1 = tkFileDialog.askopenfilename()
        self.wink = in_path1
        self.entOut.insert(END, self.wink)
        print self.wink , "\n"
    
    def test(self,main_image, logo_image):
        name = main_image
        logo = logo_image
        img = PIL.Image.open(logo_image)   ## Opens original image
        img2 = PIL.Image.open(main_image)    
        
        main_width, main_height = img2.size
        logo_width, logo_height = img.size       ## So we can have the path stored and stuff
        if name:
            img.save("new_logo.png")
            new_logo = PIL.Image.open("new_logo.png")         ##Saves a new version of the image  
        if logo:
            img2.save("main_image.png")
            new_main = PIL.Image.open("main_image.png")
            
            
        if self.seal == 0:
            if main_height < 800:
                logo_resize = new_logo.resize((logo_width/3, logo_height/3))
                small = 0                                                                   ## Resizes the images in case the main image is too small
                logo_width, logo_height = logo_resize.size    
            print("We converting a banner its lit")

            main_offset = (main_width - logo_width)/2
            offset = (main_offset,(main_height - logo_height))
            if  main_height < 800:                                                             ##Sets up offset for the images
                new_main.paste(logo_resize, offset)                                                
            else:
                new_main.paste(new_logo, offset)
            new_main.save('out.png')
            new_main.show()
        else:
            if main_height < 800:
                logo_resize = new_logo.resize((100, 100))
                small = 0
            else:
                logo_resize = new_logo.resize((300, 300))
                small = 1

            print("We are converting a seal over here")
            if small == 1:
                offset = (0,(main_height - 300))
            else:
                offset = (0,(main_height - 100))

            new_main.paste(logo_resize, offset)
            new_main.save('out.png')
            new_main.show()
        os.remove("new_logo.png") 
        os.remove("main_image.png") 
        
root = Tk()
root.wm_title("Campaign Maker")
my_gui = TheGui(root)
root.mainloop()
