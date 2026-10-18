from rich import print
from rich.console import Console

console = Console()

valores = []

print('[b blue]Obs: Digite 0 para sair da repetição[/]')

while True:
    valor = float(console.input(f'[hot_pink3]Digite o {len(valores)+1}º valor:[/] '))
    if valor == 0:
        break
    else:
        valores.append(valor)

maior_igual_50 = 0

for i in valores:
    if i >= 50:
        maior_igual_50 += 1

console.rule(style='white')

print(f'Foram digitados {len(valores)} valores.')
print(f'Soma dos valores: {sum(valores)}')
print(f'Média aritmética: {sum(valores)/len(valores):.2f}')
print(f'Maior valor: {max(valores)}')
print(f'Menor valor: {min(valores)}')
print(f'Valores maiores ou iguais a 50: {maior_igual_50}')