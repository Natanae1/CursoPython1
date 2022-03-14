#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Monitor', 1200,
            'Teclado', 259.99,
            'Mouse', 139.99,
            'Processador', 970.00,
            'GPU', 2400,
            'SSD', 479.99,
            'HD', 359.99,
            'Memoria', 399.99)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:_<30}' , end=' ')
    else:
        print(f'R${listagem[pos]:>8.2f}')