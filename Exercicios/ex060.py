#Faça um programa que leia um numero e mostre seu factorial
print('Vamos calcular o factorial!')
num = int(input('Insira um número: '))
resultado = 1
cont = 1
while cont <= num:
    resultado *= cont
    cont += 1

print(resultado)
#módulo factorial, do math, faz a mesma coisa