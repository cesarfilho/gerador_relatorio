import json
from tabulate import tabulate

class Export():
    def exportar(self, dados:dict[str,any], formato: str) -> None:
        if formato == 'json':
            self.exportar_json(dados)
        elif formato == 'text':
            self.exportar_text(dados)


    def exportar_json(self, dados:dict[str,any]) -> None:
        print(json.dumps(dados, indent=4))


    def exportar_text(self, dados:dict[str,any]) -> None:
        """
        Exporta os dados em formato tabulado.
        Args:
            dados dict : Dados a serem exportados, podendo conter subdocumentos.
        """
        if isinstance(dados, dict):
            dados = [dados]
        for item in dados:
            # Se o item tem subdocumentos (valores dict), imprime tabulado separadamente
            main_fields = {}
            subdocs = {}
            for k, v in item.items():
                if isinstance(v, dict):
                    subdocs[k] = v
                else:
                    main_fields[k] = v
            if main_fields:
                print(tabulate([main_fields], headers="keys", tablefmt="grid"))
            for subkey, subdoc in subdocs.items():
                print(f"\n{subkey}:")
                # Se subdoc for dict simples (ex: totais por produto), tabula como lista de dicts
                if isinstance(subdoc, dict) and all(isinstance(v, (int, float, str)) for v in subdoc.values()):
                    tab_data = [{"produto": k, "quantidade": v} for k, v in subdoc.items()]
                    print(tabulate(tab_data, headers="keys", tablefmt="grid"))
                else:
                    print(tabulate([subdoc], headers="keys", tablefmt="grid"))