import tkinter as tk
from tkinter import ttk

class Aplicacao(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador_1 = 0
        self.contador_2 = 0
        self.title("Contadores de Cliques")
        self.geometry("250x100")
        self.cria_quadro()

    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.l_contador_1 = ttk.Label(self.quadro,
                                      text=self.formata_contador(1, self.contador_1))
        self.l_contador_1.pack()
        self.botao_1 = ttk.Button(self.quadro,
                                  text="Adiciona ao contador 1",
                                  command=self.conta_1)
        self.botao_1.pack()
        self.l_contador_2 = ttk.Label(self.quadro,
                                      text=self.formata_contador(2, self.contador_2))
        self.l_contador_2.pack()
        self.botao_2 = ttk.Button(self.quadro,
                                  text="Adiciona ao contador 2",
                                  command=self.conta_2)
        self.botao_2.pack()

        self.quadro.pack(expand=True)

    def formata_contador(self, contador, valor):
        return f'Contador {contador}: {valor}'

    def conta_1(self):
        self.contador_1 += 1
        self.l_contador_1["text"] = self.formata_contador(1, self.contador_1)

    def conta_2(self):
        self.contador_2 += 1
        self.l_contador_2["text"] = self.formata_contador(2, self.contador_2)

raiz = Aplicacao()
raiz .mainloop()
