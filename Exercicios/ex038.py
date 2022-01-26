#Escreva um programa que leia dois numeros e compare-os: O primeiro valor é maior, o segundo é maior ou não existe valor maior

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
if n2 > n1:
    maior = n2
    print('O primeiro valor {} é maior' .format(maior))

if n1 > n2:
    maior = n1
    print(maior)

if n1 == n2:
    igual = n1
    igual = n2
    print(igual)
#rint('O maior numero é o {}' .format(maior))


