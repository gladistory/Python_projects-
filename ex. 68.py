from random import randint
print('-='*20)
print('Vamos jogar PAR OU ÍMPAR ?')
print('-='*20)
v = 0
while True:
    jogador = int(input('escolha um numero de 0 à 10:'))
    computador = randint(0, 11)
    total = jogador + computador
    opt = ' '
    while opt not in 'PI':
        opt = str(input('PAR o IMPAR [P/I]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador} somando temos {total} ')
    if opt == 'P':
        if total % 2 == 0:
            print('Deu PAR, Você venceu!')
            v += 1
        else:
            print('IMPAR, Você perdeu')
            break
    elif opt == 'I':
        if total % 2 == 1:
            print('IMPAR, Você venceu!')
            v += 1
        else:
            print('PAR, você perdeu')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER! você venceu {v} vezes ')


