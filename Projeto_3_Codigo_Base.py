class Cliente(object):

    def __init__(self):
        pass
        
    def alugarBikeHora(self, qtdeBikeHora, qtdeHoras):
        self.qtdeBikeHora = qtdeBikeHora
        self.qtdeHoras = qtdeHoras

    def alugarBikeDia(self, qtdeBikeDia, qtdeHoras):
        self.qtdeBikeDia = qtdeBikeDia
        self.qtdeHoras = qtdeHoras

    def alugarBikeSemana(self, qtdeBikeSemana, qtdeHoras):
        self.qtdeBikeSemana = qtdeBikeSemana
        self.qtdeHoras = qtdeHoras

    def alugarFamilia(self, qtdeBikeHoraFam, qtdeHorasBikehora, qtdeBikeDiaFam, qtdeHorasBikeDia, qtdeBikeSemanaFam, qtdeHorasBikeSemana):
        self.qtdeBikeHoraFam = qtdeBikeHoraFam
        self.qtdeHorasBikehora = qtdeHorasBikehora
        self.qtdeBikeDiaFam = qtdeBikeDiaFam
        self.qtdeHorasBikeDia = qtdeHorasBikeDia
        self.qtdeBikeSemanaFam = qtdeBikeSemanaFam
        self.qtdeHorasBikeSemana = qtdeHorasBikeSemana



class Loja(object):

    def __init__(self):
        self.qtdeHoras = 0
        self.valorAluguel = None
        self.estoque = 50
        self.aluguelHora = 5
        self.aluguelDia = 25
        self.aluguelSemana = 100
        self.aluguelFamilia = 0


def calcularLocacao(self):
    self.totalAluguelHora = (self.qtdeBikeHora*self.qtdeHoras)*self.valorAluguel
    self.totalAluguelDia = (self.qtdeBikeDia*self.qtdeHoras)*self.valorAluguel
    self.totalAluguelSemana = (self.qtdeBikeSemana*self.qtdeHoras)*self.valorAluguel
    self.totalAluguelFamilia = ((((self.qtdeBikeHora*self.qtdeHoras)*self.valorAluguel) + ((self.qtdeBikeDia*self.qtdeHoras)*self.valorAluguel) + ((self.qtdeBikeSemana*self.qtdeHoras)*self.valorAluguel))*0.70)

    print("Extrato de Locação de Bicicleta")
    print("Tipo Plano\tQtdeBike\tDuração da Locação\t")

    