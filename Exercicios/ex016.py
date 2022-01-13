#Crie um programa que leia um número real e mostre o número inteiro EX.: 6.127 > 6

import math
n = float (input ('Digite um numero: '))
#i = math.trunc(n) #variavel i de inteiro, recebe math.trunc(variavel)
print('O numero {} convertido para inteiro é {}' .format(n, math.trunc(n)))
