# numeros primos
n = int(input('digite um número:'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ♣ ')
        tot += 1
    else:
        print('\033[31m', end=' ♦ ')
    print('{}'.format(c), end= ' ')
print('\n\033[36m O número {} foi divisivel por {} vezes '.format(n, tot))
if tot == 2:
    print('é primo pois é divido por apenas dois números')
else:
    print('não é primo')
