#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla e mostre:
#Quantas vezes aparece o numero 9;
# Em que posição foi digitado o primeiro valor 3;
#Quais foram os numeros pares
num = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite um último número: ')))
print(f'Você digitou os números {num}')
print(f'O número  9 apareceu {num.count(9)} vezes')
print(f'O número 3 apareceu primeiro na {num.index(3)+1}ª posição ')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if num % 2 == 0:
        print(n, end=' ')

