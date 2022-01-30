#Faça um jogo "Pedra papel e tesoura"

import random
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
print('VAMOS JOGAR JOKENPO!')
opcao = str(input('Selecione sua opção entre PEDRA, PAPEL e TESOURA: '))
lista = [pedra, papel, tesoura]
pc = random.choice(lista)

if opcao == pc:
    print('Droga! Eu também escolhi {}' .format(opcao))

if opcao == papel and pc == pedra:
    print('Você ganhou!!Você escolheu {} e eu escolhi {}.' .format(opcao, pc))

if opcao == papel and pc == tesoura:
    print('Eu ganhei hahahah!')

if opcao == pedra and pc == papel:
    print('Eu ganhei, tá facil!')

if opcao == pedra and pc == tesoura:
    print('Infelizmente você ganhou :(')

if opcao == tesoura and pc == papel:
    print('Você me cortou =(')

if opcao == tesoura and pc == pedra:
    print('TOMAAA, ISSO QUE TU MERECE, PERDEU!!')

