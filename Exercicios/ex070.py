#Programa que lê o nome do produto e preço, e mostra o total da compra, produto acima de R$1000 e produto mais barato
total = 0
totalm = 0
menor = 0
cont = 0
barato = ' '
while True:
    print('{:=^40}' .format('SOLUÇÕES TI (MADE IN CHINA)'))
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totalm += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}' .format('FINALIZANDO COMPRA'))
print(f'O valor total da compra foi R${total:.2f}')
print(f'Temos {totalm} produtos que custaram mais que R$1000.00')
print(f'O produto mais barato foi o/a {barato} e custa R${menor:.2f}')