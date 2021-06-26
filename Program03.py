import tkinter as tk
import os
from Root import ProgramBase 
from tkinter import filedialog 
from PIL import Image , ImageTk

class Pgm03(ProgramBase):
    imgWidth = 0
    imgHeight = 0

    divImg = None
    divBtnArea = None
    divMsg = None

    btnOpen = None
    btnReset = None
    btnBlur = None
    btnSharp = None
    btnCompare = None

    lblMsg = None
    lblImg = None

    def __init__(self , root , width = 640 , height = 480) :
        super().__init__(root , width , height)
        self.root.title('Image Viewer')
        
    
    def defineLayout(self, widgets, cols=1, rows=1):
        for c in range(cols):    
            widgets.columnconfigure(c, weight=1)
        for r in range(rows):
            widgets.rowconfigure(r, weight=1)
        return

    def loadlayout(self) :
        align_mode = 'nswe'
        padding= 2

        self.imgWidth = self.root.width
        btnHeight = 40
        msgHeight = 40
        self.imgHeight = self.root.height - btnHeight - msgHeight

        self.divImg = tk.Frame(self.root,  width=self.imgWidth , height=self.imgHeight , bg='blue')
        self.divBtnArea = tk.Frame(self.root,  width=self.imgWidth , height=btnHeight , bg='white')
        self.divMsg = tk.Frame(self.root,  width=self.imgWidth , height=msgHeight , bg='black')

        self.divImg.grid(row=0, column=0, padx=padding, pady=padding, columnspan=1, sticky=align_mode)
        self.divBtnArea.grid(row=1, column=0, padx=padding, pady=padding, columnspan=1, sticky=align_mode)
        self.divMsg.grid(row=2, column=0, padx=padding, pady=padding, columnspan=1, sticky=align_mode)

        #self.root.update()

        self.defineLayout(self.root)
        self.defineLayout(self.divImg)
        self.defineLayout(self.divBtnArea)
        self.defineLayout(self.divMsg)
        
        self.btnOpen = tk.Button(self.divBtnArea, text='open')
        self.btnOpen.pack(side='left')

        self.btnReset = tk.Button(self.divBtnArea, text='reset')
        self.btnReset.pack(side='left')

        self.btnBlur = tk.Button(self.divBtnArea, text='blur')
        self.btnBlur.pack(side='left')

        self.btnSharp = tk.Button(self.divBtnArea,text='sharpen')
        self.btnSharp.pack(side='left')

        self.btnCompare = tk.Button(self.divBtnArea,text='B / A')
        self.btnCompare.pack(side='left')

        self.lblMsg = tk.Label(self.divMsg, text='show message here', bg='black', fg='white')
        self.lblMsg.grid(row=0, column=0, columnspan=1, sticky='w')

    def showMessage(self, msg):
        self.lblMsg['text'] = msg

    def bindBtnEvents(self):
        self.btnOpen['command'] = lambda : self.onOpen()
        self.btnReset['command'] = lambda : self.onReset()   
        self.btnBlur['command'] = lambda : self.onBlur()
        self.btnSharp['command'] = lambda : self.onSharp()

    def loadImage(self , path) :
        im = Image.open(path)
        im.thumbnail( (self.imgWidth , self.imgHeight) )
        image_tk = ImageTk.PhotoImage(im)

        if self.lblImg :
            self.lblImg.destroy()

        self.lblImg = tk.Label(self.divImg , image = image_tk)
        self.lblImg.image = image_tk
        self.lblImg['width'] = self.imgWidth
        self.lblImg['height'] = self.imgHeight

        align_mode = 'nwse'
        self.lblImg.grid(row=0, column=0, sticky=align_mode)

        self.showMessage('file {0:s} loaded'.format(path))


    def onOpen(self) :
        filename = filedialog.askopenfilename(initialdir="./", title="Select file")
        if filename :
            self.showMessage("open file {0:s}".format(filename))
            self.loadImage(filename)
    def onReset(self) :
        '''do it in Program04.py'''
    def onBlur(self) :
        '''do it in Program04.py'''
    def onSharp(self) :
        '''do it in Program04.py'''



if __name__ == '__main__' :
    program = Pgm03(tk.Tk() , width = 800 , height = 600)

    program.loadlayout()
    program.bindBtnEvents()

    cwd = os.getcwd()
    tiger = os.path.join(cwd, "data/tiger.jpeg")
    program.loadImage(tiger)

    
    program.run()
    print("quit, bye bye ...")