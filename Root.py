import tkinter as tk
class ProgramBase() :
    def __init__ (self , root , width = 600 , height = 400) :
        
        x = 450
        y = 150
        root.width = width
        root.height = height
        root.geometry('%dx%d+%d+%d' % (root.width , root.height , x , y ) )
        root.title('window')
        root.bind_all('<Key>' , self.onKey)
        self.root = root

    def run(self):
        self.root.mainloop()

    def onKey(self, event):  
        #event.char == event.keysym :  normal number and letter characters
        #len(event.char) == 1 : special charcters like []/.,><#$ 
        if event.char == event.keysym or len(event.char) == 1: 
            if event.keysym == 'Right':
                print("key Right") 
            elif event.keysym == 'Left':
                print("key Left") 
            elif event.keysym == 'space':
                print("key Space") 
            elif event.keysym == 'Escape':
                print("key Escape") 
                self.root.destroy()

if __name__ == '__main__' :
    program = ProgramBase(tk.Tk())
    program.run()
    print('quit, bye bye.....')
