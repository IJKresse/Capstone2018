from Tkinter import *
from PIL import ImageTk, Image
from math import floor

class Display(object):
    
    def __init__(self, maskFile, duration):
        self.root = Tk()
        self.scrnw = self.root.winfo_screenwidth()
        self.scrnh = self.root.winfo_screenheight()
        self.blankScreen = Image.open("blankScrn.png")
        self.blankScreen = self.blankScreen.resize((int(0.93*self.scrnw),int(0.93*self.scrnh)), Image.ANTIALIAS)
        self.mask = Image.open(maskFile)
        self.mask = self.mask.resize((int(0.93*self.scrnw),int(0.93*self.scrnh)), Image.ANTIALIAS)
        self.canvas = Canvas(self.root, width = self.scrnw, height = self.scrnh)
        self.canvas.pack()
        self.MaskImg = ImageTk.PhotoImage(self.mask)
        self.BlankImg = ImageTk.PhotoImage(self.blankScreen)
        self.canvas.create_image(self.scrnw/2,(self.scrnh/2-int(0.035*self.scrnh)),anchor='center', image = self.BlankImg)
        self.root.after(duration*1000, self.showMask)
        self.root.after(duration*2000, self.showBlankScrn)
        self.root.after(duration*3000, lambda: self.root.destroy())
        self.root.mainloop()

    def showMask(self):
        self.canvas.create_image(self.scrnw/2,(self.scrnh/2-int(0.035*self.scrnh)),anchor='center', image = self.MaskImg)
        
        
    def showBlankScrn(self):
        self.canvas.create_image(self.scrnw/2,(self.scrnh/2-int(0.035*self.scrnh)),anchor='center', image = self.BlankImg)

