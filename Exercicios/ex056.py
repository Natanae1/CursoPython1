#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e mostre:
#Media de idade
#Homem mais velho
#Quantas mulheres tem menos de 20 anos

print('CADASTRO DE PESSOAS')
somaidade = 0
mdidade = 0
maioridadeh = 0
nomevelho = ' '
totmulher20 = 0
for pess in range(1,5):
    print('==== {}° PESSOA ====' .format(pess))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = int(input('''SEXO:
[1] MASCULINO
[2] FEMININO
Digite a opção: '''))
    somaidade += idade
    if pess == 1 and sexo == 1: #se for a primeira pessoa e for do sexo masculino
        maioridadeh = idade #a maior idade recebe a idade
        nomevelho = nome # e o mais velho recebe nome
    if sexo == 1 and idade > maioridadeh: #se sexo for masculino e idade for maior que a idade anterior (maioridadeh)
        maioridadeh = idade
        nomevelho = nome
    if sexo == 2 and idade < 20:
        totmulher20 += 1
mdidade = somaidade / 4
print('O homem mais velho é o {} e tem {} anos' .format(nomevelho, maioridadeh))
print('A média de idade do grupo é de {} anos'.format(mdidade))
print('Ao todo são {} mulheres com menos de 20 anos' .format(totmulher20))




