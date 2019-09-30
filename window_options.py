# Native Modules
import tkinter as tk
# Downloaded Modules

# Custom Modules
from matrix import Matrix


class FrameOptions(tk.Frame):
    def __init__(self, p_parent, p_controller):
        tk.Frame.__init__(self, p_parent)
        self.controller = p_controller
        tk.Label(self, text="Clique em uma opção para adicioná-la à sequência.").pack(fill=tk.X)
        tk.Label(self, text="Clique em Aplicar para iniciar a edição.").pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Button(self, text="Opção 1 - Remover as linhas e colunas ímpares.", command=lambda: self.options_append("1")).pack(fill=tk.X)
        tk.Button(self, text="Opção 2 - Remover as células com valores ímpares.", command=lambda: self.options_append("2")).pack(fill=tk.X)
        tk.Button(self, text="Opção 3 - Remover as linhas e colunas impares e as células com valores pares.", command=lambda: self.options_append("3")).pack(fill=tk.X)
        tk.Button(self, text="Opção 4 - Adicionar 10 ao valor das células.", command=lambda: self.options_append("4")).pack(fill=tk.X)
        tk.Button(self, text="Opção 5 - Subtrair 10 do valor das células.", command=lambda: self.options_append("5")).pack(fill=tk.X)
        tk.Button(self, text="Opção 6 - Inverter o valor das células.", command=lambda: self.options_append("6")).pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Label(self, text="Sequência de opções:").pack(fill=tk.X)
        self.txtbox = tk.Entry(self)
        self.txtbox.pack(fill=tk.X)
        tk.Label(self, text="").pack(fill=tk.X)
        tk.Button(self, text="Remover última", command=self.options_pop).pack(side="left")
        tk.Button(self, text="Aplicar", command=self.next).pack(side="left")
        tk.Button(self, text="Voltar", command=self.back).pack(side="left")

    def options_append(self, p_option):
        self.txtbox.insert(tk.END, p_option)

    def options_pop(self):
        self.txtbox.delete(len(self.txtbox.get())-1, tk.END)

    def back(self):
        self.controller.show_frame("FrameOpenFile")

    def next(self):
        _matrix = self.controller.original_matrix

        for option in self.txtbox.get():
            if(option == "1"):
                _matrix = _matrix.option1()
            elif(option == "2"):
                _matrix = _matrix.option2()
            elif(option == "3"):
                _matrix = _matrix.option3()
            elif(option == "4"):
                _matrix = _matrix.option4()
            elif(option == "5"):
                _matrix = _matrix.option5()
            elif(option == "6"):
                _matrix = _matrix.option6()
        self.controller.new_matrix = _matrix

        self.controller.frames["FrameResults"].canvas_update()
        self.controller.show_frame("FrameResults")