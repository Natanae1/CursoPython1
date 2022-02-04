#Faça um programa que calcule a soma entre todos numero ímpaer que são multiplos de 3 e se encontra entre 1 a 500
soma = 0
cont = 0
for c in range(1, 501,2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('Soma de todos {} valores solicitados é {}' .format(cont, soma))