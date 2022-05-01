print('Média e menor e maior valor')
n = soma = cont = maior = menor = 0
x = 'S'
while x in 'Ss':
    n = float(input('Digite um número:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    x = str(input('Deseja continuar ?[S/N]')).upper().strip()[0]
média = soma / cont
print('foram adicionados  {} números, a média entre eles é {:.2f}'.format(cont, média))
print('o maior número é {} e o menor {}'.format(maior, menor))
