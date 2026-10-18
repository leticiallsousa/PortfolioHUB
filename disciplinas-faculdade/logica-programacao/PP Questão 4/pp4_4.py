# Como a instrução está repetida, para o exercício número 4 eu fiz o mesmo do anterior, porém na ordem crescente


print('-'*33)
print('Ordem Crescente Personalizada')
print('-'*33)

final = int(input('Qual o número natural final? '))
while final <= 0:
    print('Erro! O valor precisa ser maior do que zero. Tente novamente!')
    final = int(input('Qual o número natural final? '))

print('-'*33)

for i in range (0, final+1):
    print(i)

print('-'*33)
print(f'Quantidade de números: {final+1}')
print('-'*33)
