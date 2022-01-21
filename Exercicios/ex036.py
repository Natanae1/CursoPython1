#Faça um programa para aprovar empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, visto que não pode exceder 30% do salário, ou o empréstimo será negado.
from time import sleep

vc = float(input('Qual valor do imóvel?: R$')) #valor casa
s = float(input('Qual valor da sua renda mensal? RS$:')) #salario
a = int(input('Em quantos anos deseja financiar?')) #anos

porcentagem = s * 30 / 100
parcelas = (vc / a) / 12

print('CALCULANDO O FINANCIAMENTO...')
sleep(2)

if parcelas > porcentagem:
    print('CRÉDITO NÃO APROVADO!')
    print('O financiamento do imóvel no valor de R${:.2f} ficará dividido em {} anos, com parcelas de R${:.2f} mensais' .format(vc, a, parcelas))
    print('Infelizmente não poderemos concluir o financiamento, as parcelas deste imóvel estão acima de 30%  da sua renda mensal.')

else:
    print('CRÉDITO APROVADO!!')
    print('O financiamento do imóvel no valor de R${:.2f} ficará dividido em {} anos, com parcelas de R${:.2f} mensais' .format(vc, a, parcelas))


