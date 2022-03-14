#Crie uma tupla preenchida com os 20 colocados da tabela do Campeonato Brasileiro.
#Depois mostre:
#Os 5 primeiros colocados
#Os 4 últimos colocados
#A tabela em ordem alfabetica
#Em que posição está a chapecoense

tabela = ('Corinthians', 'Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Bragantino',
          'Fluminense', 'America-MG', 'Atletico-GO', 'Santos', 'Ceará', 'Inernacional', 'Chapecoense'
          'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventudo', 'Gremio', 'Bahia', 'Sport')

print(f'Os 5 primeiros colocados são: {tabela[0:5]} ')
print(f'Os ultimo 4 colocados são: {tabela[-4:]}')
print(f'A tabela em ordem alfabetica fica assim: {sorted(tabela)}')
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}º posição')


