sexo = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
      sexo = str(input('dado inválido, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
