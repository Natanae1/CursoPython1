#Faça um programa que leia um numero de 0 a 9999 e mostre os digitos separados por unidade, dezena, centena e milhar

n = int(input('Insira um numero:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Milhar: {}'.format(m))
print('Centena: {}' .format(c))
print('Dezena: {}' .format(d))
print('Unidade: {}' .format(u))