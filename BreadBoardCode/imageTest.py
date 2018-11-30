from Tkinter import *
from PIL import ImageTk, Image
from math import floor

root = Tk()
scrnw = root.winfo_screenwidth()
scrnh = root.winfo_screenheight()
blankScreen = Image.open("blankScrn.png")
blankScreen = blankScreen.resize((int(0.93*scrnw),int(0.93*scrnh)), Image.ANTIALIAS)
mask = Image.open("binaryMask.png")
mask = mask.resize((int(0.93*scrnw),int(0.93*scrnh)), Image.ANTIALIAS)
img = ImageTk.PhotoImage(mask)
canvas = Canvas(root, width = scrnw, height = scrnh)
canvas.pack()

canvas.create_image(scrnw/2,(scrnh/2-int(0.035*scrnh)),anchor='center', image = img)
#root.after(5000, changeImage(img2))
root.mainloop()

