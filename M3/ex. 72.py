n = ['zero', 'um', 'dois', 'três', 'quatro',
     'cinco', 'seis', 'sete', 'oito',
     'nove', 'dez', 'onze', 'doze',
     'treze', 'quatorze', 'quinze', 'dezesseis',
     'dezessete','dezoito', 'dezenove', 'vinte']
while True:
    choice = int(input('Digite um número entre 0 e 20:'))
    if 0 <= choice <= 20:
        print(f'você digitou o número {n[choice].upper()}')
        break
print('FIM')


