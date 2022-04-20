#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = list()
jogos = list()
print('=' * 30)
print('         MEGA SENA')
print('=' * 30)
jogosq = int(input('Quantos jogos aleatórios você deseja ? '))
totalj = 1
while totalj <= jogosq:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalj += 1
print('==' * 15, f'SORTEANDO {jogosq} JOGOS', '==' * 15)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('=' * 20, 'BOA SORTE !!', '=' *20)

