#Faça um programa que leia um nome de cidade e diga se começa com "Santo"

cidade = str(input('Qual sua cidade? ')).strip()
#dividido = cidade.split()
#print('santo' in (dividido[0].lower())) #a cidade dividida, quero somente a primeira string / joguei tudo pra minusculo e testo
print(cidade[:5].lower() == 'santo') #pego da posição 0 até a 5, jogo tudo pra minusculo e testo