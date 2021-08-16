import pyspark.sql.functions as F

from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import SparkSession

"""
Caso 1 – Adicionar 1 coluna com um contador sequencial por Município e ordenar por Estado.
Caso 2 - Adicionar 1 coluna com a Idade em anos e na coluna cod_cliente formatar o campo com 3 posições a esquerda completando com “0”. 
Caso 3 - Adicionar 1 coluna com a data de atualização, preenchendo com a data do dia da execução e retirar os caracteres especiais do campo Estado.
converter o arquivo para (.parquet)
"""

spark = (SparkSession.builder
    .master("local[*]")
    .appName("estudando-dataframes")
    .getOrCreate())

data = (
    ['1', 'José', 'Anápolis', 'São Paulo', '01-09-1900'],
    ['2', 'Igor', 'Anápolis', 'São Paulo', '11-09-1977'],
    ['3', 'Leonardo', 'Anápolis', 'São Paulo', '21-12-2000'],
    ['4', 'Humberto', 'Pato Branco', 'Rio Grande do Sul', '13-11-1964'],
    ['5', 'Isaias', 'Pato Branco', 'Rio Grande do Sul', '07-07-2002'],
    ['6', 'Lucas', 'Tauá', 'Ceará', '05-09-1984'],
)

schema = (StructType([
    StructField('cod_cliente', StringType(), True),
    StructField('nome', StringType(), True),
    StructField('municipio', StringType(), True),
    StructField('estado', StringType(), True),
    StructField('data_nasc', StringType(), True),
]))

df = spark.createDataFrame(data=data, schema=schema)

# Contador sequencial por municipio
df.groupBy('municipio').count().sort('municipio', ascending=True).show(truncate=False)

# Ordenando a coluna estado
df = df.orderBy('estado')

# Adicionando uma coluna nova de idade em anos
df = df.withColumn('idade', F.date_format(F.current_timestamp(), "yyyy").cast('integer') \
                   - F.substring(F.col('data_nasc'), 7, 4).cast('integer'))

# Adicionando 0 a esquerda na coluna cod_cliente
df = df.withColumn('cod_cliente', F.lpad(df.cod_cliente, 4, '0'))

# Data atualização
df = df.withColumn('data_atualizacao', F.date_format(F.current_timestamp(), "dd-MM-yyyy | HH:mm:ss"))

# data de execução
df = df.withColumn('data_execucao', F.date_format(F.current_timestamp(), "dd-MM-yyyy"))

# removendo caracteres especiais da coluna estado
df = df.withColumn('estado', F.regexp_replace('estado', 'á', 'a') \
    ).withColumn('estado', F.regexp_replace('estado', 'ã', 'a'))

"""
Convert PySpark Dataframe to Pandas DataFrame
pandasdf = df.toPandas()
print(pandasdf)
"""

df.show(truncate=False)
