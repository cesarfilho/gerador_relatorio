from app.output import Export


def test_export_json_nested(capsys):
    dados = {
        "total_vendas": "R$ 100.00",
        "total_vendas_por_produto": {"A": 2, "B": 3},
    }
    Export().exportar_json(dados)
    out, _ = capsys.readouterr()
    assert '"total_vendas"' in out
    assert '"total_vendas_por_produto"' in out
    assert '"A"' in out and '"B"' in out


def test_export_text_nested_and_empty(capsys):
    e = Export()
    dados = {
        "total_vendas": "R$ 100.00",
        "total_vendas_por_produto": {"A": 2, "B": 3},
    }
    e.exportar_text(dados)
    out, _ = capsys.readouterr()
    assert "total_vendas" in out
    assert "total_vendas_por_produto" in out
    assert "A" in out and "B" in out

    # Trigger non-simple subdoc branch by including a list value
    e.exportar_text({"complexo": {"nested": [1, 2, 3]}})
    out_complex, _ = capsys.readouterr()
    assert "complexo" in out_complex

    e.exportar_text({})
    out2, _ = capsys.readouterr()
    assert isinstance(out2, str)
