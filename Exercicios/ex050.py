#Faça um programa que leia 6 numeros inteiros e mostre a soma daqueles que for par, se for impar desconsidere
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Insira um numero: ' .format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} valores é igual a {}' .format(cont, soma))