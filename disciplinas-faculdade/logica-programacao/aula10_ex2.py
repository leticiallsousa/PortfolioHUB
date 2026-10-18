from rich.console import Console
console = Console()

print('Esse programa irá ler 50 números inteiros digitados pelo usuário e, em seguida, mostrar informações sobre eles.')
console.rule(style='white')
print()

pares = impares = soma = 0
for i in range(5):
    numero = int(input(f'Digite o {i+1}° número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    soma += numero

console.rule(style='white')
print(f'Quantidade de valores pares: {pares}')
print(f'Quantidade de valores ímpares: {impares}')
print(f'Soma de todos os valores: {soma}')