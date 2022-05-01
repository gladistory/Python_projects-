print('verifique se está pronto para o alistamento obrigatorio ao exercito')
idade = int(input('digite dua idade'))
n1 = idade - 18
n2 = 18 - idade
if idade == 18:
    print(' está pronto para se alistar')
elif idade > 18:
    print('passou do tempo, extamente {} anos'.format(n1))
elif idade < 18:
    print('faltam {} anos para se alistar'.format(n2))