def soma(n1:float, n2:float, n3:float) -> float:
    return n1+n2+n3

if __name__ == '__main__':
    print('Preencha os seguintes campos para somar três números', end='\n\n')

    num1 = float(input('Número 1: '))
    num2 = float(input('Número 2: '))
    num3 = float(input('Número 3: '))

    soma = soma(num1, num2, num3)
    print(f'A soma dos três valores é igual a {soma}')

