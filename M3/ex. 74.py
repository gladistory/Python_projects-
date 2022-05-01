from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=', ')
print()
print(f'\nO maior valor foi: {max(numeros)}')
print()
print(f'O menor valor foi: {min(numeros)}')

