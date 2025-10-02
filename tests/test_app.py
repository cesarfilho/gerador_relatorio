import unittest
# from unittest.mock import patch, Mock

from app.run import main
from app.parser import ArgumentoCli

class TestApp(unittest.TestCase):


    def test_app_inicial(self):
        p = main(args=["teste.csv"])
        self.assertIsNotNone(p)
        self.assertIsInstance(p, ArgumentoCli)


    def test_arg_format(self):
        self.fail("implementar")
    
    def test_arg_format_json(self):
        self.fail("implementar")

    def test_arg_format_text(self):
        self.fail("implementar")
    
    def test_arg_data_inicio(self):
        self.fail("implementar")

    def test_arg_data_fim(self):
        self.fail("implementar")

    def test_arg_main(self):
        pargs = ["teste.csv", "--start", "2023-01-01"]
        p = main(args=pargs)
        self.assertIsNotNone(p)
        self.assertIsInstance(p, ArgumentoCli)
        _args = p.parser.parse_args(pargs)
        self.assertIsNotNone(_args)
        self.assertEqual(_args.filename, "teste.csv")
        self.assertEqual(_args.start, "2023-01-01")
        self.assertIsNone(_args.end)
        self.assertIsNone(_args.format)


    # def test_app_none(self):
    #     p = main()
    #     self.assertIsNotNone(p)
    #     self.assertIsInstance(p, ArgumentoCli)

