#Crie um programa que leia duas notas do aluno: Média abaixo de 5.0, reprovado. Média entre 5.0 e 6.9, recuperação. Média 7 ou superior, aprovado

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
md = (n1 + n2) / 2
if md < 5:
    print('Você não atingiu a média de 5, infelizmente está REPROVADO !')

elif md >= 5 and md <= 6.9:
    print('Você atingiu a nota {}, terá chances de ser aprovado na RECUPERAÇÃO.' .format(md))

else:
    print('Parabéns, você atingiu a nota {}, está APROVADO!' .format(md))
