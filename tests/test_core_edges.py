import pytest

from app.core import Relatorio


def make_item(prod, valor, data):
    return {"nome_produto": prod, "valor": valor, "data_venda": data}


def test_boundary_dates_inclusive():
    data = [
        make_item("A", "10.0", "2024-01-01"),
        make_item("B", "20.0", "2024-01-31"),
        make_item("C", "30.0", "2024-02-01"),
    ]
    r = Relatorio()
    r.parametros(data=data, start="2024-01-01", end="2024-01-31", format="text")
    r.gerar()
    assert "C" not in r.dados["total_vendas_por_produto"]
    assert r.dados["total_vendas_por_produto"]["A"] == 1
    assert r.dados["total_vendas_por_produto"]["B"] == 1


def test_invalid_dates_and_values_are_skipped():
    data = [
        make_item("A", "not-a-number", "2024-01-02"),
        make_item("B", "10.5", "invalid-date"),
        make_item("C", "30.0", "2024-01-03"),
    ]
    r = Relatorio()
    r.parametros(data=data, start=None, end=None, format="text")
    r.gerar()
    assert r.dados["total_vendas_por_produto"] == {"C": 1}
    assert r.dados["total_vendas"] == "R$ 30.00"


def test_empty_data_and_all_filtered():
    r = Relatorio()
    r.parametros(data=[], start="2024-01-01", end="2024-01-02", format="json")
    r.gerar()
    assert r.dados["total_vendas_por_produto"] == {}
    assert r.dados["total_vendas"] == "R$ 0.00"
    assert r.produto_mais_vendido() == {}


def test_tie_handling_produto_mais_vendido():
    data = [
        make_item("A", "10.0", "2024-01-01"),
        make_item("B", "20.0", "2024-01-02"),
        make_item("A", "30.0", "2024-01-03"),
        make_item("B", "40.0", "2024-01-04"),
    ]
    r = Relatorio()
    r.parametros(data=data, start=None, end=None, format=None)
    r.gerar()
    assert r.dados["produto_mais_vendido"] == {"A": 2, "B": 2}
