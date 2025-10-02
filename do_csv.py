import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# --- 1. Configurações ---
NUM_LINHAS = 500
NOME_ARQUIVO = 'vendas_com_erros_v2.csv'
SEMENTE = 42 # Para resultados reproduzíveis

np.random.seed(SEMENTE)
random.seed(SEMENTE)

# --- 2. Produtos e Faixas de Preço (Base) ---

produtos_precos_base = {
    'Notebook Ultra Pro': 4500.00,
    'Smartphone X': 2200.00,
    'Fone de Ouvido Max': 450.00,
    'Tablet Lite': 950.00,
    'Câmera DSLR Z10': 3800.00,
    'Monitor Gamer 27"': 1600.00,
    'Mouse Sem Fio Ergonomico': 120.00,
    'Teclado Mecânico RGB': 350.00,
    'SSD 1TB Ultra': 600.00,
    'Placa de Vídeo RTX 4080': 7000.00,
    'Roteador Mesh Dual-Band': 550.00,
    'Impressora Laser Colorida': 1100.00,
    'Webcam Full HD': 180.00,
    'Smartwatch Esportivo': 780.00,
    'Carregador Portátil 20000mAh': 150.00,
    'Mochila Antifurto Tech': 200.00,
    'Luminária Smart LED': 85.00,
    'Caixa de Som Bluetooth Premium': 300.00,
    'Licença Software Pro': 1500.00,
    'Cabo HDMI 2.1': 50.00,
    'Pendrive USB 3.0 128GB': 75.00,
    'Kit Limpeza Eletrônicos': 35.00
}

produtos = list(produtos_precos_base.keys())

# --- 3. Geração de Dados Fictícios (Com Erros) ---

# Geração dos nomes de produto
nome_produto_limpo = np.random.choice(produtos, NUM_LINHAS)
nome_produto_sujo = []

for nome in nome_produto_limpo:
    if random.random() < 0.10: # 10% de chance de erro no nome
        if random.random() < 0.3:
            nome = nome.upper()
        elif random.random() < 0.6:
            nome = nome.lower()
        elif random.random() < 0.8:
            nome = " " + nome.strip() + " "
        else:
            nome = nome.replace('a', '@').replace('e', '3')
    
    nome_produto_sujo.append(nome)


# Geração dos valores (Com Erros)
valores = []
for nome in nome_produto_limpo:
    base = produtos_precos_base[nome]
    variacao = np.random.uniform(0.9, 1.1)
    valor_venda = base * variacao
    valores.append(round(valor_venda, 2))

for i in range(NUM_LINHAS):
    if random.random() < 0.15: # 15% de chance de erro no valor
        erro_tipo = random.choice(['ZERO', 'STRING', 'EXTREMO', 'NAN'])
        if erro_tipo == 'ZERO':
            valores[i] = 0.0
        elif erro_tipo == 'STRING':
            valores[i] = 'INVÁLIDO'
        elif erro_tipo == 'EXTREMO':
            valores[i] = random.choice([0.01, 99999.99])
        elif erro_tipo == 'NAN':
            valores[i] = np.nan


# Geração das datas de venda (Com Erros e CORRIGIDO o erro de tipo)
data_fim = datetime.now()
data_inicio = data_fim - timedelta(days=90)

dias_aleatorios = np.random.randint(0, 91, NUM_LINHAS)
horas_aleatorias = np.random.randint(0, 24, NUM_LINHAS)
minutos_aleatorios = np.random.randint(0, 60, NUM_LINHAS)
segundos_aleatorios = np.random.randint(0, 60, NUM_LINHAS)

# Geração da lista de objetos datetime puros
datas_venda_datetime = [
    data_inicio + timedelta(days=int(d), hours=int(h), minutes=int(m), seconds=int(s))
    for d, h, m, s in zip(dias_aleatorios, horas_aleatorias, minutos_aleatorios, segundos_aleatorios)
]

# Introdução de erros de formatação e nulos na data
datas_venda_sujas = []
for data in datas_venda_datetime:
    if random.random() < 0.15: # 15% de chance de erro no formato da data
        erro_tipo = random.choice(['FORMATO_1', 'FORMATO_2', 'NAN'])
        if erro_tipo == 'FORMATO_1':
            datas_venda_sujas.append(data.strftime('%d/%m/%Y %H:%M')) # Ex: 01/10/2025 15:30
        elif erro_tipo == 'FORMATO_2':
            datas_venda_sujas.append(data.strftime('%Y-%m-%d')) # Ex: 2025-10-01 (sem hora)
        elif erro_tipo == 'NAN':
            datas_venda_sujas.append(np.nan)
    else:
        datas_venda_sujas.append(data.strftime('%Y-%m-%d %H:%M:%S')) # Formato padrão


# --- 4. Criação do DataFrame e Salvamento no CSV (CORRIGIDO) ---

dados = pd.DataFrame({
    'nome produto': nome_produto_sujo,
    'valor': valores,
    'data venda': datas_venda_sujas # A coluna data venda agora está incluída
})

# Salvando no arquivo CSV
dados.to_csv(NOME_ARQUIVO, index=False, decimal=',', sep=';')

print(f"Arquivo '{NOME_ARQUIVO}' com {NUM_LINHAS} linhas gerado com sucesso!")
print("As colunas 'nome produto', 'valor' e 'data venda' contêm erros para tratamento.")