cont = soma = 0
while True:
    num = int(input('digite um número (999 para parar) :'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'foram adicionado {cont} valores e a soma deles é  {soma}')
