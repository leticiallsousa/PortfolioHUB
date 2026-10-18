def mostra_mensagem():
    return '[mensagem padrão]'

def mostra_mensagem_2(msg: str):
    print(msg)

if __name__ == '__main__':
    print('-'*30)
    msg1 = mostra_mensagem()
    print(f'{msg1}')
    print('-' * 30)
    msg2 = str(input('Dessa vez, digite uma mensagem que você quer que seja impressa na tela: '))
    mostra_mensagem_2(msg2)
    print('-' * 30)