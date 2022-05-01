# Podemos organizar as listas da seguinte forma:
# núm = [[], []]
# valor = 0
# for c in range(1, 8):
#   valor = int(input(f'Digite o {c}º valor'))
#   if valor % 2 == 0:
#       num[0].append(valor)
#   else:
#        num[1].append(valor)
valores = list()
grupo = list()
par = list()
impar = list()
test = []
for c in range(0, 7):
    valores.append(int(input(f'Digite o {c + 1}º valor:')))
    grupo.append(valores[:])
    valores.clear()
for p in grupo:
    if p[0] % 2 == 0:
        par.append(p[0])
for p in grupo:
    if p[0] % 2 == 1:
        impar.append(p[0])
test.append(par)
test.append(impar)
test[0].sort()
test[1].sort()
print(f'Os valores ímpares são: {test[1]}')
print(f'Os valores pares são: {test[0]}')





