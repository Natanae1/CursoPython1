#Faça um programa que leia o primeiro termo e a razão, no final mostre os 10 primeiros termos dessa progressão

primeiro = int(input('Insira o termo: '))
razao = int(input('Insira a razão: ' ))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}' .format(c))
print('FIM')