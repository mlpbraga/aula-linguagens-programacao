# Abrindo um arquivo para escrita (o arquivo é criado se não existir)
with open('exemplo.txt', 'w') as file:
    file.write("Olá, mundo!\n")
    file.write("Esta é nossa primeira linha de texto.\n")

# Abrindo um arquivo para adicionar conteúdo ao final (append)
with open('exemplo.txt', 'a') as file:
    file.write("Adicionando uma nova linha ao arquivo existente.\n")
