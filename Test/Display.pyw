from tkinter import *
from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, titl, master=None):
        Frame.__init__(self, master, width=1000, height=1000)
        self.grid()

        self.master.title(titl)
        self.master.configure(background='green')
        self.master.wm_attributes("-transparentcolor", "green")
        self.master.call('wm', 'attributes', '.', '-topmost', True)

        image_file = 'test1.bmp'
        image1 = ImageTk.PhotoImage(Image.open(image_file))
        self.image1 = image1
        self.master.attributes("-fullscreen", True)
        self.w = image1.width()
        self.h = image1.height()
        self.create_widgets()

    def create_widgets(self):
        image1 = self.image1
        w = self.w
        h = self.h
        self.canvas = Canvas(self, width=w, height=h, bd=0, highlightthickness=0)
        self.canvas.grid(row=1, column=1)
        self.canvas.create_image(w/2,h/2, image=image1)
        self.canvas.image = image1
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)

app = Application('Image')

app.mainloop()
