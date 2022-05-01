from time import sleep
print('CALCULADORA DE IMC')
print()
peso = float(input('Qual seu peso ? (Kg)'))
altura = float(input('Qual sua altura ? (m)'))
imc = peso / (altura)**2
print()
print('PROCESSANDO ...')
sleep(2)
print('seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO do peso')
elif 18.5 <= imc < 25:
    print('Peso IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBSIDADE')
elif imc >= 40:
    print('OBSIDADE MÓRBIDA')

