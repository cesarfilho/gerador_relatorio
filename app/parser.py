import argparse
import sys


class ArgumentoCli:

    def __init__(self, args=None):
            self.parser = argparse.ArgumentParser(description="Gerador de Relatórios CSV")
            self.definir_comandos(args)
            

    def definir_comandos(self, args=None):
        self.parser.add_argument("filename", help="nome e caminho do arquivo")
        self.parser.add_argument("--start", help="data inicio yyyy-mm-dd")
        self.parser.add_argument("--end", help="data fim yyyy-mm-dd")
        self.parser.add_argument("--format", choices=["json", "text"], default="text", help="Tipo de saída (json ou text)")

        if args is not None:
            self.parser.parse_args(args)
        else:
            self.parser.parse_args(sys.argv[1:])
        self.parser.print_help()




