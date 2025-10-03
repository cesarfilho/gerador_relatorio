
import unittest

from app.core import Relatorio
from app.file import ReadCSV



class TestRelatorio(unittest.TestCase):


    def setUp(self):
        self.data = [
            {"nome_produto": "A", "valor": "10.0", "data_venda": "2025-08-01 10:00:00"},
            {"nome_produto": "B", "valor": "20.0", "data_venda": "2025-08-02 10:00:00"},
            {"nome_produto": "A", "valor": "15.0", "data_venda": "2025-08-03 10:00:00"},
            {"nome_produto": "C", "valor": "INVÁLIDO", "data_venda": "2025-08-04 10:00:00"},
            {"nome_produto": "A", "valor": "5.0", "data_venda": ""},
        ]
        self.relatorio = Relatorio()
        self.relatorio.parametros(data=self.data, start="2025-08-01", end="2025-08-31", format="json")

    def test_relatorio(self):
        self.assertIsNotNone(self.relatorio)
        self.assertIsInstance(self.relatorio, Relatorio)

    def test_gerar(self):
        self.relatorio.gerar()
        self.assertIn("total_vendas", self.relatorio.dados)
        self.assertIn("total_vendas_por_produto", self.relatorio.dados)
        self.assertIn("produto_mais_vendido", self.relatorio.dados)

    def test_total_vendas_por_produto(self):
        self.relatorio.gerar()
        esperado = {"A": 2, "B": 1}
        self.assertEqual(self.relatorio.dados["total_vendas_por_produto"], esperado)

    def test_total_vendas(self):
        self.relatorio.gerar()
        self.assertEqual(self.relatorio.dados["total_vendas"], "R$ 45.00")

    def test_total_vendas_fail(self):
        self.relatorio.gerar()
        self.assertNotEqual(self.relatorio.dados["total_vendas"], "R$ 25.00")

    def test_produto_mais_vendido(self):
        self.relatorio.gerar()
        resultado = self.relatorio.produto_mais_vendido()
        self.assertEqual(resultado, {"produto": "A", "quantidade": 2})

    def test_data_produto_valida(self):
        self.assertTrue(self.relatorio.data_produto_valida("2025-08-01 10:00:00"))
        self.assertFalse(self.relatorio.data_produto_valida("2025-07-01 10:00:00"))
        self.assertFalse(self.relatorio.data_produto_valida(""))
        self.assertFalse(self.relatorio.data_produto_valida("data_invalida"))

    def test_valor_eh_valido(self):
        self.assertTrue(self.relatorio.valor_eh_valido("10.0"))
        self.assertFalse(self.relatorio.valor_eh_valido("INVÁLIDO"))
        self.assertFalse(self.relatorio.valor_eh_valido("") )

