# Faça um programa que leia um angulo e mostre na tela o valor do seno, cosseno e tangente

import math
a = float (input ('Insira o ângulo desejado: '))
sen = math.sin(math.radians(a)) #seno recebe math.sin, que é o seno, porém ele precisa converter para radiano
cos = math.cos(math.radians(a)) #com o radiano calculado, o math.cos calcula o cosseno
tan = math.tan(math.radians(a))

print('O angulo de {} tem o SENO de {:.2f}, COSSENO {:.2f} e TANGENTE {:.2f}' .format(a,sen,cos,tan))