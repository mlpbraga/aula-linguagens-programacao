# Importação de módulos necessários
import os

# Introdução à Manipulação de Arquivos
print("Bem-vindo à aula sobre Manipulação de Arquivos!")
print("Hoje, aprenderemos como abrir, ler, escrever e manipular diferentes tipos de arquivos em Python.\n")

# Abrindo e Lendo Arquivos
# Caminho do arquivo a ser lido
file_path = 'exemplo.txt'

# Abrindo o arquivo em modo de leitura
with open(file_path, 'r') as file:
    # Lendo todo o conteúdo do arquivo
    content = file.read()
    print("Conteúdo do arquivo 'exemplo.txt':")
    print(content)

# Explorando os métodos read, readline e readlines
with open(file_path, 'r') as file:
    print("\nPrimeira linha do arquivo:")
    first_line = file.readline()
    print(first_line.strip())

    print("\nLista de todas as linhas restantes do arquivo:")
    all_lines = file.readlines()
    for line in all_lines:
        print(line.strip())
