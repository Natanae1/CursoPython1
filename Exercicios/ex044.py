#Elabora um programa que calcule um valor a ser pago por um produto, considerando preço normal e condições de pagamento
#A vista: Cheque/dinheiro - 10% de desconto
#A vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais: 20% de juros

valor = float(input('Qual valor das compras? R$ '))
print('FORMAS DE PAGAMENTO')
print('''[1] PAGAMENTO A VISTA VIA CHEQUE OU DINHEIRO
[2] PAGAMENTO A VISTA POR CARTÃO
[3] PAGAMENTO EM ATÉ 2X NO CARTÃO
[4] PAGAMENTO EM 3X OU MAIS NO CARTÃO''')
opcao = int(input('Selecione o método de pagamento: '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
    print('A sua compra de R${:.2f} vai ficar no valor de R${:.2f} '.format(valor, total))

elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print('A sua compra de R${:.2f} vai ficar no valor de R${:.2f} '.format(valor, total))

elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de RS{:.2f} SEM JUROS!!'.format(parcela))
    print('Você não pagará juros, então sua compra de RS{:.2f} no final sairá por R${:.2f}' .format(valor, total))

elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalparcela = int(input('Em quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra de {:.2f} será parcelada em {}x de R${:.2f} com juros.'.format(valor, totalparcela, parcela))

else:
    total = valor
    print('OPÇÃO INVÁLIDA DE PAGAMENTO!!')
    print('Sua compra de R${:.2f} sairá por R${:.2f}!'.format(valor, total))


