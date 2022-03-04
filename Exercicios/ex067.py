print('--=' * 5, end='')
print(' TABUADA', '--=' * 5)
c = 0
num = int(input('Escolha um número: '))
while True:
    for c in range(1, 10):
         print('{} x {} = {}'.format(num, c, num * c))
    num = int(input('Digite outro valor: '))
    if num < 0:
        break
print('FIM! :)')