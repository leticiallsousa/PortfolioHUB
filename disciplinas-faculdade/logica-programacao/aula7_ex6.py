notas = aprovados = reprovados = 0

for i in range(5):
    aluno = float(input(f'Digite a nota do {i+1}º aluno: '))
    notas += aluno

    if aluno >= 5:
        aprovados += 1
    else:
        reprovados += 1


media = notas/5

print(f'A média da turma é: {media}')
print(f'A quantidade de alunos aprovados é: {aprovados}')
print(f'A quantidade de alunos reprovados é: {reprovados}')


