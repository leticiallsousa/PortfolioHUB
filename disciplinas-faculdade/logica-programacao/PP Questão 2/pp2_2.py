from rich import print
from rich.console import Console

console = Console()

qtd_alunos = aprovados = reprovados = soma = 0

print('[blue]Obs: Digite [b]-1[/] para sair da repetição[/]')

while True:
    valor = float(input(f'Digite a {qtd_alunos+1}ª nota da turma: '))

    if valor == -1:
        break

    if valor >= 5:
        aprovados += 1

    elif valor < 5:
        reprovados += 1

    soma += valor
    qtd_alunos += 1

media = soma/qtd_alunos

console.rule(style='white')

print(f'Quantidade de alunos que fizeram a prova: {qtd_alunos}')
print(f'Quantidade de alunos aprovados: {aprovados}')
print(f'Quantidade de alunos reprovados: {reprovados}')
print(f'Média da turma: {media:.2f}')