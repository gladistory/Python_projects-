casa = float(input('qual o valor da casa ?'))
salario = float(input('qual valor de sua renda mensal ?'))
ano = int(input('em quantos anos deseja pagar ?'))
prestacao = casa / (12 * ano)
n1 = salario * 0.3
if prestacao > n1:
    print('emprestimo negado')
else:
    print('emprestimo aceito')
    print('o valor da prestação é de {}R$'.format(prestacao))