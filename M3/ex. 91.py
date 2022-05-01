from random import randint
from time import sleep
from operator import itemgetter
print('Sorteando valores aleatórios em  um dado de 6 lados para 4 jogadores:')
dados = dict()
for c in range(0, 4):
    x = randint(1, 6)
    dados[f'Jogador {c + 1}'] = x

for k, v in dados.items():
    print(f'{k}: número sorteado = {v}')
    sleep(1)
ranking = list()
print()
print('=-'*15)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i + 1}º lugar: {v[0]}: com {v[1]} pontos')









