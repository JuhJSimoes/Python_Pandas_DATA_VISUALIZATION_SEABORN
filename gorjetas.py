#Importando base de dados

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ranksums

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

'''porcentagem_conta = sns.scatterplot(x = 'valor_da_conta', y = 'porcentagem', data = gorjetas)
porcentagem_conta.get_figure()
porcentagem_conta.figure.suptitle('Valor da conta x Gorjeta')
porcentagem_conta.set_title('Análise do valor da gorjeta em função do valor da conta')
porcentagem_conta.set(xlabel = 'Valor da conta', ylabel = 'Valor da gojeta')
porcentagem_conta_img = porcentagem_conta.get_figure()
porcentagem_conta_img.savefig('image.png')
plt.show()'''

#visualmente p valor da conta nao é proporcional ao valor dar gorjeta
'''porcentagem_conta_linha = sns.relplot(x = 'valor_da_conta', y = 'porcentagem', kind='line', data = gorjetas)
plt.show()'''

'''sns.lmplot(x = 'valor_da_conta', y = 'porcentagem', data = gorjetas)
plt.show()'''

#Analise 2 - sobremesa
sobremesa = gorjetas[gorjetas.sobremesa == 'Sim'].describe()
print(sobremesa, '\n')

'''sns.catplot(x = 'sobremesa', y = 'gorjeta', data = gorjetas)
sns.relplot(x = 'valor_da_conta', y = 'gorjeta', hue = 'sobremesa',data = gorjetas)
sns.relplot(x = 'valor_da_conta', y = 'gorjeta', hue = 'sobremesa',col = 'sobremesa' ,data = gorjetas)
sns.lmplot(x = 'valor_da_conta', y = 'gorjeta', col = 'sobremesa', hue = 'sobremesa', data = gorjetas)
sns.lmplot(x = 'valor_da_conta', y = 'porcentagem', col = 'sobremesa', hue = 'sobremesa', data = gorjetas)
sns.relplot(x = 'valor_da_conta', y = 'gorjeta', col = 'sobremesa', hue = 'sobremesa', kind = 'line', data = gorjetas)
plt.show()'''
# Visualmente existe diferença no valor da gorjeta entre aqueles que pediram sobremesa e os que não pediram.


'''Teste de hipótese 
    Hnull: a distribuição da taxa da gorjeta é a mesma nos 2 grupos.
    Halt: a distribuição da taxa da gorjeta não é a mesma nos dois grupos'''
    
sobremesa = gorjetas.query('sobremesa == "Sim"').porcentagem
sem_sobremesa = gorjetas.query('sobremesa == "Não"').porcentagem
print(sobremesa, sem_sobremesa, '\n')

r = ranksums(sobremesa, sem_sobremesa)
print('O valor do p-value é {}'.format(r.pvalue))

#Hnull: a distribuição da taxa da gorjeta é a mesma nos 2 grupos.

print(gorjetas.head(), '\n')
print(gorjetas.dia_da_semana.unique())
#sns.catplot(x='dia_da_semana', y = 'valor_da_conta', data = gorjetas)
#sns.relplot(x='valor_da_conta', y = 'porcentagem', hue = 'dia_da_semana', data = gorjetas)
#sns.relplot(x='valor_da_conta', y = 'gorjeta', hue = 'dia_da_semana', col = 'dia_da_semana', data = gorjetas)
#sns.relplot(x='valor_da_conta', y = 'porcentagem', hue = 'dia_da_semana', col = 'dia_da_semana', data = gorjetas)
sns.lmplot(x='valor_da_conta', y = 'porcentagem', hue = 'dia_da_semana', col = 'dia_da_semana', data = gorjetas)
plt.show()
    
