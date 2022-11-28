import pandas as pd

population = (
{
'Country': ['Belgium', 'India', 'Japan'],
'Population': [12345, 67891011, 98765]
})

dados = pd.DataFrame(population)

print(dados, '\n')

colunas = {'Country':'País', 'Population':'População'}
dados = dados.rename(columns=colunas)
print(dados, '\n')

paises = {'Belgium':'Bélgica', 'India':'Índia', 'Japan':'Japão'}
dados.Country = dados.Country.map(paises)
print(dados, '\n')