#Tipos de dados primitivos

int = números inteiros (7,-4,0,451)
float = números reais (4.5, 2.35, 0.005)
bool = valores lógicos (True ou False) #Se tem valor ou não e sempre a primeira leitra do True e False MAIÚSUCLA
str = caracteres ou string ('Olá', '7.5')
a.isnumeric # verifica s eé numero
a.isalpha # verifica se é letra
a.isupper # verifica se é tudo maiusculo
a.islower # verifica se é tudo minusculo
a.isspace # verifica se tem espaço
a,isalpha # verifica se é alfa numerico
a.istitle # verufuca se está capitalizada
#VARIAVEK PONTO METODO

#Ordem de precedencia

#1 - ()
#2 - **
#3 - *, //, /, %
#4 - +, -

# ** = Potencia
# // = Divisão inteira
# % = Resti da divisão

## raiz quadrada = 81**(1/2) (valor elevado a meio)
#math.
#biblioteca import math
#ceil arredonda pra cima
#floor arredonda pra baixo
#trunc elimina todos números após a virgula
#pow calcula potencia
#sqrt calcula raiz quadrada
#factorial calcula fatorial

from math import ceil  #importa só uma
import math #importa tudo
import random
#O método random.choice() retorna um elemento selecionado aleatoriamente da sequência especificada.


CADEIA DE CARCTERES
frase = 'Natanael Vaz Gomes' #tem 13 campos
len(frase) #vai imprimir o numero do campo '13'
frase.count('o') # vai contar quantas vezes aparece determinada letra, no caso o "o"
frase.find('ael') #em que momento encontrou isso e mostra a posição "5 por exemplo"
frase.find('Android') #retorna o valor -1 se não achar nada relacionado na string
frase.rfind('A') #procura do lado direito, orientado a utilizar para achar a ultima
'Vaz' in frase #existe "Vaz" na frase? True or False
frase.replace('Gomes', 'Vaz') # ele substitui. Onde tem Gomes, vai substituir por Vaz
frase.upper() #deixa tudo em maiusculo
frase.lower() #deixa tudo em minusculo
frase.capitalize() #coloca tudo em minusculo, deixando somente a PRIMEIRA maiuscula
frase.title() #coloca a primeira em maiusculo de cada PALAVRA
frase.strip() #remove todos espaços inúteis, como no começo ou fim do texto digitado
frase.rstrip() #remove os últimas da direita
frase.lstrip() #remove os espaços da esquerda
frase.split() #divide a string, ele gera uma lista com os caracteres inseridos Ex.: [Natanael][Vaz][Gomes]
'-'.join(frase) #junta todos elementos separando pelo caractere no inicio "-", se quiser espaço ''.join(frase)

#Condições Aninhadas
if #se
elif #se não se (else if) pode ter vários
else #senão

n = 1
while n != 0:
    n = int(input('Digite um valor: '))


LISTA = ['ELEMENTOS', 'ELEMENTOS']
lista.append('ELEMENTO2') #Adiciona um elemento ao fim da lista
lista.insert(0,'ELEMENTO3') #NA POSIÇÃO TAL, ADICIONA TAL COISA
del lista[2] #Apaga um elemento na posição 2
lista.pop[2] #Apaga um elemento na posição 2 #Sem indice, ele remove o ultimo
lista.remove['ELEMENTO2'] #Apaga o elemento pelo NOME
valores = [0,4,3,1,5,2]
valores.sort() #Ordena os valores





