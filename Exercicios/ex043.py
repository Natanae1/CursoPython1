#Desenvolva uma logica que leia o peso e altura, calcule o IMC e mostre seu status
#Abaixo de 18.5 - Abaixo do peso
#Entre 18.5 e 25 - Peso ideal
#25 até 30  - Sobrepeso
#30 até 40 - Obesidade
#Acima de 40 - Obesidade mórbida

peso = float(input('Insira seu peso: '))
a = float(input('Insira sua altura: '))
imc = peso / (a ** 2)
print('O seu IMC é {:.1f}' .format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso.')
elif 18.5 <= imc < 25:
    print('Você está no seu peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está na OBESIDADE.')
else:
    print('Você está na OBESIDADE MÓRBIDA.')

