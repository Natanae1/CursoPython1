#Desenvolva um programa que pergunte a distancia de uma viagem. Calcule o preço da passagem sendo R$0,50 por km para viagens de até 200km e
# R$0,45 para viagens mais longas

d = float(input('Qual distancia da viagem? '))

if d <= 200:
    print('A passagem custará R${:.2f} ' .format(d*0.50))
else:
    print('A passagem custará R${}' .format(d*0.45))
