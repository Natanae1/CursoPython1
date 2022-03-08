#Programa que lê o nome do produto e preço, e mostra o total da compra, produto acima de R$1000 e produto mais barato
total = 0
while True:
    print('{:=^40}' .format('VAREJÃO DA CHIRLEY'))
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}' .format('FINALIZANDO COMPRA'))
print(f'O valor total da compra foi R${total:.2f}')