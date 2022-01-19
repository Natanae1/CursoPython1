#Faça um programa que leia o nome completo de uma pessoa e mostre:
#Todas letras maiusculas
#Todas letras minusculas
#Quantas letras sem espaço
#Quantas letras tem o primeiro nome
#teste

nome = str(input('Insira seu nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print('Seu nome possui {} letras' .format(len(nome) - nome.count(' '))) # (len(nome)) vai contar as letras / nome.count(' ') identifica os espaços
dividido = nome.split() #dividiu a  string
print('Seu primeiro nome tem {} letras' .format(len(dividido[0]))) #está printando somente a primeira lista do nome / len está contando