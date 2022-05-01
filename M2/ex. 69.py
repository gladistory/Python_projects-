print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
CM = 0
CF = 0
total = 0
while True:
    print('-'*30)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    print('-'*30)
    print()
    if idade >= 18:
        total += 1
    if sexo == 'M':
        CM += 1
    if sexo == 'F':
        if idade <= 20:
            CF += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print()
print(f'Total de pessoas com mais de 18 anos: {total}')
print()
print(f'Ao todo temos {CM} homens cadastrados;')
print()
print(f'E temos {CF} mulheres com menos de 20 anos.')

