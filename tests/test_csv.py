import unittest
import os

from app.file import ReadCSV

class TestArquivoCsv(unittest.TestCase):
    
    def setUp(self):
        self.test_file = 'test_temp.csv'
        with open(self.test_file, 'w', encoding='utf-8', newline='') as f:
            f.write('col1;col2\n')
            f.write('a;1\n')
            f.write('b;2\n')

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_leitura_csv(self):
        result = ReadCSV().read_csv(self.test_file)
        expected = [
            {'col1': 'a', 'col2': '1'},
            {'col1': 'b', 'col2': '2'}
        ]
        self.assertEqual(result, expected)
        # expected = [
        #     {'col1': 'a', 'col2': '1'},
        #     {'col1': 'b', 'col2': '2'}
        # ]
        # self.assertEqual(result, expected)