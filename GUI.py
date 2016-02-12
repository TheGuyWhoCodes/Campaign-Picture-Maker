from Tkinter import *

import sys
import subprocess


class Political_Logo:

    def __init__(self, master):
        self.master = master
        master.title("Campaign Logo Maker")

        root = Tk()
        my_gui = Political_Logo(root)
        root.mainloop()

        self.label = Label(master, text="Picture Logo")
        self.label.pack()
        
        self.label = Label(master, text="Banner")
        self.label.pack()

        self.find_button = Button(master, text="Close Program", command=self.exit)
        self.find_button.pack()

        self.find_button = Button(master, text="Find Campaign Background", command=self.greet)
        self.find_button.pack()

        T = Text(root, height=2, width=30)
        T.pack()
        T.insert(END, "Just a text Widget\nin two lines\n")

        self.find_button = Button(master, text="Find Campaign Logo", command=self.greet())
        self.find_button.pack()

    def greet(self):
        print("Greetings!")

    def OpenExplorer(self):
        subprocess.Popen('explorer /select,"H:\Picture\student.jpg"')

    def exit(self):
        sys.exit()

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


