# calculadora imc
peso = float(input('digíte seu peso(em kg)'))
altura = float(input('digíte sua altura(em metros)'))
imc = peso / (altura * altura)
print('seu imc é de {}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('obsidade')
elif imc > 40:
    print('obsidade mórbida')
