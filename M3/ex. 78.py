listnums = []
maior = 0
menor = 0
for c in range(0, 5):
    listnums.append(int(input(f'Digite um valor na posição {c}:')))
    if c == 0:
        maior = menor = listnums[c]
    else:
        if listnums[c] > maior:
            maior = listnums[c]
        if listnums[c] < menor:
            menor = listnums[c]
print('=-'*20)
print(f'Você digitou os valores {listnums}')
print(f'O maior valor digitado foi {maior}, nas posições', end=' ')
for i, v in enumerate(listnums):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições', end=' ')
for j, k in enumerate(listnums):
    if k == menor:
        print(f'{j}...', end='')
print()

