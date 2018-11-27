from Tkinter import *
from time import sleep

class Application(Frame):
    def say_hi(self):
        print "hello world"
        
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        
        self.QUIT.pack=({"side":"left"})
        
        self.hi_there = Button(self)
        self.hi_there["text"] = "hello"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side":"left"})
        
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master = root)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
#sleep(5)
app.mainloop()
root.destroy()