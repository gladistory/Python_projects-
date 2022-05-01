# listas compostas: podemos escrever listas dentro de listas

'''dados = ['João', 19]
pessoas = list()
pessoas.append(dados[:])
print(pessoas)'''

'''teste = list()
teste.append('vinicius')
teste.append(20)
gang = list()
gang.append(teste[:])

# ao adicionar o comando cópia de dados'[:]' os os dois valores são adicinados na lista gang.]

# quando não se utiliza o comando, o programa apenas inseri o valor trocado.

teste[0] = 'maria'
teste[1] = 22
gang.append(teste)
print(gang)'''


''''# listas compostas podem ser feitas também assim:
dados = [['joana', 13], ['luan', 15], ['vini', 20], ['carla', 22]]
# podemos mostrar cada item da lista ou ela completa:
print(dados)  # lista completa
print(dados[0])  # apenas uma das listas internas
print(dados[0][0])  # apenas um dos valores da lista interna'''


'''# para mostrar os itens em outra formatação:
dados = [['joana', 13], ['luan', 15], ['vini', 20], ['carla', 22]]
for p in dados:
    print(p)
# ou
    print(p[0])  # só um item da lista interna
# ou
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

# Estrutura para salvar dados em uma lista e análise de dados de uma lista:
grupo = list()
dados = list()
totmai = totmen = 0
for c  in range(0, 1):
    dados.append(str(input('Digite seu nome:')))
    dados.append(int(input('Digite sua idade:')))
    grupo.append(dados[:])
    dados.clear()
for p in grupo:
    if p[1] >= 18:
        print(f'{p[0]} MAIOR de idade ')
        totmai += 1
    else:
        print(f'{p[0]} MENOR de idade ')
        totmen += 1
print(f'Temos  {totmen} menores e {totmai} maiores de idade')










