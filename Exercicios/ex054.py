#Crie um programa que leia o ano de nascimento de 7 pessoas e no final mostre quais atingiram a maioridade

from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? ' .format(pess)))
    idade = ano - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Existem {} pessoas maiores de idade' .format(totmaior))
print('Existem {} pessoas maiores de idade' .format(totmenor))
