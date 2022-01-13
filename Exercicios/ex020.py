#O mesmo professor deseja sortear a ordem de apresentação. Faça um programa que leia o nome dos quatro e mostre a ordem sorteada

import random
a1 = input(str('Insira o nome do primeiro aluno:'))
a2 = input(str('Insira o nome do segundo aluno:'))
a3 = input(str('Insira o nome do terceiro aluno:'))
a4 = input(str('Insira o nome do quarto aluno:'))

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: ' ,lista)