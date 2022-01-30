#Programa que le um ano de nascimento e mostre sua categoria de acordo:
#Até 9 anos - Mirim
#Até 14 anos - Infantil
#Até 19 anos - Junior
#Até 20 anos - Sênior
#Acima - Master

from datetime import datetime
from time import sleep

print('--=--' * 10)
print('               ESCOLA DE NATAÇÃO')
print('--=--' * 10)

nome = str(input('Insira seu nome: '))
idade = int(input('Qual o ano do seu nascimento? '))
ano = 2022
print('Bem vindo a nossa escola de natação, {}!!' .format(nome))
print('BUSCANDO SUA CATEGORIA...')
sleep(2)
if ano - idade <= 9:
    print('Você fará parte da categoria MIRIM!')

if ano - idade > 9 and ano - idade <= 14:
    print('Você fará parte da categoria INFANTIL!')

if ano - idade > 14 and ano - idade < 19:
    print('Você fará parte da categoria JUNIOR!')

if ano - idade >= 19 and ano - idade <= 20:
    print('Você fará parte da categoria SÊNIOR!')

else:
    print('Você fará parte da categoria MASTER!')
