print('-'*30)
print('       Loja do vini')
print('-'*30)
menor = tot = mm = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto:'))
    valor = float(input('Valor do produto:'))
    cont += 1
    resp = ' '
    tot += valor
    if valor >= 1000:
        mm += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('------- FIM DO PROGRAMA -------')
print(f'valor da compra foi de {tot:.2f} R$')
print(f'temos {mm} produtos custando mais de 1000 R$')
print(f'O produto mais barato foi {barato} que custa {menor:.2f} R$')