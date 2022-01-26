#Faça um programa que leia o ano de nascimento e informe: Se ela ainda vai se alistar, se é hora de alistar ou se já passou do tempo de alistamento
#Seu programa deve mostrar o tempo que falta ou o tempo que passou do prazo

from datetime import date
anonasc = int(input('Insira o ano do seu nascimento: '))
anoatual = 2022
if anonasc - anoatual < 17:
    print('Em breve voce se alistará')

if anonasc - anoatual > 17 and anonasc - anoatual == 18:
    print('Hora de se alistar!')

