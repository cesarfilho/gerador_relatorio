## Gerador de Relatórios CSV - CLI
![Build Status](https://github.com/cesarfilho/gerador_relatorio/actions/workflows/python-app.yml/badge.svg)
![Coverage](https://codecov.io/gh/cesarfilho/gerador_relatorio/branch/master/graph/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/github/license/cesarfilho/gerador_relatorio)

Este projeto fornece uma interface de linha de comando (CLI) para gerar relatórios a partir de arquivos CSV de vendas.

### Como executar

No terminal, execute:

```bash
python app/run.py <arquivo.csv> [opções]
```

Ou, se o comando estiver disponível como `vendas-cli`:

```bash
vendas-cli <arquivo.csv> [opções]
```

### Argumentos obrigatórios
- `<arquivo.csv>`: Caminho para o arquivo CSV de vendas.

### Opções disponíveis
- `-s`, `--start`: Data inicial no formato `YYYY-MM-DD` (filtra vendas a partir desta data)
- `-e`, `--end`: Data final no formato `YYYY-MM-DD` (filtra vendas até esta data)
- `-f`, `--format`: Formato de saída (`json` ou `text`)

### Exemplos de uso

Gerar relatório padrão:
```bash
python app/run.py vendas.csv
```

Gerar relatório filtrando por data:
```bash
python app/run.py vendas.csv --start 2023-01-01 --end 2023-01-31
```

Gerar relatório em formato JSON:
```bash
python app/run.py vendas.csv --format json
```

### Saída
O relatório exibe:
- Total de vendas (em reais)
- Total de vendas por produto
- Produto mais vendido (nome e quantidade)

### Requisitos
- Python 3.8+
- Instalar dependências com:
```bash
pip install -r requirements.txt
```

### Instalação do vendas-cli
Se desejar instalar o comando `vendas-cli` globalmente, execute:

```bash
pip install .
```

Ou, para instalar em modo desenvolvimento:

```bash
pip install -e .
```

Após a instalação, o comando `vendas-cli` estará disponível no terminal.
