import openpyxl

arquivo_entrada = "ArrumarS.xlsx"
planilha = openpyxl.load_workbook(arquivo_entrada)
aba = planilha.active 

supervisores = {
    "LUIZ CLAUDIO": "LUIZ CLAUDIO",
    "MARIA DEBORA": "MARIA DEBORA",
    "WALTER ALVES": "WALTER ALVES",
    "SANDRA ALVES": "SANDRA ALVES",
    "JOAO PAULO": "JOAO PAULO",
    "RAFAEL ALVES": "RAFAEL ALVES",
    "RUBENS FRANCISCO": "RUBENS FRANCISCO",
    "IGOR TROVÃO": "IGOR TROVÃO",
    "MARCOS GUIERME": "MARCOS GUIERME",
    "ALESSANDRA CATELANO": "ALESSANDRA CATELANO",
    "MARCOS FILHO": "MARCOS FILHO",
    "ANDRE VIANA": "ANDRE VIANA",
    "NATANAEL OLIVEIRA": "NATANAEL OLIVEIRA",
    "HERBETH ALVES": "HERBETH ALVES",
    "MARIANA VIANA": "MARIANA VIANA",
    "ELISANGELA SILVA": "ELISANGELA SILVA",
    "THIAGO DIAS": "THIAGO DIAS",
    "MURILO VIRAVA": "MURILO VIRAVA",
    "DANIEL VIEIRA": "DANIEL VIERA",
    "LEANDRO BILLATO": "LEANDRO BILLATTO",
    "CARLOS SILVERIO": "CARLOS SILVERIO",
    "JOICE CEGAL": "JOICE CEGAL",
    "ROGERIO DE SOUZA": "ROGERIO DE SOUZA",
    "ROGERIO MAIA": "ROGERIO MAIA",
    "EDSON APARECIDO": "EDSON APARECIDO",
    "DEBORA AMORIM": "DEBORA AMORIM",
    "JAQUELINE JESUS": "JAQUELINE JESUS",
    "VALDIR PINTO": "VALDIR PINTO",
    "ADILSON CRUZ": "ADILSON CRUZ",
    "ANDRE DIAS": "ANDRE DIAS",
    "DANIEL VIERA": "DANIEL VIERA",
    "VALERIA RODRIGUES": "VALERIA RODRIGUES",
    "LEANDRO BILATTO": "LEANDRO BILATTO",
    "JUNDIAI": "RAFAEL ALVES",
    "SOROCABA": "PAULO",
    "RIBEIRÃO PRETO": "FABIANA",
    "OSASCO": "MAIRA",
    "PRODESP": "MARIA",
    "METRO": "HERBETH ALVES",
    "GONZAGA": "JOSE GONZAGA",
    "FALTA FIXA": "FALTA FIXA",
    "MARCELO SOUZA": "MARCELO SOUZA"
}

resultados = []

for linha in range(2, 3025):
    valor_celula = aba[f"A{linha}"].value
    if valor_celula:
        for nome in supervisores:
            if nome in valor_celula:
                resultados.append(supervisores[nome])
                break
        else:
            ultima_palavra = valor_celula.split()[-1]
            resultados.append(ultima_palavra)
    else:
        resultados.append("")

arquivo_saida = "resultado.xlsx"
nova_planilha = openpyxl.Workbook()
nova_aba = nova_planilha.active
nova_aba.title = "Resultados"

for i, resultado in enumerate(resultados, start=2):
    nova_aba[f"A{i}"] = resultado

nova_planilha.save(arquivo_saida)

print(f"Arquivo '{arquivo_saida}' criado com sucesso!")
