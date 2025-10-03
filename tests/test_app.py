import sys
import unittest
from unittest.mock import patch

from app.run import main
from app.parser import ArgumentoCli
from app.core import Relatorio
from app.file import ReadCSV
from app.output import Export

class TestApp(unittest.TestCase):
    def setUp(self):
        self.rel=Relatorio()
        self.reader=ReadCSV()
        self.export=Export()

    @patch.object(sys, 'argv', ['vendas-cli',"vendas_com_erros_v2.csv", "--format", "text"])
    def test_arg_format_text(self):
        self.parser = ArgumentoCli(relatorio=self.rel, reader_csv=self.reader, export=self.export)
        _args = self.parser.parser.parse_args()
        self.assertEqual(_args.filename, "vendas_com_erros_v2.csv")
        self.assertEqual(_args.format, "text")

    @patch.object(sys, 'argv', ['vendas-cli',"vendas_com_erros_v2.csv", "--format", "json"])
    def test_arg_format_json(self):
        self.parser = ArgumentoCli(relatorio=self.rel, reader_csv=self.reader, export=self.export)
        _args = self.parser.parser.parse_args()
        self.assertEqual(_args.filename, "vendas_com_erros_v2.csv")
        self.assertEqual(_args.format, "json")

    @patch.object(sys, 'argv', ['vendas-cli',"vendas_com_erros_v2.csv", "--format", "json","--start", "2023-01-01"])
    def test_arg_data_inicio(self):
        self.parser = ArgumentoCli(relatorio=self.rel, reader_csv=self.reader, export=self.export)
        _args = self.parser.parser.parse_args()
        self.assertEqual(_args.start, "2023-01-01")

    @patch.object(sys, 'argv', ['vendas-cli',"vendas_com_erros_v2.csv", "--format", "json","--end", "2023-12-31"])
    def test_arg_data_fim(self):
        self.parser = ArgumentoCli(relatorio=self.rel, reader_csv=self.reader, export=self.export)
        _args = self.parser.parser.parse_args()
        self.assertEqual(_args.end, "2023-12-31")

    @patch.object(sys, 'argv', ['vendas-cli', "--format", "json"])
    def test_arg_missing_filename(self):
        with self.assertRaises(SystemExit):
            self.parser = ArgumentoCli(relatorio=self.rel, reader_csv=self.reader, export=self.export)

    @patch.object(sys, 'argv', ['vendas-cli',"--help"])
    def test_arg_help(self):
        with self.assertRaises(SystemExit):
            self.parser = ArgumentoCli(relatorio=self.rel, reader_csv=self.reader, export=self.export)

    @patch.object(sys, 'argv', ['vendas-cli',"vendas_com_erros_v2.csv", "--format", "json"])
    def test_app_inicial(self):
        p = main()
        self.assertIsNotNone(p)
        self.assertIsInstance(p, ArgumentoCli)

    @patch.object(sys, 'argv', ['vendas-cli',"vendas_com_erros_v2.csv","--start", "2023-01-01","--format", "json"])
    def test_arg_main(self):
        self.parser = main()
        self.assertIsNotNone(self.parser)
        self.assertIsInstance(self.parser, ArgumentoCli)
        _args = self.parser.parser.parse_args()
        self.assertIsNotNone(_args)
        self.assertEqual(_args.filename, "vendas_com_erros_v2.csv")
        self.assertEqual(_args.start, "2023-01-01")
        self.assertIsNone(_args.end)
        self.assertEqual(_args.format, "json")
