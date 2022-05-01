from datetime import date
atual = date.today().year
nasc = int(input('digite o seu ano de nascimento:'))
idade = atual - nasc
print('''temos as seguintes categorias:
[1]- até 9 anos: MIRIM
[2]- até 14 anos: INFANTIL
[3]- até 19 anos: JUNIOR
[4]- até 25 anos: SÊNIOR
[5]- acima de 25 anos: MASTER''')
print('sua IDADE é de {}'.format(idade))

if 7 < idade <= 9:
    print('categoria MIRIM')
elif 9 < idade <= 14:
    print('Categoria INFANTIL')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade <= 25:
    print('Categoria SÊNIOR ')
elif idade > 25:
    print('Categoria MASTER')