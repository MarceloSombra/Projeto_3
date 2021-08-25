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