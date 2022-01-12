#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre a hipotenusa

import math
c1 = float(input ('Insira o comprimento do cateto oposto: '))
c2 = float (input ('Insira o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(c1,c2)
print('A hipotenusa dos catetos {} e {} é de {:.2f} '.format (c1,c2,hipotenusa))