import sys
import pytest

from app.run import main


def write_csv(path, rows):
    lines = ["nome_produto;valor;data_venda\n"]
    lines += [";".join(r) + "\n" for r in rows]
    path.write_text("".join(lines))


def test_e2e_cli_text_output(tmp_path, capsys, monkeypatch):
    csvf = tmp_path / "vendas.csv"
    write_csv(csvf, [["A", "10.0", "2024-01-01"], ["B", "20.0", "2024-01-02"]])
    monkeypatch.setattr(sys, "argv", [
        "vendas-cli", str(csvf), "--start", "2024-01-01", "--end", "2024-12-31", "--format", "text"
    ])
    main()
    out, _ = capsys.readouterr()
    assert "total_vendas" in out
    assert "total_vendas_por_produto" in out


def test_e2e_cli_json_output(tmp_path, capsys, monkeypatch):
    csvf = tmp_path / "vendas.csv"
    write_csv(csvf, [["A", "10.0", "2024-01-01"]])
    monkeypatch.setattr(sys, "argv", [
        "vendas-cli", str(csvf), "--format", "json"
    ])
    main()
    out, _ = capsys.readouterr()
    assert '"total_vendas"' in out


def test_e2e_cli_missing_file_errors(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["vendas-cli", "/no/such/file.csv"])
    with pytest.raises(FileNotFoundError):
        main()
