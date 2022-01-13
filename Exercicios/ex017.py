#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre a hipotenusa

from math import hypot
c1 = float(input ('Insira o comprimento do cateto oposto: '))
c2 = float (input ('Insira o comprimento do cateto adjacente: '))
hipotenusa = hypot(c1,c2)
print('A hipotenusa dos catetos {} e {} é de {:.2f} '.format (c1,c2,hipotenusa))