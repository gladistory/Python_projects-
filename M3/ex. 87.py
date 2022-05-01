from time import sleep
from random import randint
print('-'*30)
print('      JOGA NA MEGA SENA')
print('-'*30)
nsort = int(input('Quantos jogos deseja fazer ?'))
jogos = list()
tot = 1
lista = list()
while tot <= nsort:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('-='*3, 'SORTEANDO JOGOS', '=-'*3)
for i, l in enumerate(jogos):
    sleep(0.5)
    print(f'jogo {i + 1}: {l}')
print('-='*30)



