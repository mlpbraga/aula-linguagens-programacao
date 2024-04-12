def tamanhoPalavra(palavra):
    contador = 0
    
    for letra in palavra:
        contador = contador+1

    return contador

print(len('MariaLuisaBraga'))
print(tamanhoPalavra('MariaLuisaBraga'))
