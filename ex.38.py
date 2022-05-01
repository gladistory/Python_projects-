# analise numérica
print('-='*15)
print('teste dos números')
print('-='*15)
n1 = int(input('digíte o primeiro número'))
n2 = int(input('digíte o segundo número'))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
elif n2 < n1:
    print('{} é menor que {}'.format(n2, n1))
else:
    print(' são iguais')