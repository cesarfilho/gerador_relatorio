import json


class Export():
    def exportar(self, dados, formato):
        if formato == 'json':
            self.exportar_json(dados)
        elif formato == 'text':
            self.exportar_text(dados)


    def exportar_json(self, dados):
        print(json.dumps(dados, indent=4))


    def exportar_text(self, dados):
        for item in dados:
            print(item)