#Programa que lê nome completo e mostre o primeiro e ultimo separadamente

nome = str(input('Insira seu nome: ')).strip()
dividido = nome.split()
print('Seu primeiro nome é {} '.format(dividido[0]))
print('Seu último nome é {}' .format(dividido[len(dividido)-1])) #ele via imprimir o dividido na posição len, que vai contar quantos tem -1, sendo a ultima
