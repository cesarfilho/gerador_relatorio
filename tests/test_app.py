import unittest
from unittest.mock import patch, Mock

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
    

    def test_arg_data(self):
        self.fail("implementar")

    # def test_app_none(self):
    #     p = main()
    #     self.assertIsNotNone(p)
    #     self.assertIsInstance(p, ArgumentoCli)

