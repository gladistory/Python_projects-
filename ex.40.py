import time
print('Calculo da média da turma X')
nome = str(input('digite seu nome:'))
lista = ['luan', 'joana', 'paulo']
if nome == lista[0]:
    print('PROCESSANDO...')
    time.sleep(2)
    print('Acesso liberado')
    n1 = float(input('digite a primeira nota:'))
    n2 = float(input('digite a segunda nota:'))
    media = (n1 + n2) / 2
    if media < 5:
        print('REPROVADO!')
    elif 5 <= media < 7:
        print('RECUPERAÇÃO')
    elif media >= 7:
        print('APROVADO')
elif nome == lista[1]:
    print('PROCESSANDO...')
    time.sleep(2)
    print('Acesso liberado')
elif nome == lista[2]:
    print('PROCESSANDO...')
    time.sleep(2)
    print('Acesso liberado !')
else:
    print('PROCESSANDO...')
    time.sleep(2)
    print('Acesso negado !')
print('PROCESSO FINALIZADO!')