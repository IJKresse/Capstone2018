from Tkinter import *
#from PIL import ImageTk, Image
root = Tk()
canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()
#img = ImageTk.PhotoImage(Image.open("binaryImage.png"))
#canvas.create_image(20,20,anchor=NW, image = img)
root.mainloop()