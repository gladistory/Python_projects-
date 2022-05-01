import time
from random import randint
maquina = randint(0,10)
print('*'*20)
print('JOGO DA ADIVINHAÇÃO ')
print('*'*20)
print()
print('SOU SEU COMPUTADOR...')
time.sleep(2)
print('ESCOLHI UM NÚMERO ENTRE 0 E 10')
time.sleep(2)
print('DESAFIO VOCÊ A ADIVINHAR ESSE NÚMERO')
time.sleep(2)
print('1')
time.sleep(1)
print('2')
time.sleep(1)
print('3')
time.sleep(1)
print('VALENDO!!!')
acertou = False
palpites = 0
while not acertou:
    numero = int(input('Digite um número entre 0 e 10:'))
    palpites += 1
    if numero < maquina:
        print('Mais... Tente novamente ')
    if numero > maquina:
        print('Menos ... Tente novamente')
    if numero == maquina:
        acertou = True
print('ACERTOU !!!')
print('Você precisou de {} palpites para acertar'.format(palpites))