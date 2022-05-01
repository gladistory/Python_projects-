valores = list()
ímpares = list()
pares = list()
while True:
    valores.append(int(input('Digite um valor:')))
    resp = str(input('Deseja continuar ?[S/N]')).upper().split()[0]
    while resp not in 'SN':
        resp = str(input('Não entendi, deseja continuar ?[S/N]')).upper().split()[0]
    if resp == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'A lista completa é : {valores}')
print(f'A lista com números pares: {pares}')
print(f'A lista com números ímpares: {ímpares}')


