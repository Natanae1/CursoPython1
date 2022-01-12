#Um professor que sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude lendo o nome deles e o escolhido

import random
a = input(str('Qual nome do primeiro aluno?:'))
b = input(str('Insira o nome do segundo aluno:'))
c = input(str('Informe o terceiro aluno:'))
d = input(str('E o último aluno?'))
lista = [a, b, c, d]
random.shuffle(lista)



print ('O aluno que apagará o quadro é o de número {}' .format (lista))