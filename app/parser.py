import argparse


class ArgumentoCli:

    def __init__(self):
            self.parser = argparse.ArgumentParser(description="Gerador de Relatórios CSV")
            self.definir_comandos()
            

    def definir_comandos(self):
        self.parser.add_subparsers(dest="command",help="Comandos disponíveis")
        self.parser.parse_args()
        self.parser.print_help()



