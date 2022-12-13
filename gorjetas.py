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
print(gorjetas.dia_da_semana.unique(), '\n')
'''sns.catplot(x='dia_da_semana', y = 'valor_da_conta', data = gorjetas)
sns.relplot(x='valor_da_conta', y = 'porcentagem', hue = 'dia_da_semana', data = gorjetas)
sns.relplot(x='valor_da_conta', y = 'gorjeta', hue = 'dia_da_semana', col = 'dia_da_semana', data = gorjetas)
sns.relplot(x='valor_da_conta', y = 'porcentagem', hue = 'dia_da_semana', col = 'dia_da_semana', data = gorjetas)
sns.lmplot(x='valor_da_conta', y = 'porcentagem', hue = 'dia_da_semana', col = 'dia_da_semana', data = gorjetas)
plt.show()'''


media_geral_gorjetas = gorjetas['gorjeta'].mean()
print('A média geral das gorjetas é de {}'. format(media_geral_gorjetas),'\n')

medias = gorjetas.groupby(['dia_da_semana']).mean()[['valor_da_conta', 'gorjeta', 'porcentagem']]
print(medias, '\n')

print('Frequencia dos dias')
gorjetas['dia_da_semana'].value_counts()

#Teste de hipotese
#Hnull: a distribuição do valor da conta é igual no sabado e no domingo
#Halt: a distribuição do valor da conta é igual no sabado e no domingo

valor_conta_domingo = gorjetas.query("dia_da_semana == 'Domingo'").valor_da_conta
valor_conta_sabado = gorjetas.query("dia_da_semana == 'Sábado'").valor_da_conta

r2 = ranksums(valor_conta_domingo, valor_conta_sabado)
print('O valor do p-value é {}'.format(r2.pvalue), '\n')
#Hnull: a distribuição do valor da conta é igual no sabado e no domingo
    
    
print(gorjetas.head(), '\n')

#Análise 4 - Hora do dia

print(gorjetas.hora_do_dia.unique())

#sns.catplot(x ='hora_do_dia', y = 'valor_da_conta', data = gorjetas)
#sns.catplot(x ='hora_do_dia', y = 'valor_da_conta', kind = 'swarm', data = gorjetas)
#sns.violinplot(x = 'hora_do_dia', y = 'valor_da_conta', data = gorjetas)
#sns.boxplot(x = 'hora_do_dia', y = 'valor_da_conta', data = gorjetas)
almoco = gorjetas.query("hora_do_dia == 'Almoço'").valor_da_conta
sns.displot(almoco, kde=False)

jantar = gorjetas.query("hora_do_dia == 'Jantar'").valor_da_conta
sns.displot(jantar, kde=False)
#plt.show()

print(gorjetas.groupby(['hora_do_dia']).mean()[['valor_da_conta', 'gorjeta', 'porcentagem']], '\n')

#Teste de hipotese
#Hnull: a distribuição do valor da conta é igual no almoço e no jantar
#Halt: a distribuição do valor da conta não é igual no almoço e no jantar
#é menor do que 0.005, logo não são iguais

r2 = ranksums(jantar, almoco)
print('O valor do p-value é de {}'. format(r2.pvalue.round(3)), '\n')

porcentagem_almoco = gorjetas.query("hora_do_dia == 'Almoço'").porcentagem
print(porcentagem_almoco, '\n')
porcentagem_jantar = gorjetas.query("hora_do_dia == 'Jantar'").porcentagem
print(porcentagem_jantar, '\n')

#Teste de hipotese
#Hnull: a distribuição da taxa da gorjeta é igual no almoço e no jantar
#Halt: a distribuição da taxa da gorjeta não é igual no almoço e no jantar
#é maior do que 0.005, , logo são iguais

r3 = ranksums(porcentagem_almoco, porcentagem_jantar)
print('O valor do p-value é de {}'. format(r2.pvalue.round(3)), '\n')
