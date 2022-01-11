# Faça um programa que leia o preço de um produto e mostre seu preço com 5% de desconto

produto = float(input('Qual valor do produto? R$'))
#desconto = 5.0 / 100.0 #5%
produtod = produto - (produto * 5 / 100) # produto com desconto recebe o produto menos o valor do desconto vezes produto inicial


print('Com o desconto de 5%, você pagará somente R$ {:.02f}' .format(produtod))

