def tamanho_lista(lista):
    contador = 0
    for elemento in lista:
        contador +=1
    return contador

def tamanho_lista_palavras(lista_palavras):
    qtd_palavras = tamanho_lista(lista_palavras)
    print('quantidade de palavras na lista:', qtd_palavras)
    posicao = 1
    for palavra in lista_palavras:
        print('quantidade de letras na palavra', posicao,':', tamanho_lista(palavra) )
        posicao += 1

lista_palavras = ["oii", "tudo bem", "tchau", "?", "não"]
tamanho_lista_palavras(lista_palavras)
