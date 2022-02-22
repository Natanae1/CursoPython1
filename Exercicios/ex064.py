#Crie um programa que leia varios numeros inteiros. O programa só vai parar quando digitar 999 e no final mostre a soma de todos
num = 0
cont = 0
soma = 0
num = int(input('Insira um numero ou digite 999 para finalizar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Insira um numero: '))
if cont == 0:
    print('Nenhum número digitado!')
print('A soma dos {} números digitados é {}.' .format(cont, soma))
print('Finalizando. . .')
