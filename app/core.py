from typing import Dict, AnyStr
import logging 
from datetime import datetime

logger = logging.getLogger(__name__)

class Relatorio:
    def parametros(self, 
            data:Dict=None, 
            start:AnyStr=None, 
            end:AnyStr=None, 
            format:AnyStr=None
    ):
        self.data = data
        self.start = start
        self.end = end
        self.format = format

    def gerar(self) -> None:
        # Lógica para gerar o relatório

        logger.info(
            f"Gerando relatório com formato: {self.format}, start: {self.start}, end: {self.end}"
            )
        self.dados={}
        self.total_vendas_por_produto()
        self.total_vendas()
        self.dados['produto_mais_vendido'] = self.produto_mais_vendido()
        
    def total_vendas_por_produto(self) -> None:
        """
        Calcula o total de vendas por produto.
        
        Returns:
            None:
        """
        self.dados['total_vendas_por_produto'] = {}
        for item in self.data:
            if not self.data_produto_valida(item['data_venda']):
                continue
            if not self.valor_eh_valido(item['valor']):
                continue
            
            produto = item['nome_produto']

            if produto not in self.dados['total_vendas_por_produto']:
                self.dados['total_vendas_por_produto'][produto] = 1
            else:
                self.dados['total_vendas_por_produto'][produto] += 1

    def total_vendas(self) -> None:
        """
        Calcula o total de vendas.

        Returns:
            None:
        """
        total = sum(float(item['valor']) for item in self.data if self.valor_eh_valido(item['valor']) and self.data_produto_valida(item['data_venda']))
        self.dados['total_vendas'] = f"R$ {total:,.2f}".replace(",", ".")

    def produto_mais_vendido(self) -> Dict:
        """
        Retorna todos os produtos mais vendidos (empate).

        Returns:
            dict: Dicionário com os nomes dos produtos mais vendidos e a quantidade vendida.
        """
        vendas = self.dados['total_vendas_por_produto']
        if not vendas:
            return {}
        max_qtd = max(vendas.values())
        mais_vendidos = {prod: qtd for prod, qtd in vendas.items() if qtd == max_qtd}
        return mais_vendidos
    
    def data_produto_valida(self, data_str) -> bool:
        """
        Valida data se está dentro do intervalo start e end.
        Args:
            data_str (str): Data no formato 'YYYY-MM-DD'.

        Returns:
            bool: True se a data está dentro do intervalo ou se start/end não são definidos
        """
        try:
            if not data_str:
                return False
            pdata = datetime.strptime(data_str.split()[0], '%Y-%m-%d')

            valida_start = (self.start and pdata >= datetime.strptime(self.start, '%Y-%m-%d') or not self.start)
            valida_end = (self.end and pdata <= datetime.strptime(self.end, '%Y-%m-%d') or not self.end)
            return valida_start and valida_end
        
        except ValueError:
            return False
        
    def valor_eh_valido(self, valor_str) -> bool:
        """
        Valida se o valor é um float válido.

        Args:
            valor_str (str): O valor a ser validado.

        Returns:
            bool: True se o valor é um float válido, False caso contrário.
        """
        try:
            float(valor_str)
            return True
        except ValueError:
            return False
        