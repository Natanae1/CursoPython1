#SIMULADOR DE CAIXA ELETRONICO COM NOTAS DE 50, 20, 10 E 1
print('=' * 30)
print('{:^30}' .format('CAIXA  ELETRONICO'))
print('=' * 30)
valor = int(input('Quanto você quer sacar ? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('SAQUE EFETUADO COM SUCESSO!! VOLTE SEMPRE!')