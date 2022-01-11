#Faça um programa que leia o salario de um funcionario e mostre seu novo salário com 15% de aumento

salario = float  (input ('Qual valor do salário? R$'))
#percentual = 15.0 / 100.0 #15%
salario_final = salario + (salario * 15 / 100)

print('O valor do seu salário atualmente é de: {:.2f}, logo ele passará a ser {:.2f}' .format(salario,salario_final))