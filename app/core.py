from typing import Dict, AnyStr
import logging

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
        # Lógica para calcular total de vendas por produto
        self.dados['total_vendas_por_produto'] = {}
        for item in self.data:
            produto = item['nome_produto']
            valor = item['valor']
            if not self.data_produto_valida(item['data_venda']):
                continue
            if not self.valor_eh_valido(valor):
                continue
            if produto not in self.dados['total_vendas_por_produto']:
                self.dados['total_vendas_por_produto'][produto] = 1
            self.dados['total_vendas_por_produto'][produto] += 1
        pass
    def total_vendas(self) -> None:
        self.dados['total_vendas'] = sum(float(item['valor']) for item in self.data if self.valor_eh_valido(item['valor']) and self.data_produto_valida(item['data_venda']))


    def produto_mais_vendido(self):
        return max(self.dados['total_vendas_por_produto'], key=self.dados['total_vendas_por_produto'].get)
    
    def data_produto_valida(self, data_str) -> bool:
        # Validar formato da data
        try:
            from datetime import datetime
            pdata = datetime.strptime(data_str, '%Y-%m-%d')

            valida_start = (self.start and pdata >= datetime.strptime(self.start, '%Y-%m-%d') or not self.start)
            valida_end = (self.end and pdata <= datetime.strptime(self.end, '%Y-%m-%d') or not self.end)
            return valida_start and valida_end
        
        except ValueError:
            return False
        
    def valor_eh_valido(self, valor_str) -> bool:
        try:
            float(valor_str)
            return True
        except ValueError:
            return False