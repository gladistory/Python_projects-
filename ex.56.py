# analisador
totidade = 0
maioridadehomem = 0
nomevelho = 0
totmulheres = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]: ')).strip()
    totidade += idade
    if p == 1 and sexo in'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulheres += 1
média = totidade / 4
print('A média de idade do grupo é {}'.format(média))
print('O homem mais velho é o {} com {} anos '.format(nomevelho, maioridadehomem))
print('O total de mulheres a baixo dos 20 anos é de {}'.format(totmulheres))
