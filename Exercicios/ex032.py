#faça um programa que leia um ano e mostre se ele é bissexto

ano = int(input('Insira um ano:'))

if (ano % 4) == 0 and (ano % 100) == 0 or (ano % 400) == 0:
    print('{} é um ano bissexto' .format(ano))
else:
    print('Este não é um ano bissexto')