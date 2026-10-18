def area_triangulo(base:float, altura:float):
    return base*altura/2

if __name__ == '__main__':
    print('Preencha os seguintes campos para calcular a área de um triângulo', end='\n\n')
    b = float(input('Base do triângulo: '))
    a = float(input('Altura do triângulo: '))

    print(f'A área do triângulo é igual a {area_triangulo(b, a)}')