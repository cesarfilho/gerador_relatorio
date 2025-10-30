import sys
import types
import argparse
import pytest

from app.parser import ArgumentoCli


class DummyReader:
    def __init__(self, data):
        self._data = data

    def read_csv(self, path):
        return self._data


class DummyRelatorio:
    def __init__(self):
        self.called = False
        self.params = None
        self.dados = {"ok": True}

    def parametros(self, **kwargs):
        self.params = kwargs

    def gerar(self):
        self.called = True


class DummyExport:
    def __init__(self):
        self.exported = None

    def exportar(self, dados, formato):
        self.exported = (dados, formato)


def test_cli_missing_filename_exits(monkeypatch):
    monkeypatch.setenv("PYTHONWARNINGS", "ignore")
    monkeypatch.setattr(sys, "argv", ["vendas-cli"])  # no filename
    with pytest.raises(SystemExit):
        ArgumentoCli(relatorio=DummyRelatorio(), reader_csv=DummyReader([]), export=DummyExport())


def test_cli_help_exits_zero(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["vendas-cli", "-h"])  # argparse handles and exits
    with pytest.raises(SystemExit) as ex:
        ArgumentoCli(relatorio=DummyRelatorio(), reader_csv=DummyReader([]), export=DummyExport())
    assert ex.value.code == 0


def test_cli_unknown_args_are_ignored(monkeypatch):
    data = [{"nome_produto": "A", "valor": "10.0", "data_venda": "2024-01-01"}]
    rel = DummyRelatorio()
    exp = DummyExport()
    monkeypatch.setattr(sys, "argv", [
        "vendas-cli", "file.csv", "--unknown", "x", "--start", "2024-01-01", "--end", "2024-12-31", "--format", "text"
    ])
    ArgumentoCli(relatorio=rel, reader_csv=DummyReader(data), export=exp)
    assert rel.called is True
    assert exp.exported[1] == "text"


def test_cli_invalid_format_exits(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["vendas-cli", "file.csv", "--format", "yaml"])  # invalid by choices
    with pytest.raises(SystemExit):
        ArgumentoCli(relatorio=DummyRelatorio(), reader_csv=DummyReader([]), export=DummyExport())


def test_processar_no_filename_branch(monkeypatch):
    # Force parse_known_args to return a namespace without filename
    monkeypatch.setattr(sys, "argv", ["vendas-cli"])  # base argv not used
    arg = ArgumentoCli.__new__(ArgumentoCli)
    arg.parser = argparse.ArgumentParser(add_help=False)
    arg.relatorio = DummyRelatorio()
    arg.read_csv = DummyReader([])
    arg.export = DummyExport()
    def fake_parse_known_args():
        class NS: pass
        return (NS(), [])
    arg.definir_argumentos = lambda: None
    arg.parser.parse_known_args = fake_parse_known_args
    with pytest.raises(SystemExit):
        ArgumentoCli.processar(arg)
