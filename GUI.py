from Tkinter import Tk, Label, Button
import subprocess


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

        self.find_button = Button(master, text="Find", command=self.greet)
        self.find_button.pack()

    def greet(self):
        print("Greetings!")
    def OpenExplorer(self):
        subprocess.Popen('explorer /select,"H:\Picture\student.jpg"')


root = Tk()
my_gui = Political_Logo(root)
root.mainloop()