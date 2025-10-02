# import tabulate
import logging
import sys
import os 

from app.parser import ArgumentoCli


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
    return ArgumentoCli(args=args)


if __name__== "__main__":
    logger.info('Iniciando CLI ...')
    main()