from Tkinter import Tk, Label, Button
import subprocess
import sys

class Political_Logo:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Picture Logo")
        self.label.pack()
        
        self.label = Label(master, text="Banner")
        self.label.pack()

        self.find_button = Button(master, text="Find", command=self.OpenExplorer)
        self.find_button.pack()
        
        self.find_campaign_background_button = Button(master, text="Find Campaign Background", command=self.greet)
        self.find_campaign_background_button.pack()
        
        self.find_button = Button(master, text="Find", command=self.greet)
        self.find_button.pack()
    
        self.find_filename_button = Button(master, text="Find filename", command= self.find_filename("../"))
    
    def greet(self):
        print("Greetings!")
    def OpenExplorer(self):
        subprocess.Popen('explorer /select,"H:\Picture\student.jpg"')
    def find_filename(substring, self):
        import os
        import re
        files = os.listdir(os.getcwd())
        for file in files:
            search = re.search(substring, file)
            if search:
                filename = file
                break
        return filename
root = Tk()
my_gui = Political_Logo(root)
root.mainloop()