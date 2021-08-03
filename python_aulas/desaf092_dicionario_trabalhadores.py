from datetime import date
func = {}
func['Nome'] = str(input('Nome: '))
func['idade'] = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - func['idade']
func['idade'] = idade
func['CTPS'] = int(input('Carteira de trabalho (0 não possui): '))
if not func['CTPS'] == 0:
    func['Contratação'] = int(input('Ano de contratação: '))
    func['Salarios'] = float(input('Salario R$: '))
    func['Aposentadoria'] = (func['Contratação']+ 35) - anoatual + idade
print('+='*30)
for k , v in func.items():
    print(f'{k} tem o valor {v}')
