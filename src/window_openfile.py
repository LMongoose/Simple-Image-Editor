# Native Modules
import os, imghdr
import tkinter as tk
from tkinter import messagebox, filedialog
# Downloaded Modules

# Custom Modules
from matrix import Matrix


class FrameOpenFile(tk.Frame):
    def __init__(self, p_parent, p_controller):
        tk.Frame.__init__(self, p_parent)
        self.controller = p_controller
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Label(self, text="Bem vindo ao editor de imagens!").pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Label(self, text="Selecione o arquivo desejado clicando no botão abaixo.").pack(fill=tk.X)
        tk.Button(self, text="Escolha o arquivo", command=self.select_file).pack(fill=tk.X)

    def select_file(self):
        _file = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagem PNG", "png")], initialdir=".")
        _file = _file.replace("/", "\\")
        if((os.path.isfile(_file)) and (imghdr.what(_file) == "png")):
            try:
                self.controller.original_matrix = Matrix.read_from(_file)
            except:
                messagebox.showerror("Erro!", "Houve um erro com a abertura da imagem.")
            else:
                self.next()
        else:
            if(_file != ""):
                messagebox.showerror("Erro!", "O arquivo é inválido!")
                self.select_file()

    def next(self):
        self.controller.show_frame("FrameOptions")