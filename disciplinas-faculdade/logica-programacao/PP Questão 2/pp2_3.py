from rich import print
from rich.console import Console

console = Console()

pares = []
impares = []

print('[blue]Obs: Digite [b]0[/] para sair da repetição[/]')

while True:
    valor = float(input(f'Digite o número: '))

    if valor == 0:
        break

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

console.rule(style='white')

print(f'Média dos números pares: {sum(pares)/len(pares):.2f}')
print(f'Média dos números ímpares: {sum(impares)/len(impares):.2f}')
print(f'Quantidade total de números digitados: {len(pares)+len(impares)}')
print(f'Soma total de números digitados: {sum(pares)+sum(impares):.2f}')