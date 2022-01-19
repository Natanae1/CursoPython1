#Faça um programa que leia a velocidade do carro, se ele ultrapassar 80km/h, será multado em 7 R$ a cada km acima

v = int(input('Qual velocidade do carro ? '))

if v > 80:
    print('A velocidade máxima permitida é de 80km/h, você está acima da velocidade, será multado em R${:.2f} reais' .format((v - 80) * 7))
else:
    print('Está nos limites de velocidade, boa viagem.')