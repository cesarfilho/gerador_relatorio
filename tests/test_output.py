import unittest
import io
import sys
import json
from tabulate import tabulate

from app.output import Export
from app.file import ReadCSV


class TestExport(unittest.TestCase):
    def test_exportar_text_dict_simples(self):
        # Testa exportar_text recebendo um dict simples
        dados = {"chave": "valor", "outra": 123}
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar_text(dados)
        finally:
            sys.stdout = sys_stdout
        expected = tabulate([dados], headers="keys", tablefmt="grid") + "\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_exportar_formato_invalido(self):
        # Testa exportar com formato inválido (não deve imprimir nada)
        dados = [{"a": 1}]
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar(dados, "xml")
        finally:
            sys.stdout = sys_stdout
        self.assertEqual(captured_output.getvalue(), "")

    def test_exportar_json_lista_vazia(self):
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar_json([])
        finally:
            sys.stdout = sys_stdout
        expected = json.dumps([], indent=4) + "\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_exportar_text_diferentes(self):
        dados = [
            {"A": 10, "ativo": True},
            {"B": None, "ativo": False}
        ]
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar_text(dados)
        finally:
            sys.stdout = sys_stdout
        expected = ""
        for item in dados:
            expected += tabulate([item], headers="keys", tablefmt="grid") + "\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_exportar_json_exportar(self):
        dados = [{"a": 1}]
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar(dados, "json")
        finally:
            sys.stdout = sys_stdout
        expected = json.dumps(dados, indent=4) + "\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_exportar_text_exportar(self):
        dados = [{"a": 1}]
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar(dados, "text")
        finally:
            sys.stdout = sys_stdout
        expected = tabulate([dados[0]], headers="keys", tablefmt="grid") + "\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_exportar_json_print(self):
        dados = ReadCSV().read_csv_quantidade('vendas_com_erros_v2.csv',2)
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar_json(dados)
        finally:
            sys.stdout = sys_stdout

        expected = json.dumps(dados, ensure_ascii=False, indent=4) + "\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_exportar_text_print(self):
        dados = ReadCSV().read_csv_quantidade('vendas_com_erros_v2.csv',5)
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar_text(dados)
        finally:
            sys.stdout = sys_stdout
        expected = ""
        for item in dados:
            expected += tabulate([item], headers="keys", tablefmt="grid") + "\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_exportar_text_lista_vazia(self):
        dados = []
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar_text(dados)
        finally:
            sys.stdout = sys_stdout
        self.assertEqual(captured_output.getvalue(), "")

    def test_exportar_text_item(self):
        dados = [{"chave": "valor"}]
        export = Export()
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            export.exportar_text(dados)
        finally:
            sys.stdout = sys_stdout
        expected = tabulate([dados[0]], headers="keys", tablefmt="grid") + "\n"
        self.assertEqual(captured_output.getvalue(), expected)