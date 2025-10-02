import csv

class ReadCSV():

    def read_csv(self, file_path):

        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            return [
                {
                    "nome_produto": row[0].split(";")[0],
                    "valor": row[0].split(";")[1],
                    "data_venda": row[0].split(";")[2],
                }
                for row in reader
            ]

