# !pip install --update gspread

from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())

# passo 1
projeto_x = gc.open('projeto 1')

# passo 2
page_one = projeto_x.sheet1

# passo 3
from time import sleep
print()
print(' EXP- 2 -DETERMINAÇÃO DA VELOCIDADE DE REAÇÃO DE HIDRÓLISE,')
print(' BÁSICA DO ACETATO DE ETILA SEGUIDA POR CONDUTÂNCIA')
print('-='*30)
print('Cálculo do eixo Y para seguintes temperaturas: 23.7, 32.6, 41°C;')
print()
print('OBS: Y = L∞ - Lo/a(L∞ - Lt) ')
print('L∞ = Condutividade ao fim da reação; ')
print('Lo = Condutividade ao misturar os dois reagentes;')
print('a = Concentração da base após a mistura dos reagentes;')
print('Lt = Condutividade medida durante os tempos t')
print()
t = 0
temp = [24.2, 32.6, 45]

# Passo 4
while t not in temp:
    t = float(input('Em qual temperatura deseja calcular?'))
    if t not in temp:
        print()
        print('Apenas para 24.2, 32.6, 45°C ')
        print('-'*30)
        print()
    dados = list()
    valorLt = list()
    print('-='*20)
    if t == 24.2:
        for c in range(0, 11):
            lt = float(input(f'digite o valor de Lt {c} (condutividade ):'))
            y = -2.12 / (0.02 * (2.25 - lt))
            dados.append(y)
            valorLt.append(lt)
    elif t == 32.6:
        for c in range(0, 11):
            lt = float(input(f'digite o valor de Lt {c} (valores da condutividade):'))
            y = -2.82 / (0.02 * (2.62 - lt))
            dados.append(y)
            valorLt.append(lt)
    elif t == 45:
        for c in range(0, 11):
            lt = float(input(f'digite o valor de Lt {c} (valores da condutividade):'))
            y = -2.73 / (0.02 * (3.13 - lt))
            dados.append(y)
            valorLt.append(lt)
print()
print('-='*20)

# passo 5
page_one.update_acell('A1', 'tempo(min)')
page_one.update_acell('B1', 'L - L0a(L - Lt)')

eixo_x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for c in range(1, 12):
    coluna_1 = f'A{c + 1}'
    page_one.update_acell(coluna_1, eixo_x[c - 1])

for c in range(1, 12):
    coluna_2 = f'B{c + 1}'
    page_one.update_acell(coluna_2, dados[c - 1])

for c in range(1, 12):
    coluna_3 = f'C{c + 1}'
    page_one.update_acell(coluna_3, c - 1)
