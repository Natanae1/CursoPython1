#Melhore o jogo do desafio 28. Mas agora vai advinhar ate acertar e no final mostre quantas tentativas necessárias
import random
print('Eu escolhi um número entre 0 e 10.')
n = random.randint(0,10)
palpite = 0
acertou = False
while not acertou:
    num = int(input('Tente advinhar: '))
    palpite += 1
    if num == n:
        acertou = True
        print('Você acertou!')
    else:
        print('EROOOOOOOOW')
        if
print('Só precisou de {} tentativas' .format(palpite))
