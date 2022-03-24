#Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
qtdn = 0
lista = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    qtdn += 1
    r = str(input('Deseja continuar ?[S/N] '))
    if r in 'Nn':
        break
print('=-' * 35)
print(f'Você digitou {qtdn} valores')
print(f'A lista em ordem decrescente é {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não está na lista.')
