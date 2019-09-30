# Native Modules
import tkinter as tk
from tkinter import messagebox
# Downloaded Modules

# Custom Modules



class FrameSave(tk.Frame):
    def __init__(self, p_parent, p_controller):
        tk.Frame.__init__(self, p_parent)
        self.controller = p_controller
        tk.Label(self, text="Digite o nome de arquivo para salvar sua imagem.").pack(fill=tk.X)
        tk.Label(self, text="(a extensão será adicionada automaticamente)").pack(fill=tk.X)
        self.txtbox = tk.Entry(self)
        self.txtbox.pack(fill=tk.X)
        tk.Button(self, text="Salvar", command=self.next).pack(side="left")
        tk.Button(self, text="Voltar", command=self.back).pack(side="left")

    def validate_filename(self):
        _filename = self.txtbox.get()
        for char in _filename:
        	if (char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_()[] "):
        		return False
        return True

    def back(self):
        self.controller.show_frame("FrameResults")

    def next(self):
        try:
            if(self.validate_filename()):
                self.controller.new_matrix.write_to(self.txtbox.get()+".png")
            else:
                messagebox.showerror("Erro!", "Você digitou um nome de arquivo inválido!")
        except:
            messagebox.showerror("Erro!", "Houve um erro com a criação da nova imagem!")
        else:
            messagebox.showinfo("Concluido!", "Sua nova imagem foi salva com sucesso!")
        self.controller.show_frame("FrameOpenFile")