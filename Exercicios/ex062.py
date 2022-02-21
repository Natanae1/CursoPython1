#Refaça o desafio 61 perguntando se ele quer mostrar mais termos, programa encerra quando disser que quer mostrar 0 termos
print('Gerador de PA')
print('-==' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Insira a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > ' .format(termo), end = '' )
        termo += razao
        cont += 1
    print('AGUARDANDO...')
    mais = int(input('Quantos temos a mais você quer visualizar? '))
print('Progessão finalizada com {} termos '.format(total))