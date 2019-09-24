# Native Modules
import tkinter as tk
from tkinter import messagebox
# Downloaded Modules

# Custom Modules



class FrameResults(tk.Frame):
    def __init__(self, p_parent, p_controller):
        tk.Frame.__init__(self, p_parent)
        self.controller = p_controller
        tk.Label(self, text="Aqui está sua imagem:").pack(fill=tk.X)
        tk.Label(self, text="Deseja Salvar").pack(fill=tk.X)
        tk.Button(self, text="Salvar", command=self.next_save).pack(fill=tk.X)
        tk.Button(self, text="Não Salvar", command=self.next_nosave).pack(fill=tk.X)
        tk.Button(self, text="Voltar", command=self.back).pack(fill=tk.X)

    def back(self):
        self.controller.show_frame("FrameOptions")

    def next_save(self):
        try:
            _newfilename = "newimage.png"
            self.controller.new_matrix.write_to(_newfilename)
        except:
            messagebox.showerror("Erro!", "Houve um erro com a conversão da imagem para o formato PGM!")
        else:
            messagebox.showinfo("Concluido!", "Sua imagem foi salva com sucesso!")
        self.controller.show_frame("FrameOpenFile")

    def next_nosave(self):
        self.controller.show_frame("FrameOpenFile")