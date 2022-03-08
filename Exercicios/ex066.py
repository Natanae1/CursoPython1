#Programa que lê vários números inteiros e só vai parar ao digitar o número 999.
#No final, mostrar quantos foram digitados e a soma deles
n = 0
s = 0
cont = 0
while True:
    n = int(input('Digite um numero: (999 para encerrar): '))
    if n == 999:
        break
    s += n
    cont += 1
#print('A soma é {}' .format(s))
print(f'Foram digitados {cont} valores')
print(f'A soma é {s}')