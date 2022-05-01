print('-='*15)
print('           BOLETIM')
print('-='*15)
ficha = list()
while True:
    nome = str(input('Nome do aluno:'))
    n1 = float(input('NOTA 1:'))
    n2 = float(input('NOTA 2:'))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar ?[S/N]')).upper().split()[0]
    if resp == 'N':
        break
print('-'*26)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')
while True:
    x = int(input('Digite o número do aluno para ver suas notas:'))
    print(f'As notas são: {ficha[x][0]}= {ficha[x][1]}')
    print('-'*35)
    quest = str(input('Deseja ver as notas de outro aluno ? [S/N]')).upper().split()[0]
    print()
    if quest == 'N':
        break
print('-='*30)
print('Obrigado, volte sempre')





