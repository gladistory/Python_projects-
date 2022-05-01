dados = list()
grupo = list()
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome:')))
    dados.append((float(input('Digite seu peso(Kg):'))))
    if len(grupo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    grupo.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
    while resp not in 'SN':
        resp = str(input('Não entendi ! Deseja continuar ? [S/N]')).upper().strip()[0]
print(f'Foram cadastradas {len(grupo)} pessoas')
print(f'O maior peso foi {maior} Kg. Peso de', end=' ')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor} Kg. Peso de', end=' ')
for p in grupo:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')



