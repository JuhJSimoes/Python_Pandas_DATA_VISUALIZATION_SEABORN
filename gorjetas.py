#Importando base de dados

import pandas as pd

dados = pd.read_csv('tips.csv')
print(dados.head())