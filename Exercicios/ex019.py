#Um professor que sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude lendo o nome deles e o escolhido

import random
a = str (input('Qual nome do primeiro aluno?:'))
b = str (input('Insira o nome do segundo aluno:'))
c = str (input('Informe o terceiro aluno:'))
d = str (input('E o último aluno?'))
lista = [a, b, c, d]
#random.choice escolhe um dos valores inseridos na lista
print ('O aluno que apagará o quadro é o: {}' .format (random.choice(lista)))