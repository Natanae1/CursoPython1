#Faça um programa que faça o computador escolher um numero de 0 a 5 e peça para o usuário descobrir o escolhido

n1 = int(input('Insira um número entre 0 e 5'))
import random
num = random.randint(0, 5)

if n1 == num:
    print('VOCÊ ACERTOU O NÚMERO, PARABÉNS!')
else:
    print('Você errou, eu pensei no {} =('.format(num))

