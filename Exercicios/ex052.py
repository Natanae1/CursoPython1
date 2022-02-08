#Faça um programa que leia um numero inteiro e diga se ele é primo ou não

num = int(input('Insira um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), end=' ')
print('\nO Numero {} foi dividido {} vezes' .format(num, total))
if total == 2:
    print('É um número primo')
else:
    print('Não é  um número primo')
