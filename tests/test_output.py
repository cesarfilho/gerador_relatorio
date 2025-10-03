import unittest
import io
import sys
import json

from app.output import Export
from app.file import ReadCSV


class TestExport(unittest.TestCase):

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
            {"produto": "A", "valor": 10, "ativo": True},
            {"produto": "B", "valor": None, "ativo": False}
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
            for k, v in item.items():
                expected += f"{k}: {v}\n"
            expected += "-" * 20 + "\n"
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
        expected = "a: 1\n" + "-" * 20 + "\n"
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
            for k, v in item.items():
                expected += f"{k}: {v}\n"
            expected += "-" * 20 + "\n"
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
        expected = "chave: valor\n" + "-" * 20 + "\n"
        self.assertEqual(captured_output.getvalue(), expected)