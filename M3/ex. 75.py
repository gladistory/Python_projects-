n1 = int(input('digite um número:'))
n2 = int(input('digite outro número:'))
n3 = int(input('digite mais um número:'))
n4 = int(input('digite o último número:'))
nd = (n1, n2, n3, n4)
print(f'Você digitou os números {nd}')
print(f'O valor 9 apareceu {nd.count(9)} vezes')
if 3 in nd:
    print(f'O valor 3 está na {nd.index(3) + 1}ª posição')
else:
    print('O valor 3 nao foi digitado')
print(f'O números pares são: ')
for n in nd:
    if n % 2 == 0:
        print(n, end=' ')
