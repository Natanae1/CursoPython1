#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'Você digitou os valores {lista}')
print(f'O menor valor digitado foi o {menor} nas posições ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end=' ')
print(f'\nO maior valor digitado foi o {maior} nas posições ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end=' ')
print()




