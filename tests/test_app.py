import unittest
# from unittest.mock import patch, Mock

from app.run import main
from app.parser import ArgumentoCli

class TestApp(unittest.TestCase):

    def test_arg_format_text(self):
        pargs = ["teste.csv", "--format", "text"]
        p = ArgumentoCli()
        _args = p.parser.parse_args(pargs)
        self.assertEqual(_args.filename, "teste.csv")
        self.assertEqual(_args.format, "text")

    def test_arg_format_json(self):
        pargs = ["teste.csv", "--format", "json"]
        p = ArgumentoCli()
        _args = p.parser.parse_args(pargs)
        self.assertEqual(_args.filename, "teste.csv")
        self.assertEqual(_args.format, "json")

    def test_arg_data_inicio(self):
        pargs = ["teste.csv", "--start", "2023-01-01"]
        p = ArgumentoCli()
        _args = p.parser.parse_args(pargs)
        self.assertEqual(_args.start, "2023-01-01")

    def test_arg_data_fim(self):
        pargs = ["teste.csv", "--end", "2023-12-31"]
        p = ArgumentoCli()
        _args = p.parser.parse_args(pargs)
        self.assertEqual(_args.end, "2023-12-31")

    def test_arg_missing_filename(self):
        pargs = []
        p = ArgumentoCli()
        with self.assertRaises(SystemExit):
            p.parser.parse_args(pargs)

    def test_arg_help(self):
        pargs = ["--help"]
        p = ArgumentoCli()
        with self.assertRaises(SystemExit):
            p.parser.parse_args(pargs)

    def test_app_inicial(self):
        p = main()
        self.assertIsNotNone(p)
        self.assertIsInstance(p, ArgumentoCli)

    def test_arg_main(self):
        pargs = ["teste.csv", "--start", "2023-01-01"]
        p = main()
        self.assertIsNotNone(p)
        self.assertIsInstance(p, ArgumentoCli)
        _args = p.parser.parse_args(pargs)
        self.assertIsNotNone(_args)
        self.assertEqual(_args.filename, "teste.csv")
        self.assertEqual(_args.start, "2023-01-01")
        self.assertIsNone(_args.end)
        self.assertIsNone(_args.format)
