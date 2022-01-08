#Faça um programa que leia o valor em metros e mostre convertido em centrimetros e milimetros

m = float (input ('Qual o valor em metros deseja calcular? '))

d = m * 10
c = m * 100
ml = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000
print ('Os {}m metros convertidos em decimetros é {:.0f}dm\n Em centimetros é {:.0f}cm\nEm milimetros é: {:.0f}\nEm decametro é {:.0f}dam\nEm hectometro é {:.0f}hm\nEm kilometro é {:.0f}km'.format(m, d, c, ml, dam, hm, km))





