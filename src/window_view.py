# Native Modules
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
# Downloaded Modules

# Custom Modules



class FrameResults(tk.Frame):
    def __init__(self, p_parent, p_controller):
        tk.Frame.__init__(self, p_parent)
        self.controller = p_controller
        self.newfilename = "tempimg.png"
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.bind("<Configure>", self.resize)
        self.loadimg()
        tk.Label(self, text="Deseja Salvar").pack(fill=tk.X)
        tk.Button(self, text="Salvar", command=self.next_save).pack(fill=tk.X)
        tk.Button(self, text="Não Salvar", command=self.next_nosave).pack(fill=tk.X)
        tk.Button(self, text="Voltar", command=self.back).pack(fill=tk.X)

    def loadimg(self):
        try:
            self.img = ImageTk.PhotoImage(Image.open(self.newfilename))
        except:
            pass
        else:
            self.canvas_img = self.canvas.create_image(0, 0, anchor="nw", image=self.img)

    def canvas_update(self):
        try:
            self.controller.new_matrix.write_to(self.newfilename)
        except:
            tk.Label(self, text="Houve um erro com a renderização da nova imagem!")
        else:
            self.loadimg()
        finally:
            try:
                os.remove(self.newfilename)
            except:
                pass

    def resize(self, event):
        try:
            img = Image.open(self.newfilename).resize((event.width, event.height), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(img)
        except:
            pass
        else:
            self.canvas.itemconfig(self.canvas_img, image=self.img)

    def back(self):
        self.controller.show_frame("FrameOptions")

    def next_save(self):
        self.controller.show_frame("FrameSave")

    def next_nosave(self):
        self.controller.show_frame("FrameOpenFile")