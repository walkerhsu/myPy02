import tkinter as tk
from Program03 import Pgm03
import os
import cv2
from PIL import Image , ImageTk
import numpy as np

class Pgm04(Pgm03) :
    cvImg = None
    cvImgUpdate = None
    def __init__(self , root , width = 640 , height = 480) :
        super().__init__(root , width , height)
        root.title('Image Editor')
    
    def bindBtnEvents(self) :
        self.btnOpen['command'] = lambda : self.onOpen()
        self.btnReset['command'] = lambda : self.onReset()   
        self.btnBlur['command'] = lambda : self.onBlur()
        self.btnSharp['command'] = lambda : self.onSharp()
        self.btnCompare.bind('<ButtonPress-1>', self.onBAPress)
        self.btnCompare.bind('<ButtonRelease-1>',self.onBARelease)

    def onReset(self):
        self.updateImage(self.cvImg)
        self.showMessage('aply sharpen effect')

    def onBlur(self):
        size = 15
        self.cvImgUpdate = cv2.GaussianBlur(self.cvImgUpdate , (size , size) , 0)
        self.updateImage(self.cvImgUpdate)
        self.showMessage('apply gaussian blur')

    def onSharp(self):    
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        self.cvImgUpdate = cv2.filter2D(self.cvImgUpdate , -1 , kernel)
        self.updateImage(self.cvImgUpdate)
        self.showMessage('aply sharpen effect')

    def onBAPress(self , effect): 
        self.updateImage(self.cvImg)
        self.showMessage("show original image")

    def onBARelease(self , effect):
        self.updateImage(self.cvImgUpdate)
        self.showMessage("show original image")

    def loadImage(self , path) :
        self.cvImg = cv2.imread(path)
        self.cvImg = self.cvImg[:,:,::-1] # 將 BGR 圖片轉為 RGB 圖片
        self.cvImgUpdate = self.cvImg.copy()
        self.updateImage(self.cvImg)
        self.showMessage("file {0:s} loaded".format(path))

    def updateImage(self , img) :
        im = Image.fromarray(img)
        im.thumbnail( (self.imgWidth , self.imgHeight) )
        image_tk = ImageTk.PhotoImage(im)

        if self.lblImg:
            self.lblImg.destroy()

        # create label
        self.lblImg = tk.Label(self.divImg, image=image_tk)
        self.lblImg.image = image_tk
        self.lblImg['width'] = self.imgWidth
        self.lblImg['height'] = self.imgHeight

        align_mode = 'nswe'
        self.lblImg.grid(row=0, column=0, sticky=align_mode)

if __name__ == '__main__':
    program = Pgm04(tk.Tk(), width=800, height=600)
    program.loadlayout()
    program.bindBtnEvents()
    # load image data 
    cwd = os.getcwd()
    tiger = os.path.join(cwd, "data/tiger.jpeg")
    program.loadImage(tiger)

    program.run()
    print("quit, bye bye ...")