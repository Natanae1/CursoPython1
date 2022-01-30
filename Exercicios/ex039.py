#Faça um programa que leia o ano de nascimento e informe: Se ela ainda vai se alistar, se é hora de alistar ou se já passou do tempo de alistamento
#Seu programa deve mostrar o tempo que falta ou o tempo que passou do prazo

from datetime import date
print('''Qual seu sexo ?
ESCOLHA [1] PARA MASCULINO
ESCOLHA [2] PARA FEMININO''')
sexo = int(input('Insira sua opção:'))
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year #pegando o ano atual

if sexo == 1:
    if anoatual - anonasc < 18:
        print('Em breve você se alistará, faltam {} anos' .format(18 - (anoatual - anonasc)))
        print('Você se alistará em {}.' .format(anoatual + (anoatual - anonasc)))

    elif anoatual - anonasc == 18:
        print('Você deve se alistar imediatamente!')

    elif anoatual - anonasc > 18:
        print('Você já deveria ter se alistado há {} anos.' .format((anoatual - anonasc) - 18))

else:
    print('Você nao precisa  cumprir o alistamento obrigatório.')
