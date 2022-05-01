n1 = float(input('digite a primeira nota'))
n2 = float(input('digite a segunda nota'))
n3 = float(input('digite a terceira nota'))
media = (n1 + n2 +n3 ) / 3
print('sua media foi {}'.format(media))
if media < 5:
    print('reprovado')
elif media >= 5 or media <= 6.9:
    print('recurperaçao')
elif media > 6.9:
    print('aprovado')