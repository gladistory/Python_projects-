listagem = ('Lápis', 1.50,
            'Borracha', 2,
            'Caderno', 20.50,
            'Mochila', 120.35,
            'Estojo', 10)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='*40)
