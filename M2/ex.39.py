import datetime
nasc = int(input('Qual seu ano de nascimento:'))
data = datetime.date.today().year
idade = (data - nasc)
print('sua idade é de {} anos'.format(idade))
passou = idade - 18
ano1 = data - passou
falta = 18 - idade
ano2 = data + falta
if idade == 18:
    print('hora de se alistar ')
elif idade > 18:
    print('fazem {} anos de seu alistamento, foi no ano de {} '.format(passou, ano1))
elif idade < 18:
    print('faltam {} anos para seu alistamento, previsto para o ano de {}'.format(falta, ano2))
