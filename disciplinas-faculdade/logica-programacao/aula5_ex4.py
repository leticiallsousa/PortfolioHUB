from rich import print
from rich.console import Console

console = Console()

print('[blue]Obs: Digite [b]0[/] para sair da repetição[/]')

maior = menor = None

while True:
    valor = int(input('Digite um número inteiro qualquer: '))

    if maior is None:
        maior = valor
    if menor is None:
        menor = valor

    if valor == 0:
        break

    if valor < menor:
        menor = valor

    if valor > maior:
        maior = valor

console.rule(style='white')

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')