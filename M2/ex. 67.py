print('#'*90)
print('TABUADA (digite qualquer número inteiro NEGATIVO para interromper o programa')
print('#'*90)
while True:
    num = int(input('digite um número para ver sua TABUADA:'))
    print('-'*30)
    if num < 0:
        break
    for c in range(1, 11):
        x = num * c
        print(f'{num} x {c} = {x}')
    print('-'*30)
print('FIM')

