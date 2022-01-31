#Elabora um programa que calcule um valor a ser pago por um produto, considerando preço normal e condições de pagamento
#A vista: Cheque/dinheiro - 10% de desconto
#A vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais: 20% de juros

valor = float(input('Qual valor do produto? R$ '))
print('FORMAS DE PAGAMENTO')
print('''[1] PAGAMENTO A VISTA VIA CHEQUE OU DINHEIRO
[2] PAGAMENTO A VISTA POR CARTÃO
[3] PAGAMENTO EM ATÉ 2X NO CARTÃO
[4] PAGAMENTO EM 3X OU MAIS NO CARTÃO''')
opcao = int(input('Selecione o método de pagamento: '))
if opcao == 1:
    desconto = valor - (valor * 10 / 100)
    print('A sua compra de R${:.2f} vai ficar no valor de R${:.2f} '.format(valor, desconto))

elif opcao == 2:
    desconto = valor - (valor * 5 / 100)
    print('A sua compra de R${:.2f} vai ficar no valor de R${:.2f} '.format(valor, desconto))
