dados = dict()
dados["nome"] = str(input('Nome:'))
dados["date_nasc"] = int(input('Ano de nascimento:'))
dados["n_carteira"] = int(input('Nº Carteira de Trabalho (0 não tem):'))
dados["data_cont"] = int(input('Ano de contratação:'))
dados["salario"] = float(input('Salário:'))
if dados["n_carteira"] == 0:
    for k, v in dados.items():
        print(f'{k}, {v}')

