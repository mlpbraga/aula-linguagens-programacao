import tkinter as tk
from tkinter import ttk

contador_1 = 0
contador_2 = 0

def formata_contador(contador, valor):
    return f'Contador {contador}: {valor}'

def conta_1():
    global contador_1, l_contador_1
    contador_1 += 1
    l_contador_1["text"] = formata_contador(1, contador_1)

def conta_2():
    global contador_2, l_contador_2
    contador_2 += 1
    l_contador_2["text"] = formata_contador(2, contador_2)

raiz = tk.Tk()
raiz.title("Contadores")
raiz.geometry("250x100")
quadro = ttk.Frame(raiz)

l_contador_1 = ttk.Label(quadro, text=formata_contador(1, contador_1))
l_contador_1.pack()
botao_1 = ttk.Button(quadro, text="Adiciona ao contador 1", command=conta_1)
botao_1.pack()

l_contador_2 = ttk.Label(quadro, text=formata_contador(2, contador_2))
l_contador_2.pack()
botao_2 = ttk.Button(quadro, text="Adiciona ao contador 2", command=conta_2)
botao_2.pack()

quadro.pack(expand=True)
raiz.mainloop()
