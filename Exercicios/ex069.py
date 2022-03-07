#Analise de dados do grupo
opcao = 'S'
maiorid = 0
totalh = 0
totalm = 0
while opcao in 'Ss':
    print("==" * 10)
    print("CADASTRE UMA PESSOA")
    print("==" * 10)
    idade = int(input('Idade: '))
    sexo = int(input('''SEXO:
[1] MASCULINO
[2] FEMININO 
Escolha uma opção: '''))
    if idade > 18:
        maiorid += 1
    if sexo == 1:
        totalh += 1
    if sexo == 2 and idade < 20:
        totalm += 1
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Existem {maiorid} pessoas com mais de 18 anos')
print(f'Existem {totalh} homens cadastrados.')
print(f'Existem {totalm} mulheres com menos de 20 anos')

