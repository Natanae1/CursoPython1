# Faça um programa que leia um angulo e mostre na tela o valor do seno, cosseno e tangente

import math
a = float (input ('Insira o ângulo desejado: '))
sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)

print('O angulo de {} equivale ao seno {}, cosseno {} e tangente {}' .format(a,sen,cos,tan))