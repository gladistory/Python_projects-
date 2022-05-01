from time import sleep
print('=-'*20)
print('             BANCO S & S')
print('=-'*20)
while True:
    senha = int(input('digite sua senha:'))
    if senha != 123456:
        print('Acesso negado')
        break
    if senha == 123456:
        print('Liberando acesso .', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.')
    sleep(1)
    print('-'*30)
    valor = int(input('Qual valor deseja sacar ?'))
    total = valor
    céd = 50
    totcéd = 0
    while True:
        if total >= céd:
            total -= céd
            totcéd += 1
        else:
            if totcéd > 0:
                print(f'total de {totcéd} cédulas de {céd} R$')
            if céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 1
            totcéd = 0
            if total == 0:
                break
    cont = str(input('Finalizar operação ? [S/N]')).upper().strip()[0]
    if cont == 'S':
        break
print('Muito obrigado, Volte sempre!')