#Faça um programa que leia o peso de 5 pessoas e mostre qual foi o maior e menor peso

for pess in range(1,6):
    peso = float(input('Insira o peso da {}° pessoa: ' .format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso
print('O maior peso digitado foi de {}Kg' .format(maior))
print('O menor peso digitado foi de {}kg' .format(menor))
