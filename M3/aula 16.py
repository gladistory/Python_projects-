# () = tuplas : São imutáveis
# , [] = lista,
# {} = dicionário
# sorteio de nomes:
listnum = []
while True:
    listnum.append(int(input('adicione números a lista:')))
    choice = str(input('Deseja continuar ?[S/N]')).upper().strip()[0]
    if choice == 'N':
        break
print(f'os números adicionados foram: {listnum}')
