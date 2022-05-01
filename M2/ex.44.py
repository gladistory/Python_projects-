from time import sleep
print('============== LOJA QUÍMICOS S.S ============')
print('Simulador de formas de pagamento')
print()
senha = int(input('Digite a senha de acesso:'))
if senha == 123456:
    print('Verificando ...')
    sleep(2)
    print()
    print('ACESSO LIBERADO')
    print()
    valor = float(input('digite o valor da compra:'))
    print('''FORMAS DE PAGAMENTO:
    [1]- à vista DINHEIRO/CHEQUE
    [2]- à vista CARTÃO
    [3]- 2X no cartão
    [4]- 3X ou mais no cartão''')
    print()
    option = int(input('escolha uma das opções:'))
    print()
    op1 = valor - (valor * 10)/ 100
    op2 = valor - (valor * 5)/ 100
    op3 = valor
    op4 = valor + (valor * 20)/ 100
    if option == 1:
        print('O valor da compra será de {:.2f} R$'.format(op1))
    elif option == 2:
        print('O valor da compra será de {:.2f} R$'.format(op2))
    elif option == 3:
        print('O valor da compra será de {:.2f} R$'.format(op3))
    elif option == 4:
        print('O valor da compra será de {:.2f} R$'.format(op4))
else: print('ACESSO NEGADO')

