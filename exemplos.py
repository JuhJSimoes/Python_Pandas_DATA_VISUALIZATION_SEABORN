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
dados['País'] = dados['País'].map(paises)
print(dados, '\n')



boletim = ({
    'Aluno' : ['Márcia', 'Lucas', 'Ana', 'Flávio'],
    'Nota_1' : [10, 8, 5, 4],
    'Nota_2' : [7, 4, 8, 5],
    'Nota_3' : [6, 7, 4, 9]
})

dados = pd.DataFrame(boletim)

print(dados, '\n')

dados['Média'] = ((dados.Nota_1 + dados.Nota_2 + dados.Nota_3) / 3).round(2)

print(dados, '\n')


