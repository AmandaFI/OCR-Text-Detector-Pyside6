import tkinter as tk

from time import sleep
from PIL import ImageTk, ImageGrab, ImageEnhance


class Image_Area_Selection():

    def __init__(self, darken_img=True):
        self.darken_img = darken_img
        self.roi_image = None
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def on_mouse_down(self, event):
        self.x1 = event.x
        self.y1 = event.y
        self.canvas.create_rectangle(self.x1, self.y1, self.x1, self.y1, outline="red", tag="roi")

    def on_mouse_move(self, event):
        self.x2 = event.x
        self.y2 = event.y
        # remove old overlay image
        self.canvas.delete("roi-image")
        # get the image of selected region
        self.roi_image = self.image.crop((self.x1, self.y1, self.x2, self.y2))
        self.canvas.image = ImageTk.PhotoImage(self.roi_image)
        self.canvas.create_image(
            self.x1, self.y1, image=self.canvas.image, tag=("roi-image"), anchor="nw"
        )
        self.canvas.coords("roi", self.x1, self.y1, self.x2, self.y2)
        # make sure the select rectangle is on top of the overlay image
        self.canvas.lift("roi")

    def select_area(self):
        # hide the root window
        tk.Tk().withdraw()
        sleep(0.3)
        # grab the fullscreen as select region background
        self.image = ImageGrab.grab()
        if self.darken_img:
            # darken the capture image
            bgimage = ImageEnhance.Brightness(self.image).enhance(
                0.3)
        else:
            # darken the capture image
            bgimage = self.image
        # create a fullscreen window to perform the select region action
        win = tk.Toplevel()
        win.attributes("-fullscreen", 1)
        win.attributes("-topmost", 1)
        self.canvas = tk.Canvas(win, highlightthickness=0)
        self.canvas.pack(fill="both", expand=1)
        tkimage = ImageTk.PhotoImage(bgimage)
        self.canvas.create_image(0, 0, image=tkimage, anchor="nw", tag="images")
        # bind the mouse events for selecting region
        win.bind("<ButtonPress-1>", self.on_mouse_down)
        win.bind("<B1-Motion>", self.on_mouse_move)
        win.bind("<ButtonRelease-1>", lambda e: win.destroy())
        # use Esc key to abort the capture
        win.bind("<Escape>", lambda e: win.destroy())
        win.focus_force()
        win.grab_set()
        win.wait_window(win)
        if self.roi_image:
            return self.roi_image
        else:
            return False
