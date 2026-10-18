from rich import print
from rich.console import Console

console = Console()

nome_disciplina = input('Qual o nome da disciplina? ')

qt_alunos = notas = 0
print('[blue]Digite [b]-1[/] para sair da repetição[/]')

while True:
    nota = float(input(f'Qual a nota do {qt_alunos+1}º aluno? '))
    if nota == -1:
        print('[red]Finalizando programa...[/]')
        break
    notas += nota
    qt_alunos += 1

console.rule(style='white')

media = notas/qt_alunos

print(f'Nome da disciplina: {nome_disciplina}')
print(f'Quantidade de alunos: {qt_alunos}')
print(f'Soma de todas as notas: {notas:.2f}')
print(f'Média aritmética: {media:.2f}')


