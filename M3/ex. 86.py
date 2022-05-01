numbers = list()
line1 = list()
line2 = list()
line3 = list()
par = list()
impar = list()
for c in range(0, 3):
    numbers.append(int(input(f'Digite um valor para [0, {c}]:')))
    line1.append(numbers[:])
    numbers.clear()
for c in range(0, 3):
    numbers.append(int(input(f'Digite um valor para [1, {c}]:')))
    line2.append(numbers[:])
    numbers.clear()
for c in range(0, 3):
    numbers.append(int(input(f'Digite um valor para [2, {c}]')))
    line3.append(numbers[:])
    numbers.clear()
for p in line1:
    print(f'[ {p[0]:^5} ]', end=' ')
print()
for d in line2:
    print(f'[ {d[0]:^5} ]', end=' ')
print()
for f in line3:
    print(f'[ {f[0]:^5} ]', end=' ')
print()
print(par, impar)
