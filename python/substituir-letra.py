# FAÇA UM PROGRAMA EM PYTHON QUE RECEBA O NOME DO
# USUARIO E A POSICAO EM QUE ELE DESEJA ADICIONAR UMA
# LETRA SE A LETRA QUE ESTIVER NA POSICAO INDICADA FOR
# R,SUBSTITUA POR S SE A LETRA FOR M, SUBSTIITUA POR N
# SENAO FOR NENHUMA DESSAS, REMOVA A LETRA DO NOME
# IMPRIMA NA TELA, A PALAVRA REFORMULADA

# Recebendo o nome do usuário
nome = input("Digite o seu nome: ")

# Recebendo a posição desejada
posicao = int(input("Digite a posição em que deseja adicionar uma letra: ")) - 1  # Ajuste para base 0

# Verificando e modificando a letra na posição indicada
if nome[posicao] == 'R':
    nome = nome[:posicao] + 'S' + nome[posicao+1:]
elif nome[posicao] == 'M':
    nome = nome[:posicao] + 'N' + nome[posicao+1:]
else:
    nome = nome[:posicao] + nome[posicao+1:]
