import os
import re
import shutil
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageEnhance, ImageFilter
import fitz
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
OCR_CONFIG = r'--oem 3 --psm 6'

EMPRESAS_DISPONIVEIS = {'Works': '02', 'Qualitech': '02', 'Partner': '07', 'Presseg': '01'}
TIPO_DOCS = {'Folha de Ponto': '01', 'FT': '02'}
ANO = {str(y): str(y)[-2:] for y in range(2020, 2026)}
MES = {'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04',
       'Maio': '05', 'Junho': '06', 'Julho': '07', 'Agosto': '08',
       'Setembro': '09', 'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'}

def pdf_para_imagens(caminho_pdf):
    imagens = []
    try:
        doc = fitz.open(caminho_pdf)
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            imagens.append(img)
    except Exception as e:
        print(f"[ERRO ABRIR PDF] {caminho_pdf}: {e}")
    return imagens

def preprocessar_imagem(img):
    img = img.convert("L")
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    return img

def extrair_re(texto):
    print("\n---- TEXTO EXTRAÍDO ----")
    print(texto[:1000])
    print("---- EXTRAINDO RE ----")

    # 1ª
    match = re.search(r'Registro[:\-]?\s*(\d{5,})', texto, re.IGNORECASE)
    if not match:
        match = re.search(r'\b(?:registro|reg)\s*[:\-]?\s*(\d{5,})', texto, re.IGNORECASE)

    if match:
        return match.group(1)

    # 2ª
    linhas = texto.strip().splitlines()
    for linha in reversed(linhas):
        if " - Nome" in linha:
            tentativa = re.search(r'(\d{5,})\s*-\s*Nome', linha)
            if tentativa:
                return tentativa.group(1)
    return "0000"

def limpar_nome(nome):
    return re.sub(r'[<>:"/\\|?*\n\r\t]', '_', nome)

def gerar_nome_unico(nome_base, destino):
    novo_nome = os.path.join(destino, f"{nome_base}.pdf")
    contador = 1
    while os.path.exists(novo_nome):
        novo_nome = os.path.join(destino, f"{nome_base}_{contador}.pdf")
        contador += 1
    return novo_nome

def renomear_pdfs(pasta_entrada, pasta_saida, empresa, mes, ano, tipodoc="1"):
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.lower().endswith(".pdf"):
            caminho_pdf = os.path.join(pasta_entrada, nome_arquivo)
            imagens = pdf_para_imagens(caminho_pdf)

            if not imagens:
                print(f"[IGNORADO] {nome_arquivo} não pôde ser processado.")
                continue

            texto_completo = ""
            for img in imagens:
                img_pre = preprocessar_imagem(img)
                texto = pytesseract.image_to_string(img_pre, lang='eng', config=OCR_CONFIG)
                texto_completo += texto

            registro = extrair_re(texto_completo)
            print(f"Arquivo: {nome_arquivo} ➜ RE extraído: {registro}")

            paginas = len(imagens)
            codigo = f"{empresa}{mes}{ano}{paginas}{tipodoc}{registro}"
            codigo_limpo = limpar_nome(codigo)
            novo_nome = gerar_nome_unico(codigo_limpo, pasta_saida)

            try:
                shutil.move(caminho_pdf, novo_nome)
                print(f"Renomeado para: {novo_nome}")
            except Exception as e:
                print(f"[ERRO RENOMEAR] {e}")

    messagebox.showinfo("Concluído", "Renomeação finalizada com sucesso.")

def selecionar_pasta():
    return filedialog.askdirectory(title="Selecione a pasta com PDFs")

def selecionar_pasta_destino():
    return filedialog.askdirectory(title="Selecione a pasta DESTINO para os PDFs renomeados")

def iniciar_script():
    empresa_nome = combo_empresa.get()
    tipodoc_nome = combo_tipodoc.get()
    ano = combo_ano.get()
    mes = combo_mes.get()

    if not (empresa_nome and mes and ano and tipodoc_nome):
        messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
        return

    empresa_codigo = EMPRESAS_DISPONIVEIS.get(empresa_nome, "0")
    tipodoc_codigo = TIPO_DOCS.get(tipodoc_nome, "1")
    ano = ANO.get(ano, "25")
    mes = MES.get(mes, "01")

    pasta_entrada = selecionar_pasta()
    if not pasta_entrada:
        return

    pasta_saida = selecionar_pasta_destino()
    if not pasta_saida:
        return

    renomear_pdfs(pasta_entrada, pasta_saida, empresa_codigo, mes, ano, tipodoc_codigo)

# Interface
janela = tk.Tk()
janela.title("Codificador de PDFs")
janela.geometry("280x180")

tk.Label(janela, text="Empresa:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
combo_empresa = ttk.Combobox(janela, values=list(EMPRESAS_DISPONIVEIS.keys()), state="readonly")
combo_empresa.grid(row=0, column=1)
combo_empresa.set(list(EMPRESAS_DISPONIVEIS.keys())[0])

tk.Label(janela, text="Tipo de Documento:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
combo_tipodoc = ttk.Combobox(janela, values=list(TIPO_DOCS.keys()), state="readonly")
combo_tipodoc.grid(row=1, column=1)
combo_tipodoc.set(list(TIPO_DOCS.keys())[0])

tk.Label(janela, text="Ano:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
combo_ano = ttk.Combobox(janela, values=list(ANO.keys()), state="readonly")
combo_ano.grid(row=2, column=1)
combo_ano.set(list(ANO.keys())[0])

tk.Label(janela, text="Mês:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
combo_mes = ttk.Combobox(janela, values=list(MES.keys()), state="readonly")
combo_mes.grid(row=3, column=1)
combo_mes.set(list(MES.keys())[0])

tk.Button(janela, text="Selecionar Pastas e Iniciar", command=iniciar_script).grid(row=4, column=0, columnspan=2, pady=15)

janela.mainloop()
