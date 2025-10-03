import logging
import sys

from app.parser import ArgumentoCli
from app.core import Relatorio
from app.file import ReadCSV
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
    export = Export()
    return ArgumentoCli(
        args=args, 
        relatorio=relatorio, 
        reader_csv=read_csv, 
        export=export
    )


if __name__== "__main__":
    main(sys.argv[1:])
