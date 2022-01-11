# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto em dólar pode comprar ($3.27)

s = float  (input('Digite o valor da sua carteira? R$'))
d = s / 3.27
print('Com R${:.2f} você pode comprar US${:.2f} em dolares' .format(s,d))


