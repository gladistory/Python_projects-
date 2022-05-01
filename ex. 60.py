from math import factorial
n1 = int(input('digite um número para saber seu fatorial :'))
c = n1
f = factorial(n1)
print('Calculando {}! = '.format(n1), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' X ' if c > 1 else '=', end='')
    c -= 1
print(' {}'.format(f), end='' )


