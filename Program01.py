import tkinter as tk
import os
from PIL import Image , ImageTk

from Root import ProgramBase 

class Pgm01(ProgramBase) :
    def __init__ (self , root , width = 640 , height = 480) :
        super().__init__(root,width,height)

    def loadImage(self , path) :
        img = Image.open(path)
        #img.thumbnail( (self.root.width , self.root.height)) : resize by the same shape as the original one
        #img = img.resize((self.root.width , self.root.height) ) : resize into this shape
        img = img.resize((self.root.width , self.root.height) )
        image_tk = ImageTk.PhotoImage(img)

        lbl = tk.Label(self.root, image=image_tk)
        lbl.image = image_tk
        lbl.pack()

        



if __name__ == '__main__':
    program = Pgm01(tk.Tk())

    cwd = os.getcwd()
    tiger = os.path.join(cwd , 'data/tiger.jpeg')
    program.loadImage(tiger)

    program.run()
    print("quit, bye bye ...")
