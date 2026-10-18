def fatorar(num:int):
    divisores = []

    for i in range(1, num):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def check_perfeito(num:int):
    if sum(fatorar(num)) == num:
        return f'O número {numero} é um número perfeito!'
    return f'O número {numero} não é um número perfeito!'

if __name__ == '__main__':
    numero = int(input('Número: '))
    print(check_perfeito(numero))


