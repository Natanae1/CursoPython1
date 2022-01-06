#Faça um programa que leia o salario de um funcionario e mostre seu novo salário com 15% de aumento

salario = int (input ('Qual valor do salário?'))
percentual = 15.0 / 100.0 #15%
salario_final = salario + (percentual * salario)

print('O valor do seu salário atualmente é de: {:.02f}, logo ele passará a ser {:.02f}' .format(salario,salario_final))