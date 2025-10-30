import pytest

from app.file import ReadCSV


def test_readcsv_file_not_found():
    reader = ReadCSV()
    with pytest.raises(FileNotFoundError):
        reader.read_csv("/path/that/does/not/exist.csv")


def test_readcsv_empty_file(tmp_path):
    empty = tmp_path / "empty.csv"
    empty.write_text("")
    reader = ReadCSV()
    with pytest.raises(StopIteration):
        reader.read_csv(str(empty))


def test_readcsv_malformed_rows_and_header(tmp_path):
    # Header has 3 columns; some rows have fewer/more fields
    content = (
        "nome_produto;valor;data_venda\n"
        "A;10.0;2024-01-01\n"
        "B;20.0\n"
        "C;30.0;2024-01-03;EXTRA\n"
    )
    f = tmp_path / "malformed.csv"
    f.write_text(content)
    reader = ReadCSV()
    data = reader.read_csv(str(f))
    # First row complete
    assert data[0]["nome_produto"] == "A"
    assert data[0]["valor"] == "10.0"
    assert data[0]["data_venda"] == "2024-01-01"
    # Second row missing data_venda -> key not present
    assert data[1]["nome_produto"] == "B"
    assert data[1]["valor"] == "20.0"
    assert "data_venda" not in data[1]
    # Third row has extra field; extras are ignored by zip
    assert data[2]["nome_produto"] == "C"
    assert data[2]["valor"] == "30.0"
    assert data[2]["data_venda"] == "2024-01-03"


def test_readcsv_quantidade_limits(tmp_path):
    content = (
        "nome_produto;valor;data_venda\n"
        "A;10.0;2024-01-01\n"
        "B;20.0;2024-01-02\n"
        "C;30.0;2024-01-03\n"
    )
    f = tmp_path / "data.csv"
    f.write_text(content)
    reader = ReadCSV()
    first_two = reader.read_csv_quantidade(str(f), 2)
    assert len(first_two) == 2
    assert [r["nome_produto"] for r in first_two] == ["A", "B"]
