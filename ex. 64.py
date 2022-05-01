print('tratando vários valores ')
x = soma = cont = 0
while not x == 999:
    x = int(input('Digite um número [999 para parar]'))
    if x != 999:
        cont += 1
    if x != 999:
        soma += x
print('foram adicionados {} números e a soma deles é {} '.format(cont, soma))
