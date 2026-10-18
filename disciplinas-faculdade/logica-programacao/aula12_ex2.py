def soma(n1:int, n2:int) -> int:
    return n1+n2

def subtracao(n1:int, n2:int) -> int:
    return n1-n2

if __name__ == '__main__':
    print('Preencha os seguintes campos para calcular a soma e subtração dos números', end='\n\n')
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    print('=-'*20)
    print(f'Soma: {num1} + {num2} = {soma(num1, num2)}')
    print(f'Subtração: {num1} - {num2} = {subtracao(num1, num2)}')
