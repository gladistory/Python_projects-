# soma de numeros pares
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('digite um número:'))
    if n % 2 == 0:
        soma += c
        cont += 1
print('temos {} números pares e a soma deles é {}'.format(cont, soma))
