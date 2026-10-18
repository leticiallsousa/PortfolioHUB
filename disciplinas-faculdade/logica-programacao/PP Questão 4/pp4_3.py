print('-'*33)
print('Ordem Decrescente Personalizada')
print('-'*33)

inicial = int(input('Qual o número natural inicial? '))
while inicial <= 0:
    print('Erro! O valor precisa ser maior do que zero. Tente novamente!')
    inicial = int(input('Qual o número natural inicial? '))

print('-'*33)

for i in range (inicial, -1, -1):
    print(i)

print('-'*33)
print(f'Quantidade de números: {inicial+1}')
print('-'*33)
