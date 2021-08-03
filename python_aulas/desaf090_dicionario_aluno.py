aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] > 7:
    aluno['resultado'] = 'APROVADO'
else:
    aluno['resultado'] = 'REPROVADO'
for k , v in aluno.items():
    print(f'  -{k} é {v}')
