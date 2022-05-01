p1 = int(input('digite o primeiro valor:'))
p2 = int(input('digite o segundo valor:'))
fim = 0
while not fim == 5:
    soma = p1 + p2
    multiplicar = p1 * p2
    print('=/='*30)
    print('''
              [1] - Somar
              [2] - Multiplicar
              [3] - Maior
              [4] - Novos números
              [5] - Sair do programa
              ''')
    print('=/='*30)
    print()
    fim = int(input('escolha uma opção:'))
    print()
    if fim == 1:
        print('A soma ente {} e {} é {}'.format(p1, p2, soma))
        print('-'*30)
    if fim == 3:
        if p1 > p2:
            print('{} é maior que  {}'.format(p1, p2))
            print('-'*30)
        else:
            print('{} é maior que {}'.format(p2, p1))
            print('-'*30)
    if fim == 2:
        print('{} X {} = {}'.format(p1, p2, multiplicar))
        print('-'*30)
    if fim == 4:
        p1 = int(input('digite um novo valor:'))
        p2 = int(input('digite um novo valor:'))
    if fim > 5:
        print('ação inválida, tente novamente ')
print('Finalizado')

