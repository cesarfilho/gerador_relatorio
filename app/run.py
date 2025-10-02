import logging
import sys

from app.parser import ArgumentoCli
from app.core import Relatorio
from app.csv import ReadCSV
from app.output import Export

# Configuração do logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main(args=None): 
    relatorio = Relatorio()
    read_csv = ReadCSV()
    export = Export()  # Certifique-se de que a classe Export está definida em algum lugar
    return ArgumentoCli(
        args=args, 
        relatorio=relatorio, 
        reader_csv=read_csv, 
        export=export
    )


if __name__== "__main__":
    main(sys.argv[1:])
