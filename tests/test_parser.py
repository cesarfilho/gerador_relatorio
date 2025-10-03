import pytest
from unittest.mock import MagicMock, patch
from app.parser import ArgumentoCli

@pytest.fixture
def mock_relatorio():
    rel = MagicMock()
    return rel

@pytest.fixture
def mock_reader_csv():
    reader = MagicMock()
    reader.read_csv.return_value = [{"col1": "val1"}, {"col1": "val2"}]
    return reader

@pytest.fixture
def mock_export():
    return MagicMock()

@pytest.fixture
def argumento_cli(mock_relatorio, mock_reader_csv, mock_export):
    return ArgumentoCli(relatorio=mock_relatorio, reader_csv=mock_reader_csv, export=mock_export)

def test_processar_calls_parametros(monkeypatch, argumento_cli, mock_relatorio, mock_reader_csv):
    args = ["arquivo.csv", "-s", "2024-01-01", "-e", "2024-01-31", "-f", "json"]
    with patch("app.parser.logger") as mock_logger:
        argumento_cli.processar(args)
        mock_reader_csv.read_csv.assert_called_once_with("arquivo.csv")
        mock_logger.info.assert_called_once()
        mock_relatorio.parametros.assert_called_once_with(
            data=mock_reader_csv.read_csv.return_value,
            start="2024-01-01",
            end="2024-01-31",
            format="json"
        )

def test_processar_missing_filename(monkeypatch, argumento_cli):
    args = []
    with patch.object(argumento_cli.parser, "print_help") as mock_print_help, \
         patch("sys.exit") as mock_exit:
        argumento_cli.processar(args)
        mock_print_help.assert_called_once()
        mock_exit.assert_called_once_with(1)

def test_processar_none_optional_args(argumento_cli, mock_relatorio, mock_reader_csv):
    args = ["arquivo.csv"]
    with patch("app.parser.logger") as mock_logger:
        argumento_cli.processar(args)
        mock_relatorio.parametros.assert_called_once_with(
            data=mock_reader_csv.read_csv.return_value,
            start=None,
            end=None,
            format=None
        )
        mock_logger.info.assert_called_once()