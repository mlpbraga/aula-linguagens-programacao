def menu():
    print('--------------------')
    print('1. Cadastro')
    print('2. Visualizalizar')
    print('3. Alterar')
    print('4. Remover')
    print('5. Busca')
    print('6. Sair')

def boas_vindas():
    print('--------------------')
    print('Bem vindo ao sistema')
    print('--------------------')

def mostra_alunos():
    tamanho = len(alunos)
    print('----------------------------')
    print('INDICE\tNOME\tIDADE\tTURMA')
    for i in range(tamanho):
        print('----------------------------')
        nome, idade, turma = alunos[i].split(',')
        texto = str(i) + '\t' + nome + '\t' + idade +  '\t' + turma + ''
        print(texto)

def cadastro():
    # cadastro de alunos
    nome = input('nome:')
    idade = input('idade:')
    turma = input('turma:')

    texto =  nome + ',' + idade + ',' +turma
    alunos.append(texto)

alunos = ['Luisa,26,NAI03', 'Luisa,26,NAI03', 'Luisa,26,NAI03', 'CAIO,18,NAI03', 'Luisa,26,NAI03']

boas_vindas()
menu()

comando = input()
while comando != '6':
    if comando == '1':
        cadastro()
    elif comando == '2':
        mostra_alunos()
    elif comando == '3':
        #  alteração de alunos
        # busca = input('nome do aluno:')

        # for aluno in alunos:
        #     if busca in aluno:
        #         posicao = alunos.index(aluno)

        posicao = int(input('posicao:'))
        nome = input('nome:')
        idade = input('idade:')
        turma = input('turma:')
        texto =  nome + ',' + idade + ',' +turma
        alunos[posicao] = texto

    elif comando == '4':
        # remoção de alunos
        pass
    elif comando == '5':
        # busca
        chave = input().upper()
        tamanho = len(alunos)
        print('----------------------------')
        print('INDICE\tNOME\tIDADE\tTURMA')
        for i in range(tamanho):
            if chave in alunos[i].upper():
                print('----------------------------')
                nome, idade, turma = alunos[i].split(',')
                texto = str(i) + '\t' + nome + '\t' + idade +  '\t' + turma + ''
                print(texto)
    
    elif comando == '6':
        print('Até logo!')
    else:
        print('Comando inválido')

    menu()
    comando = input()

print(alunos)
