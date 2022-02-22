#Crie um programa que leia vários numeros inteiros. No final mostre a media, maior e menor valor. O programa deve perguntar se quer continuar a digitar

opcao = 'S'
soma = 0
media = 0
quantos = 0
maior = 0
menor = 0
while opcao in 'Ss':
    num = int(input('Insira um número: '))
    soma += num
    quantos += 1
    if quantos == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
media = soma / quantos
print('Você digitou {} numeros e a média foi {}' .format(quantos, media))
print('O Maior valor foi {} e menor foi o {}' .format(maior, menor))

