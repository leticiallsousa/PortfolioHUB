def soma(n1: float, n2: float):
    return n1+n2

if __name__ == '__main__':
    print('Para realizarmos a operação [soma], digite dois números nos seguintes campos:')
    print('-'*30)
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))
    soma = soma(num1, num2)
    print(f'Soma: {soma}')
    print('-' * 30)
