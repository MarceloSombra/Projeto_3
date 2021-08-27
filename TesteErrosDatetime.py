import datetime
import math


class Loja(object):

    def __init__(self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        self.aluguelHora = 5
        self.aluguelDia = 25
        self.aluguelSemana = 100
        self.aluguelFamilia = 0
      
       
    def receberPedidoHora(self, qtdeBike, retiraBike, devolveBike):
        self.qtdeBike = qtdeBike
        self.tempoLocacao = devolveBike - retiraBike
        self.totalHoras = math.ceil(self.tempoLocacao.seconds / 3600) + self.tempoLocacao.days * 24
        return self.totalHoras*self.aluguelDia
       
    print(receberPedidoHora(5, datetime.datetime(2021, 8, 22, 19, 50), datetime.datetime(2021, 8, 24, 18, 00 ), datetime.datetime(2021, 8, 24, 18, 00 )))