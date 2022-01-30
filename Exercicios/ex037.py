#Escreva um programa que leia um numero inteiro e peça para usuário selecionar qual base de conversão será, tendo a binária, octal e hexadecimal (python tem biblioteca)

num = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
ESCOLHA [1] PARA BINARIA
ESCOLHA [2] PARA OCTAL
ESCOLHA [3] PARA HEXADECIMAL''')
opcao = int(input('Selecione a opção desejada: '))

if opcao == 1:
    print('{} convertido para binário é igual a {} '.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}' .format(num, hex(num)[2:]))

else:
    print('OPÇÃO INVÁLIDA!! ESCOLHA ENTRE 1, 2 e 3')