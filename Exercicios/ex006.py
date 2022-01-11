#Faça um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada

n1 = int (input ('Digite um numero: '))
print('O número digitado foi o {}.\nO dobro desse número é {}.\nO triplo é {}.\nA raiz quadrada: {:.2f}' .format(n1,n1*2,n1*3,n1**(1/2)))