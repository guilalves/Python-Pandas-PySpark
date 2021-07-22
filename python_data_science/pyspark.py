from unidecode import unidecode
from datetime import datetime

import pandas as pd

# variaveis
data_atual = datetime.now()
data_atualizacao = data_atual.strftime('%m/%d/%Y')
data = data_atual.strftime('%Y')
data = int(data)

# data frame
base = {
    'cod_cliente':['1', '2', '3', '4', '5', '6'],
     'Nome':['José', 'Igor', 'Leonardo', 'Humberto', 'Isaias', 'Lucas'],
     'Municipio':['Anápolis', 'Anápolis', 'Anápolis', 'Pato Branco', 'Pato Branco', 'Taua'],
     'Estado':['São Paulo', 'São Paulo', 'São Paulo', 'Rio Grande do Sul', 'Rio Grande do Sul', 'Ceará'],
     'data_nasc':['01-09-1900', '11-09-1977', '11-09-1977', '13-11-1964', '07-07-2002', '05-09-1984'],
     }
df = pd.DataFrame(base)

# contador sequencial
c = df['Municipio'].value_counts().to_frame('count')
new_df = pd.DataFrame(c)

# ordenando por Estado
df.sort_values(by='Estado', inplace=True)

# coluna temporária
df['temp'] = df['data_nasc']

# adicionando uma nova coluna de idade em anos
df['data_nasc'] = pd.to_datetime(df.data_nasc)
df['data_nasc'] = df['data_nasc'].dt.strftime('%Y')
df['data_nasc'] = df['data_nasc'].astype(int)
df['idade'] = data - df['data_nasc']

df['data_nasc'] = df['temp']

# formatando o campo com 0 a esquerda
df["cod_cliente"] = df["cod_cliente"].apply(lambda x: x.zfill(3))

# adicionando nova coluna data de atualizacao
df['data atualizada'] = data_atualizacao

# removendo caracteres especiais do campo Estado
def remove_caracter_especial(columns):
   columns = columns.replace('á', 'a').replace('ã', 'a')
   return columns

df['Estado'] = df['Estado'].apply(remove_caracter_especial)

# Excluindo a coluna temporaria
df.drop(columns=['temp'], inplace=True)

# convertendo dataframe em um arquivo '.parquet'
# df.to_parquet('df.parquet.gzip', compression='gzip')
# pd.read_parquet('df.parquet.gzip')

print(df)

# Contador sequencial
print(new_df)