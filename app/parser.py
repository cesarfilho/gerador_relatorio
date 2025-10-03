import argparse
import sys
from venv import logger

from app.file import ReadCSV
from app.core import Relatorio


class ArgumentoCli:

    def __init__(self, args=None, relatorio=None, reader_csv=None, export=None):
        self.parser = argparse.ArgumentParser(
            prog="vendas-cli",
            description="Gerador de Relatórios CSV",
            add_help=True,
        )
        self.relatorio = relatorio
        self.read_csv = reader_csv
        self.export = export
        self.definir_argumentos(args)

    def definir_argumentos(self, args=None):
        self.parser.add_argument("filename", type=str, help="nome e caminho do arquivo")
        self.parser.add_argument("-s","--start", help="data início yyyy-mm-dd")
        self.parser.add_argument("-e","--end", help="data fim yyyy-mm-dd")
        self.parser.add_argument("-f","--format", choices=["json", "text"], help="Tipo de saída (json ou text)")

        if args is not None:
            self.parser.parse_args(args)
        else:
            self.parser.parse_args(sys.argv[1:])

        if not self.parser.parse_args(args).filename:
            self.parser.print_help()
            sys.exit(1)
        
        self.processar()

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
