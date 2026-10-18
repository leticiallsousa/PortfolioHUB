def valor(num):
    if num > 0:
        print('Valor positivo.')
    elif num == 0:
        print('Valor nulo.')
    elif num < 0:
        print('Valor negativo.')
    else:
        print('Inválido. O valor inserido não é um número.')

if __name__ == '__main__':
    print('Preencha o seguinte campo para verificar se o número é positivo, negativo ou nulo.', end='\n\n')

    numero = int(input('Número: '))
    print(f'Número digitado: {numero}')
    valor(numero)