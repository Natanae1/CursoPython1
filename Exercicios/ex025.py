#Crie um programa que leia o nome de uma pessoa e informe se possui "Silva"

nome = str(input('Insira seu nome: '))
print('Analisando seu nome...')
print('silva' in nome.lower())