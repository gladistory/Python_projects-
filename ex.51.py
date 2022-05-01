# P.A
n = int(input('primeiro termo:'))
r = int(input('razão:'))
decimo = n + (10 - 1) * r
for c in range(n, decimo, r):
    print(c, end=' ♠ ')
print('ACABOU')
