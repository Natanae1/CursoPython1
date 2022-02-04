#Reçafa o desafio 9 da tabuada usando o laço for
print('--=' * 5, end='')
print(' TABUADA', '--=' * 5)
num = int(input('Escolha um número: '))
for c in range(1,10):
    print('{} x {} = {}' .format(num, c, num*c ))
print('GOSTOU ? :)')