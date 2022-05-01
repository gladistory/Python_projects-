# estruturas condicionais aninhadas, usando os comandos if.. elif.. else
# para criar diversos blocos, podemos aplicar vários elif dentro de um if, não é possível usar elif sem if.
# o else ele pode ser usado uma ou nehuma vez.

# CONDIÇÃO SIMPLES EX:
'''nome = str(input('nome:'))
if nome == 'vini':
    print('que nome foda!')
print(f'tenha um bom dia {nome}')
print()'''

# CONDIÇÃO COMPOSTA EX:
'''nome = str(input('nome:'))
if nome == "vini":
    print('belo nome!')
else:
    print("seu nome é bem bosta")
print(f"tenha um mal dia {nome}")
print()'''

# CONDIÇÃO ANINHADA EX:
'''nome = str(input('nome:'))
if nome == "vini":
    print('que nome foda!')
elif nome == "paulo" or nome == "fabio" or nome == "gabi" or nome == "edu":
    print('que nome normal')
else:
    print('que nome bosta')
print(f'tenha um bom dia {nome}')'''


