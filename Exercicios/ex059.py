#Crie um programa que mostre dois valores e mostre um menu na tela:
# Somar, multiplicar, maior, novos números, sair do programa
from time import sleep
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
opcao = 0
maior = 0
while opcao != 5:
    print('''Escolha o que você quer fazer:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] INSERIR NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('A soma entre {} e {} é {}' .format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação de {} e {} é {}' .format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior número é o {}' .format(n1, n2,maior))
    elif opcao == 4:
        print('Informe novamente os números: ')
        n1 = int(input('Insira o primeiro número: '))
        n2 = int(input('Insira o segundo número: '))
    elif opcao == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida! Tente novamente')
    sleep(2)
