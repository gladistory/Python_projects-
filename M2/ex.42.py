# simbolo de diferente de:  !=
print('TIPOS DE TRIÂNGULOS')
l1 = float(input('primeiro lado:'))
l2 = float(input('segundo lado:'))
l3 = float(input('terciro lado:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('é possivel formar um triângulo', end='')
    if l1 == l2 == l3:
        print(' equilátero')
    elif l1 == l2:
        print(' isóceles')
    elif l1 == l3:\
        print(' isóceles')
    elif l2 == l3:
        print(' isóceles')
    else:
        print(' escaleno')
else:
    print('não é possivel formar um triângulo')
