print('Sequência de Fibonacci')
print('=-'*15)
n1 = int(input('quantos termos você quer mostar ?'))
p1 = 0
p2 = 1
cont = 3
print('{} ♠ {}'.format(p1, p2), end=' ')
while cont <= n1:
    p3 = p1 + p2
    print('♠ {} '.format(p3), end=' ')
    cont += 1
    p1 = p2
    p2 = p3
print('FIM')