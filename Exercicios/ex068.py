#Programa que joga par ou ímpar e mostra o total de vitórias consecutivas
from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer PAR ou ÍMPAR ?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. O total é {total}')
    if total % 2 == 0:
        print('DEU PAR.' , end=' ')
    else:
        print('DEU ÍMPAR.' ,end=' ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente. . .')
print(f'GAME OVER! Você venceu {v} vezes')