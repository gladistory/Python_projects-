# dicionários são representados por :
# var = {}
# value = dict()
# funcionam de forma semaelhante a listas e tuplas, porém, podemos
# usar nomes ao invés de números para separar os elementos do dic.

''' var = {'nome': 'pedro', 'idade': 21}
print(var['nome'], var['idade'])'''

#para adcionar elementos ao dic. nao usamos append:

'''var = {'nome': 'vini'}
var['idade'] = 20
print(f'{var["nome"]} tem {var["idade"]} anos')'''

# Para remover uma estrutura usamos: del

'''var = {'nome':'vini', 'idade': 20}
del var['idade']
print(var)'''

# os elementos dentro do dic. ex: nome e idade, o python chama de keys(chaves):

# é importante saber a diferença entre os elementos de um dic.

# temos os valores, são os valores adicionados no dic. podemos mostrar esse valores da seguinte forma:

''''var = {'nome': 'vini', 'idade': 20, 'sexo': 'M'}
print(var.values())
# temos as keys: São as classes ao qual adicionamos os values;
print(var.keys())
# temos o items: q mostra tanto os values quanto as keys.
print(var.items())

# Podemos formatar o print da seguinte forma:
print()
for k, v in var.items():
    print(f'{k}: {v}')

# Podemos adicionar dic. em listas:
print()
ficha = [var]
print(ficha[0]['nome'])
print(ficha[0]['idade'])'''

# PRÁTICA

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa:'))
    estado['sigla'] = str(input('Sigla dos Estado:'))
    brasil.append(estado.copy())
print(brasil)
# ou
print()
for e in brasil:
    print(e)
# ou
print()
for e in brasil:
    for k, v in e.items():
        print(f'{k}: {v}')


