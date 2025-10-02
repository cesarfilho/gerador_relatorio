
import unittest

from app.core import Relatorio
from app.csv import ReadCSV



class TestRelatorio(unittest.TestCase):

    def test_relatorio(self):

        relatorio=Relatorio()
        self.assertIsNotNone(relatorio)
        self.assertIsInstance(relatorio, Relatorio)
        data = ReadCSV().read_csv('vendas_com_erros_v2.csv')
        relatorio.parametros(data=data, start=None, end=None, format=None)
        relatorio.gerar()