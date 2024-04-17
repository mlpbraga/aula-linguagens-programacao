from datetime import datetime

with open('info.txt', 'w') as arquivo:
    arquivo.write('Maria Luisa Braga\n')
    hoje = datetime.now().strftime('%d/%m/%Y')
    arquivo.write(hoje)
    arquivo.write('\t')
    arquivo.write('MANAUS-AM\n')
    arquivo.write('26')
    arquivo.write('\t')
    arquivo.write('DISTRITO\n')
