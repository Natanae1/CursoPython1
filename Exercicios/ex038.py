#Escreva um programa que leia dois numeros e compare-os: O primeiro valor é maior, o segundo é maior ou não existe valor maior

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')

elif n2 > n1:
    print('O SEGUNDO valor é maior')

else:
    print('Ambos são IGUAIS!')

