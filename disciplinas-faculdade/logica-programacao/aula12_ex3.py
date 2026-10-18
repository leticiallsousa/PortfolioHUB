def soma(n1:int, n2:int) -> int:
    return n1+n2

def subtracao(n1:int, n2:int) -> int:
    return n1-n2

if __name__ == '__main__':
    print('[+] Somar\n[-] Subtrair\n')
    operacao = input(f'Escolha uma operação: ')
    while operacao not in ['+', '-']:
        operacao = input(f'Inválido! Escolha uma operação: ')

    print('=-' * 20)
    num1 = int(input(f'Número 1: '))
    num2 = int(input(f'Número 2: '))

    print('=-'*20)
    if operacao == '+':
        print(f'Resultado da soma: {num1} + {num2} = {soma(num1, num2)}')
    elif operacao == '-':
        print(f'Resultado da subtração: {num1} - {num2} = {subtracao(num1, num2)}')

