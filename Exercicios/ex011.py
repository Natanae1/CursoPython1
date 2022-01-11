#Faça um programa que leia LARGURA E ALTURA, calcule sua area e a quantidade de tinta para pintá-la, cada litro de tinta pinta área de 2m²

a = float (input('Insira a altura da área:'))
l = float (input('Insira a largura da área:'))

al = a * l
t = al/2

print ('Será necessário {:.01f}l de tinta para pintar {:.02f}m²'.format(t,al))