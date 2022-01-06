#Faça um programa que leia algo inserido e informe todas informações

a = input ('Digite algo: ')
print('Qual é esse tipo de dado inserido? ' ,type(a))
print('Só tem espaços?' ,a.isspace())
print('É um número? ' ,a.isnumeric())
print ('Possui letras ?' ,a.isalpha())
print('É alfanumerico? ',a.isalnum())
print('Está todo em letras maiúsculas ?' ,a.isupper())
print('Está todo em letras minusculas? ' ,a.islower())
print('A primeira letra está capitalizada? ' ,a.istitle())



