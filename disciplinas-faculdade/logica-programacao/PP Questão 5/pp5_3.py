def idade(ano_nasc:int) -> int:
    return 2026-ano_nasc

if __name__ == '__main__':
    print('Preencha o seguinte campo para calcular uma idade', end='\n\n')

    ano = int(input('Ano de nascimento: '))
    idade = idade(ano)

    print(f'Em 2026, quem nasceu em {ano} tem {idade} anos')