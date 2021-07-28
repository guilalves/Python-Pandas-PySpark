import pandas as pd

# Base de dados para um dataframe
dados = {
    'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Nome': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Venda': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(dados)

# Group By
group = df.groupby('Empresa')

# soma
group.sum()

# media
group.mean()

# print(df)
print()
print(group.describe())

# contador
print(group.count())