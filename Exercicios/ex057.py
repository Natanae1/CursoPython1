#Faça um programa que leia o sexo de uma pessoa, mas só aceita M ou F. Caso seja diferente peça um valor correto.
nome = str(input('Insira seu nome: '))
sexo = str(input(('Digite seu sexo: [F/M] '))).strip().upper()[0]
while sexo not in 'MF':
    print('Opção inválida!')
    sexo = str(input('Digite seu sexo novamente: [F/M] ')).strip().upper()[0]
print('Olá {}, o sexo foi registrado com sucesso!' .format(nome))
