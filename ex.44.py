# condiçoes de pagamento
nome = str(input('digite seu nome:'))
senha = int(input('digite sua senha'))
if senha == 1234:
    print('acesso liberado')
    print('você esta na pagina de pagamentos e seram fornecidas as opções')
    preço = float(input('digite o valor do produto'))
    c1 = preço - (preço * 0.1)
    c2 = preço - (preço * 0.05)
    c3 = preço + (preço * 0.2)
    print('1- a vista ou no cheque o produto terá um desconto de 10% e seu valor será de {}R$'.format(c1))
    print('2- a vista no cartão o produto terá  5% de desconto e seu valor será de {}R$'.format(c2))
    print('3- até 2x no cartão o preço será normal de {}R$'.format(preço))
    print('4- em 3x ou mais o valor sairá com juros de 20%, saindo a {}'.format(c3))
    pagamento = float(input('digite 1, 2, 3 ou 4 para selecionar uma das opções a cima'))
    if pagamento == 1:
        print('o pagamento será a vista ou no cheque com valor de {}'.format(c1))
    elif pagamento == 2:
        print('o pagamento será a vista no cartão com valor de{}'.format(c2))
    elif pagamento == 3:
        print('o pagamento será em 2x no cartão com valor de {}'.format(preço))
    elif pagamento == 4:
        print('o pagamento será em 3x ou mais no cartão com valor de {}'.format(c3))
    print('muito obrigado e volte sempre ')
else:
    print('acesso negado')
