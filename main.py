# Native Modules
import tkinter as tk
# Downloaded Modules

# Custom Modules
from window_openfile import FrameOpenFile
from window_options import FrameOptions
from window_view import FrameResults
from window_save import FrameSave

## TODO: add method to create and delete each frame to reload when needed

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Editor de Imagens")
        self.geometry("420x400")
        self.iconbitmap("icon1.ico")
        self.resizable(width=False, height=False)

        # Application Shared Variables
        self.options_sequence = ""
        self.original_matrix = None
        self.new_matrix = None

        # Frame container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for page in (FrameOpenFile, FrameOptions, FrameResults, FrameSave):
            frame = page(self.container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            page_name = page.__name__
            self.frames[page_name] = frame
        self.show_frame("FrameOpenFile")

    def show_frame(self, page_name):
        self.frames[page_name].tkraise()

if(__name__ == "__main__"):
    app = Application()
    app.mainloop()