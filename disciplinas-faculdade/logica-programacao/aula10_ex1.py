from rich import print
from rich.console import Console

console = Console()

print('[white]Digite [0] para sair da repetição[/]')
print('''Chegou num frigorífico uma determinada quantidade de bois cadastrados da seguinte forma: cada boi traz preso ao seu pescoço um cartão com o seu peso. Digite abaixo o peso escrito no cartão de cada um desses bois.''')

console.rule(style='white')
print()

qnt = soma = mais_600 = 0
while True:
    peso = float(input(f'Cartão {qnt+1}: '))
    if peso == 0:
        break
    elif peso > 600:
        mais_600 += 1
    qnt += 1
    soma += peso

media = soma/qnt

console.rule(style='white')

print(f'Quantidade de bois analisados: {qnt}')
print(f'Soma de peso dos bois: {soma}')
print(f'Média aritmética do peso dos bois: {media:.2f}')
print(f'Quantidade de bois com mais de 600kg: {mais_600}')