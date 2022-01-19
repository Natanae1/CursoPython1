#Escreva um programa que calcule o valor dos funcionarios. Salario superior a 1250, o aumento é de 10% e para inferior é de 15%

salario = float(input('Insira seu salário: '))

if salario > 1250:
    print('Você receberá um aumento de 10% e seu novo salário é de R${:.2f} '.format(salario + (salario * 10 / 100)))
else:
    print('Você receberá um aumento de 15% e seu novo salário é de R${:.2f}' .format(salario + (salario * 15 / 100)))