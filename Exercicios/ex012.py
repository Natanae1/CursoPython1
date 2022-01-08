# Faça um programa que leia o preço de um produto e mostre seu preço com 5% de desconto

produto = int(input('Qual valor do produto?'))
desconto = 4.0 / 100.0 #5%
produtod = produto - (desconto * produto) # produto com descunto recebe o produto menos o valor do desconto vezes produto inicial


print('Com o desconto de 5%, você pagará somente R$' ,produtod)

