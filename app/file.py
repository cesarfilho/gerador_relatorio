import csv 

class ReadCSV():

    def read_csv(self, file_path):

        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            header = header[0].split(";")
            a= [
                {
                    k:v for k,v in zip(header, row[0].split(";"))
                }
                for row in reader
            ]
            return a

    def read_csv_quantidade(self, file_path:str, quantidade:int):
        return self.read_csv(file_path)[:quantidade]