primeiro = int(input('primeiro termo:'))
razao = int(input('razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ♠ '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Gostaria de ver mais quantos termos ? '))
print('progressão foi de  {} termos'.format(total))


