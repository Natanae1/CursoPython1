#Programa que lê o comprimento de três retas e diz se pode ou não formar um triangulo

a = int(input('Insira a primeira medida: '))
b = int(input('Insira a segunda pedida: '))
c = int(input('Insira a terceira medida: '))
if a < b + c and b < a + c and c < a + b:
    print('Essas medidas PODEM formar um triangulo!')
else:
    print('Medidas insuficientes para formar um triangulo, tente outras medidas.')
#teste
