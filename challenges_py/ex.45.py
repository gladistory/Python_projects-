#game : jo ken po
from random import randint
itens = ( 'pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('[0] = pedra')
print('[1] = papel')
print('[2] = tesoura')
jogada = int(input('digite o valor referente a sua jogada'))
print()