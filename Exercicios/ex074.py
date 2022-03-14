#Crie um programa que vai gerar 5 números aleatorio e colocar na tupla.
#Depois vai mostrar a lista, maior e menor.
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numeros sorteados foram: ' , end= '')
for n in numeros:
    print(f'{n} ' , end='')
print(f'\nO MAIOR valor sorteado foi: {max(numeros)}') #Função que mostra o valor maximo da tupla
print(f'O MENOR valor sorteado foi: {min(numeros)}') #Função que mostra o valor minimo da tupla