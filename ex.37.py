# conversão de bases numéricas
num = int(input('DIGITE UMA NÚMERO QUALQUER:'))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO: )
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL ''')

opção = int(input('sua opção:'))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção inválida, tente novamente')
