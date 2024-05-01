import tkinter as tk
from tkinter import ttk

class Aplicacao(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Calculadora de IMC")
        self.geometry("300x150")
        self.cria_quadro()

    def cria_quadro(self):
        self.quadro = ttk.Frame(self)

        # Entradas para peso e altura
        self.l_peso = ttk.Label(self.quadro, text="Peso (kg):")
        self.l_peso.pack()

        self.e_peso = ttk.Entry(self.quadro)
        self.e_peso.pack()

        self.l_altura = ttk.Label(self.quadro, text="Altura (m):")
        self.l_altura.pack()

        self.e_altura = ttk.Entry(self.quadro)
        self.e_altura.pack()

        # Botão para calcular IMC
        self.botao_imc = ttk.Button(self.quadro, text="Calcular IMC", command=self.calcula_imc)
        self.botao_imc.pack()

        # Label para exibir o resultado do IMC
        self.l_resultado = ttk.Label(self.quadro, text="")
        self.l_resultado.pack()

        self.quadro.pack(expand=True)

    def calcula_imc(self):
        try:
            peso = float(self.e_peso.get())
            altura = float(self.e_altura.get())
            imc = peso / (altura ** 2)
            self.l_resultado["text"] = f"IMC: {imc:.2f}"
        except ValueError:
            self.l_resultado["text"] = "Entradas inválidas!"

# Inicia a aplicação
raiz = Aplicacao()
raiz.mainloop()
