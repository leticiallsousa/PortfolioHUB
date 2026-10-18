from rich import print
from rich.console import Console

console = Console()

qtd = soma = maior_20 = 0

print('[blue]Obs: Digite [b]0[/] para sair da repetição[/]')

while True:
    valor = float(input(f'Digite o {qtd+1}° número: '))

    if valor == 0:
        break

    qtd += 1
    soma += valor

    if valor > 20:
        maior_20 += 1

media = soma/qtd

console.rule(style='white')

print(f'Quantidade de valores digitados: {qtd}')
print(f'Soma dos valores: {soma:.2f}')
print(f'Média aritmética: {media:.2f}')
print(f'Quantidade de valores acima de 20: {maior_20}')


