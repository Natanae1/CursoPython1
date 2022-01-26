#Desenvolva uma logica que leia o peso e altura, calcule o IMC e mostre seu status
#Abaixo de 18.5 - Abaixo do peso
#Entre 18.5 e 25 - Peso ideal
#25 até 30  - Sobrepeso
#30 até 40 - Obesidade
#Acima de 40 - Obesidade mórbida

peso = int(input('Insira seu peso: '))
a = int(input('Insira sua altura: '))
imc = peso / (a * a)
print(imc)

