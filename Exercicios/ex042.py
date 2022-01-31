##Programa que lê o comprimento de três retas e diz se pode ou não formar um triangulo
#Equilatero: Todos lados iguais
#Isósceles: Dois lados iguais
#Escaleno: todos lados diferentes

a = int(input('Insira a primeira medida: '))
b = int(input('Insira a segunda medida: '))
c = int(input('Insira a terceira medida: '))
if a < b + c and b < a + c and c < a + b:
    print('Essas medidas PODEM formar um triangulo ' ,end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Medidas insuficientes para formar um triangulo, tente outras medidas.')

