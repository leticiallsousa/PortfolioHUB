from rich import print
from rich.console import Console

console = Console()

print('[b blue]Obs: Digite 0 para sair da repetição[/]')
sal_minimo = float(console.input(f'[orange1]Salário mínimo da empresa:[/] '))
salarios = []

while True:
    salario = float(console.input(f'[hot_pink3]Digite o {len(salarios)+1}º salário:[/] '))
    if salario == 0:
        break
    else:
        salarios.append(salario)

menos_que_cinco = cinco_a_dez = dez_ou_mais = 0

for i in salarios:
    if i < sal_minimo*5:
        menos_que_cinco += 1
    elif sal_minimo*5 < i < sal_minimo*10:
        cinco_a_dez += 1
    else:
        dez_ou_mais += 1

console.rule(style='white')

print(f'Salário mínimo: {sal_minimo}')
print(f'Funcionários que ganham menos que 5 salários mínimos: {menos_que_cinco}')
print(f'Funcionários que ganham entre 5 e 10 salários mínimos: {cinco_a_dez}')
print(f'Funcionários que ganham 10 ou mais salários mínimos: {dez_ou_mais}')
print(f'Valor total da folha de pagamento da empresa: {sum(salarios)}')