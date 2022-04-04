import matplotlib.pyplot as plt
from time import sleep
print()
print(' EXP- 2 -DETERMINAÇÃO DA VELOCIDADE DE REAÇÃO DE HIDRÓLISE,')
print(' BÁSICA DO ACETATO DE ETILA SEGUIDA POR CONDUTÂNCIA')

print('-='*30)

print('\nCálculo do eixo Y para seguintes temperaturas: 23.7, 32.6, 41°C;')

print('OBS: Y = L∞ - Lo/a(L∞ - Lt) ')
print('L∞ = Condutividade ao fim da reação; ')
print('Lo = Condutividade ao misturar os dois reagentes;')
print('a = Concentração da base após a mistura dos reagentes;')
print('Lt = Condutividade medida durante os tempos t')
print()
t = 0
temp = [23.7, 32.6, 41]
while t not in temp:
    t = float(input('Em qual temperatura deseja calcular?'))
    if t not in temp:
        print()
        print('Apenas para 23.7, 32.6, 41°C ')
        print('-'*30)
        print()
    dados = list()
    valorLt = list()
    print('-='*20)
    if t == 23.7:
        for c in range(0, 11):
            lt = float(input(f'digite o valor de Lt {c} (condutividade ):'))
            y = -2.17 / (0.02 * (2.65 - lt))
            dados.append(y)
            valorLt.append(lt)
    elif t == 32.6:
        for c in range(0, 11):
            lt = float(input(f'digite o valor de Lt {c} (valores da condutividade):'))
            y = -2.5 / (0.02 * (2.89 - lt))
            dados.append(y)
            valorLt.append(lt)
    elif t == 41:
        for c in range(0, 11):
            lt = float(input(f'digite o valor de Lt {c} (valores da condutividade):'))
            y = -2.55 / (0.02 * (3.09 - lt))
            dados.append(y)
            valorLt.append(lt)
print('\n-='*20)
print('Gerando dados', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print('VALORES ADICIONADOS DE Lt:')
for t, p in enumerate(valorLt):
    print(f'Lt {t} = {p}')
print("-="*20)
sleep(1)
print('RESULTADO DOS VALORES DE Y:')
for k, d in enumerate(dados):
    print(f'Y {k} = {d:.3f}')
print("-="*20)
sleep(1)
print(f'O MAIOR valor de Y é :{max(dados):.3f}')
print(f'O MENOR valor de Y é: {min(dados):.3f}')
print(f"A MÉDIA dos valores de Y é: {sum(dados) / 11:.3f}")
print(f'MÉDIA dos valores de Lt adicionados: {sum(valorLt) / 11:.3f}')
print('-='*20)
sleep(1.5)
eixo_x = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
plt.plot(eixo_x, dados)
plt.ylabel("L∞- Lo/a(L∞ - Lt)")
plt.xlabel("Tempo(min.)")
plt.show()

