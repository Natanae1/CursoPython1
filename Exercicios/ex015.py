d = int (input ('Quantos dias você utilizou o carro ?'))
km = int (input('Quantos km rodados ?'))
t = (d * 60) + (km * 0.15)
print('O valor a ser pago é de R${:.2f} '.format(t))