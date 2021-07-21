"""Data frame seleção condicional"""

import pandas as pd
import numpy as np

from numpy.random import randn

SEPARATOR = '#' * 40

np.random.seed(50)

df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print(SEPARATOR)
bol = df > 0 # verificando se os index são maior que 0
print(bol)
print(SEPARATOR)
# resetando o index
df.reset_index()
print(df)
# para ficar fixo o resete, énecessário passar como parâmetro o inplace=True
print(SEPARATOR)
df.reset_index(inplace=True)
print(df)
print(SEPARATOR)
# inserindo uma nova coluna no df
col = 'SP SC RJ BH PE'.split()
print(col)
df['Estado'] = col
print(df)
print(SEPARATOR)
# inserindo a coluna nova Estado como index, deixando ela em primeiro
df.set_index('Estado', inplace=True)
print(df)
print(SEPARATOR)
