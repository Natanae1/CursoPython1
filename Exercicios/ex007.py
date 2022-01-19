#Faça um programa que leia duas notas do aluno e mostre sua média

n1 = float (input ('Insira a primeira nota: '))
n2 = float (input ('Insira a segunda nota: '))
m = (n1+n2)/2

print('A primeira nota inserida é:{:.1f}',n1)
print('A segunda nota é:{:.1f} ',n2)
print('A soma das duas notas é:{:.1f}' ,n1+n2)
print('A média foi:{:.1f} ',m)

if m >= 6:
    print('A sua média foi {}, você está aprovado!' .format(m))

else:
    print('A sua média foi {}, você está reprovado.' .format(m))



