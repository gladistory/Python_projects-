# categorias de natação
n1 = int(input('digite o ano de nascimento '))
n2 = 2019 - n1
print('sua idade é {} anos'.format(n2))
if n2 <= 9:
    print('categoria MIRIM')
elif n2 > 9 and n2 <= 14:
    print('categoria INFANTIL')
elif n2 > 14 and n2 <= 19:
    print('categoria JUNIOR')
elif n2 > 19 and n2 <= 20:
    print('caregoria SENIOR')
elif n2 > 20:
    print('categoria master')