#Programa que le um ano de nascimento e mostre sua categoria de acordo:
#Até 9 anos - Mirim
#Até 14 anos - Infantil
#Até 19 anos - Junior
#Até 25 anos - Sênior
#Acima - Master

from datetime import datetime
from datetime import date
from time import sleep

print('--=--' * 10)
print('               ESCOLA DE NATAÇÃO')
print('--=--' * 10)

nome = str(input('Insira seu nome: '))
idade = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year
print('Bem vindo a nossa escola de natação, {}!!' .format(nome))
print('BUSCANDO SUA CATEGORIA...')
sleep(2)
if ano - idade <= 9:
    print('Você fará parte da categoria MIRIM!')
elif ano - idade <= 14:
    print('Você fará parte da categoria INFANTIL!')
elif ano - idade <= 19:
    print('Você fará parte da categoria JUNIOR!')
elif ano - idade <= 25:
    print('Você fará parte da categoria SÊNIOR!')
else:
    print('Você fará parte da categoria MASTER!')
