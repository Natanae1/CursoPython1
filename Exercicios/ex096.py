# Faça um programa que tenha uma função chamada área() que receba dimensões de um terreno (largura e comprimento)
# mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


print(' Calculo de terreno')
print('-' *20)
l = float(input('Insira a largura(m): '))
c = float(input('Insira o comprimento(m): '))
area(l, c)
