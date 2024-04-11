#faça um programa em python que receba 10 notas do usuário
#guarde em uma lista e tire a média dessas notas
#no final o programa deve imprimir se o aluno foi aprovado
#ou não, considerando que a média é 7

notas = []

for i in range(0, 10):
    nota = float(input('nota['+str(i)+']:'))
    notas.append(nota)

soma = sum(notas)

media = soma / len(notas)

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
