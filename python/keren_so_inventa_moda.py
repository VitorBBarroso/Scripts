import fitz  # PyMuPDF
import pandas as pd
import re

# Abre o PDF
doc = fitz.open(r"C:\Users\ADM\Documents\Scritps\python\works001.pdf")


# Lista para armazenar os dados extraídos
dados = []

# Expressão regular para RE + Nome
padrao = re.compile(r"(\d{5,})\s+([A-Z\sÇÃÁÉÍÓÚÊÔÂ]+)")

# Percorrer todas as páginas
for pagina in doc:
    texto = pagina.get_text()
    matches = padrao.findall(texto)

    for re_, nome in matches:
        dados.append({'RE': re_, 'NOME COMPLETO': nome.title()})

# Criar DataFrame e exportar
df = pd.DataFrame(dados)
df.to_excel("Bases Tratadas/res_extraidos.xlsx", index=False)

