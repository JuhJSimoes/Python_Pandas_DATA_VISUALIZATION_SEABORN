#Importando base de dados

import pandas as pd

dados = pd.read_csv('tips.csv')
print(dados.head(), '\n')

#Tradução

#print(dados.columns)

renomear = {
    'total_bill' : 'valor_da_conta', 
    'tip': 'gorjeta', 
    'dessert': 'sobremesa', 
    'day': 'dia_da_semana', 
    'time': 'hora_do_dia', 
    'size':'total_de_pessoas'
    }

gorjetas = dados.rename(columns = renomear)

gorjetas['sobremesa'].unique()
sim_nao = {'No' : 'Não', 'Yes' : 'Sim'}

gorjetas['sobremesa'] = gorjetas['sobremesa'].map(sim_nao)
print(gorjetas.head(), '\n')

print(gorjetas['dia_da_semana'].unique())

dias = {
    'Sun' : 'Domingo',
    'Sat' : 'Sábado',
    'Thur' : 'Quinta-Feira',
    'Fri' : 'Sexta-Feira'
}

gorjetas['dia_da_semana'] = gorjetas['dia_da_semana'].map(dias)
#print(gorjetas['dia_da_semana'].unique(), '\n')
print(gorjetas.head(), '\n')

print(gorjetas['hora_do_dia'].unique(), '\n')

hora = {
    'Dinner' : 'Jantar', 
    'Lunch' : 'Almoço'
}

gorjetas['hora_do_dia'] = gorjetas['hora_do_dia'].map(hora)
print(gorjetas.head(), '\n')