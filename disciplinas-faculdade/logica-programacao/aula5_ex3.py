from rich import print
from rich.console import Console

console = Console()

print('[blue]Obs: Digite [b]0[/] para sair da repetição[/]')

menor_valor = 9999999999999999999

while True:
    valor = float(input('Digite um valor: '))

    if valor == 0:
        break

    if valor < menor_valor:
        menor_valor = valor

console.rule(style='white')

print(f'O menor valor digitado foi {menor_valor}')