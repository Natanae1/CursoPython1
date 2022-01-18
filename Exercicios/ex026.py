#Leia uma frase e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece primeiro
#Em que posição aparece pela ultima vez

frase = str(input('Insira uma frase: ')).strip()
print('Esta frase possui {} letras "A"' .format(frase.lower().count('a')))  #joguei tudo pra minusculo e contei o A)
print('A letra "A" aparece primeiro na posição {}.' .format(frase.lower().find('a'))) #se eu quiser colocar nas posições a partir de 1, só colocar +1
print('A letra "A" aparece por última na posição {}.' .format(frase.lower().rfind('a')))
