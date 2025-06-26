import pandas as pd
from datetime import datetime

df = pd.read_excel('tempofhouse.xlsx', header=0)

coluna = df.columns[0] 
df.rename(columns={coluna: "Data_Admissao"}, inplace=True)

df['Data_Admissao'] = pd.to_datetime(df['Data_Admissao'], format="%d/%m/%Y", errors='coerce')

df['Tempo_de_Casa'] = df['Data_Admissao'].apply(lambda x: None if pd.isna(x) else '')

hoje = datetime.today()

def calcular_tempo_casa(data_admissao):
    anos = hoje.year - data_admissao.year - ((hoje.month, hoje.day) < (data_admissao.month, data_admissao.day))
    meses = (hoje.year - data_admissao.year) * 12 + (hoje.month - data_admissao.month)
    meses_restantes = meses % 12
    dias = (hoje - data_admissao).days
    # horas = (hoje - data_admissao).seconds // 3600
    # minutos = (hoje - data_admissao).seconds % 3600 // 60  
    # segundos = (hoje - data_admissao).seconds % 60


    if anos >= 1:
        return f"{anos} anos e {meses_restantes} meses"
    else:
        if meses_restantes == 0:
            return f"{dias} dias"
        elif meses_restantes == 1:
            return f"{meses_restantes} mês"
        return f"{meses} meses"

df.loc[df['Data_Admissao'].notna(), 'Tempo_de_Casa'] = df['Data_Admissao'].apply(calcular_tempo_casa)

df.to_excel("Bases Tratadas/res_extraidos.xlsx", index=False)

print("Arquivo Excel gerado: resultado.xlsx")