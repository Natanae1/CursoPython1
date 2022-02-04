#Faça um programa que mostre na tela uma contagem regressiva de 10 segundos, com pausa de 1 segundo

from time import sleep
print('CONTAGEM REGRESSIVA...')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUUUUUUUUUM')