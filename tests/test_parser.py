
import sys
import unittest
from unittest.mock import MagicMock, patch
from app.parser import ArgumentoCli

class TestArgumentoCli(unittest.TestCase):
    
    
    def setUp(self):
        self.mock_relatorio = MagicMock()
        self.mock_reader_csv = MagicMock()
        self.mock_reader_csv.read_csv.return_value = [{"col1": "val1"}, {"col1": "val2"}]
        self.mock_export = MagicMock()



    @patch.object(sys, 'argv', ['vendas-cli',"arquivo.csv", "--start", "2024-01-01", "--end", "2024-01-31", "--format", "json"])
    def test_processar_calls_parametros(self):
        self.argumento_cli = ArgumentoCli(
            relatorio=self.mock_relatorio,
            reader_csv=self.mock_reader_csv,
            export=self.mock_export
        )
        self.mock_reader_csv.reset_mock()
        self.mock_relatorio.reset_mock()
        with patch("app.parser.logger") as mock_logger:
            self.argumento_cli.processar()
            # Verifica se a chamada correta está entre as chamadas
            self.assertIn(
                ("arquivo.csv",),
                [call.args for call in self.mock_reader_csv.read_csv.call_args_list]
            )
            mock_logger.info.assert_called()
            # Verifica se a chamada correta está entre as chamadas
            self.assertIn(
                {
                    "data": self.mock_reader_csv.read_csv.return_value,
                    "start": "2024-01-01",
                    "end": "2024-01-31",
                    "format": "json"
                },
                [call.kwargs for call in self.mock_relatorio.parametros.call_args_list]
            )

    @patch.object(sys, 'argv', ['vendas-cli'])
    def test_processar_missing_filename(self):
        with self.assertRaises(SystemExit):
            self.argumento_cli = ArgumentoCli(
                relatorio=self.mock_relatorio,
                reader_csv=self.mock_reader_csv,
                export=self.mock_export
            )
            with patch.object(self.argumento_cli.parser, "print_help") as mock_print_help, \
                patch("sys.exit") as mock_exit:
                self.argumento_cli.processar()
                mock_print_help.assert_called()
                mock_exit.assert_called_with(1)

    @patch('sys.argv', ['vendas-cli', 'arquivo.csv'])
    def test_processar_none_optional_args(self):
        self.argumento_cli = ArgumentoCli(
            relatorio=self.mock_relatorio,
            reader_csv=self.mock_reader_csv,
            export=self.mock_export
        )
        self.mock_reader_csv.reset_mock()
        self.mock_relatorio.reset_mock()
        with patch("app.parser.logger") as mock_logger:
            self.argumento_cli.processar()
            # Verifica se a chamada correta está entre as chamadas
            self.assertIn(
                {
                    "data": self.mock_reader_csv.read_csv.return_value,
                    "start": None,
                    "end": None,
                    "format": None
                },
                [call.kwargs for call in self.mock_relatorio.parametros.call_args_list]
            )
            mock_logger.info.assert_called()