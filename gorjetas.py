#Importando base de dados

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

#Analise 1 - valor da conta e gorjeta
'''valor_gorjeta = sns.scatterplot(x = 'valor_da_conta', y = 'gorjeta', data = gorjetas)
plt.show() #Visualmente o valor da gorjeta aumenta conforme aumenta o valor da conta'''


print('A base de dados contém {} registros \n'. format(gorjetas.shape[0]))
print('Registros não nulos:')
print(gorjetas.count(), '\n')


#criando campo porcentagem
print(gorjetas.info(),'\n')
gorjetas['porcentagem'] = gorjetas['gorjeta']/gorjetas['valor_da_conta']
gorjetas['porcentagem'] = gorjetas['porcentagem'].round(2)
print(gorjetas.head(), '\n')

porcentagem_conta = sns.scatterplot(x = 'valor_da_conta', y = 'porcentagem', data = gorjetas)
porcentagem_conta.get_figure()
porcentagem_conta.figure.suptitle('Valor da conta x Gorjeta')
plt.show()

#visualmente p valor da conta nao é proporcional ao valor dar gorjeta


'''porcentagem_conta_linha = sns.relplot(x = 'valor_da_conta', y = 'porcentagem', kind='line', data = gorjetas)
plt.show()'''

'''sns.lmplot(x = 'valor_da_conta', y = 'porcentagem', data = gorjetas)
plt.show()'''