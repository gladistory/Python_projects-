list = []
while True:
    n = int(input('Digite um valor:'))
    if n not in list:
        list.append(n)
        print('Valor adicinado com sucesso ...')
    else:
        print('valor duplicado ! Não vou adicionar.')
    choice = str(input('Deseja continuar ?[S/N]')).upper().split()[0]
    if choice in 'N':
        break
list.sort()
print(f'Foram adicionados os valores: {list}')

