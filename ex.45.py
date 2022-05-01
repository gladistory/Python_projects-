from time import sleep
from random import randint
print('*'*30)
print('JO KEN PO')
print('*'*30)
itens = ['PEDRA', 'PAPEL','TESOURA']
maquina = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ['PEDRA', 'PAPEL' , 'TESOURA']
jogador = int(input('digite sua opção:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print()
print('a maquina ecolheu {}'.format(itens[maquina]))
print('voce jogou {}'.format(itens[jogador]))
if maquina == 0:
    if jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    elif jogador == 0:
        print('TENTE NOVAMENTE')
elif maquina == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('TENTE NOVAMNETE')
elif maquina == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('TENTE NOVAMENTE')




