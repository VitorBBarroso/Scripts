import os
from dbfread import DBF
import pandas as pd
from pyspark.sql import SparkSession

caminho_pasta = 'S:\\dbfs'

spark = SparkSession.builder \
    .appName("FoxPro DBF Reader") \
    .getOrCreate()

for arquivo in os.listdir(caminho_pasta):
    if arquivo.lower().endswith('.dbf'):
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        nome_tabela = os.path.splitext(arquivo)[0].lower()

        try:
            registros = DBF(caminho_arquivo, encoding='latin1')
            df_pd = pd.DataFrame(iter(registros))

            if df_pd.empty:
                print(f"[AVISO] Tabela '{nome_tabela}' está vazia, pulando.")
                continue

            df_spark = spark.createDataFrame(df_pd)

            df_spark.createOrReplaceTempView(nome_tabela)

            print(f"[OK] Tabela '{nome_tabela}' carregada com {df_spark.count()} registros.")

        except Exception as e:
            print(f"[ERRO] Falha ao carregar '{arquivo}': {e}")
