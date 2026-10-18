def print_msg_num(msg:str, num:float) -> None:
    print(f'Mensagem: {msg}')
    print(f'Número: {num}')

if __name__ == '__main__':
    print('Preencha os seguintes campos para mostrar uma mensagem e um número', end='\n\n')

    mensagem = str(input('Mensagem: '))
    numero = float(input('Número: '))
    print('=-' * 20)
    print('Output:')
    print_msg_num(mensagem, numero)
    print('=-' * 20)
