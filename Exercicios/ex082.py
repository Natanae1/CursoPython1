#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listai = []
listap = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n%2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    r = str(input('Deseja continuar ?[S/N] '))
    if r in 'Nn':
        break
print('=*' * 35)
print(f'A lista completa é {lista}')
print(f'A lista de números ímpares é {listai}')
print(f'A lista de números pares é {listap}')