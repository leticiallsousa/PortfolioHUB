from rich import print
soma = 0
qtd = 0

print('[blue]Obs: Digite [b]0[/] para sair da repetição[/]')

while True:
    numero = int(input('Digite um número inteiro qualquer: '))

    if numero == 0:
        break
    elif numero % 2 == 0:
        soma += numero
        qtd += 1

print(f'[hot_pink2]A soma dos {qtd} números pares é igual a {soma}[/]')
