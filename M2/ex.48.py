soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador = contador + 1
print('A soma dos multiplos de 3 é {}'.format(soma))
print('Sendo {} números multiplos de 3'.format(contador))


