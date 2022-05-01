list = []
while True:
    list. append(int(input('Digite um valor:')))
    resp = str(input('Deseja continuar ?[S/N]')).upper().split()[0]
    if resp == 'N':
        break
list.sort(reverse= True)
print(f'Foram adicionados {len(list)} valores a lista')
print(f'Os valores ordenados de forma decrescente ficam: {list}')
if 5 in list:
    print('O valor 5 foi adicionado a lista')
else:
    print('O valor 5 não foi adcionado na lista')