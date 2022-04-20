galera = list()
dado = list()
totpess = 0
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    totpess += 1
    r = str(input('Deseja cadastrar outra pessoa ? [S/N] '))
    if r in 'Nn':
        break

print('=' *35)
print(f'Você cadastrou {totpess} pessoas.')
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'{p[0]} ' , end='')
print()
print(f'O maior peso foi de {mai}kg. Peso de ' , end='')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]} ' , end='')
print('=' *35)


