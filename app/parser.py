import argparse
import sys
from venv import logger

from app.file import ReadCSV
from app.core import Relatorio
from app.output import Export


class ArgumentoCli:

    def __init__(self, relatorio:Relatorio=None, reader_csv:ReadCSV=None, export:Export=None):
        self.parser = argparse.ArgumentParser(
            prog="vendas-cli",
            description="Gerador de Relatórios CSV",
            add_help=True,
        )
        self.relatorio = relatorio
        self.read_csv = reader_csv
        self.export = export
        self.definir_argumentos()

    def definir_argumentos(self):
        self.parser.add_argument("filename", type=str, help="nome e caminho do arquivo")
        self.parser.add_argument("-s","--start", help="data início yyyy-mm-dd")
        self.parser.add_argument("-e","--end", help="data fim yyyy-mm-dd")
        self.parser.add_argument("-f","--format", choices=["json", "text"], help="Tipo de saída (json ou text)")

    def processar(self, args=None):
        parsed = self.parser.parse_args(args)
        formato = getattr(parsed, "format", None)
        start = getattr(parsed, "start", None)
        end = getattr(parsed, "end", None)
        filename = getattr(parsed, "filename", None)
        if not filename:
            self.parser.print_help()
            sys.exit(1)
            
        dados = self.read_csv.read_csv(filename)
        logger.info(f"Lendo arquivo: {filename} com {len(dados)} linhas")
        self.relatorio.parametros(
            data=dados,
            start=start,
            end=end,
            format=formato
        )

    def processar(self):
        if "format" in self.parser.parse_args():
            formato = self.parser.parse_args().format
        
        if "start" in self.parser.parse_args():
            start = self.parser.parse_args().start

        if "end" in self.parser.parse_args():
            end = self.parser.parse_args().end  

        filename = self.parser.parse_args().filename

        dados = self.read_csv.read_csv(filename)
        logger.info(f"Lendo arquivo: {filename} com {len(dados)} linhas")

        self.relatorio.parametros(
            data=dados,
            start=start,
            end=end,
            format=formato
        )
        self.relatorio.gerar()
        
        self.export.exportar(self.relatorio.dados, formato)
