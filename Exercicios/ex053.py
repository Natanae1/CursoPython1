#Crie um programa que leia uma frase e diga se é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper() #removi os espaços e coloquei tudo em maiusculo
palavras = frase.split() #dividi a frase
junto = ''.join(palavras) #juntei ela com espaços (''.join)
inverso = ''
#poderia usar a forma:
#inverso = junto[::-1] pega do inicio ate o fim de trás pra frente (-1)
for letra in range(len(junto) -1, -1, -1): #foi da ultima ate a primeira, trocando as letras
    inverso += junto[letra]
print('O inverso de {} é {}'. format(junto, inverso))
if inverso == junto: #comparou se o inverso é o mesmo que o junto
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')