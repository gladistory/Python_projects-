dados = dict()
dados['aluno'] = str(input('Aluno: '))
dados['média'] = float(input(f'Média de {dados["aluno"]}: '))


if dados['média'] >= 6:
    dados["Situação"] = 'APROVADO'
elif 5 <= dados['média'] < 6:
    dados["Situação"] = 'RECUPERAÇÃO '
else:
    dados['Situação'] = 'REPROVADO'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
