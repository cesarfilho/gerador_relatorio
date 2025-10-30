import sys
import runpy


def test_run_module_as_main(tmp_path, monkeypatch):
    csvf = tmp_path / "vendas.csv"
    csvf.write_text("nome_produto;valor;data_venda\nA;10.0;2024-01-01\n")
    monkeypatch.setattr(sys, "argv", ["python", str(csvf), "--format", "json"])
    # Running the module as __main__ should not raise
    runpy.run_module("app.run", run_name="__main__")
