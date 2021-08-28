from Rascunho_BicicletariaDatetime import Cliente, Loja
import datetime
import unittest

class Testes(unittest.TestCase):

    def setUp(self):         
        self.loja = Loja(200, 20)  
        self.cliente = Cliente("Marcelo", 32) 

    
    def testeReceberPedidoHoraFamilia(self):
        print("\nTeste da Bicicletaria recebendo pedido por Hora (Familia)")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoHora(5, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 420)
    
    def testeReceberPedidoHora(self):
        print("\nTeste da Bicicletaria recebendo pedido por Hora")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoHora(2, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 240)

    def testeReceberPedidoHoraValueError(self):
        print("\nTeste da Bicicletaria recebendo pedido por Hora. - Erro ValueError")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoHora(-1, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 0)

    def testeReceberPedidoHoraSystemError(self):
        print("\nTeste da Bicicletaria recebendo pedido por Hora. - System Error")
        self.loja = Loja(20, 20)
        self.assertEqual(self.loja.receberPedidoHora(22, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 0)

    def testeReceberPedidoDiaFamilia(self):
        print("\nTeste da Bicicletaria recebendo pedido por Dia (Familia)")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoDia(5, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 87.5)

    def testeReceberPedidoDia(self): # neste teste, simulamos o periodo de 25 horas, portanto, resultando em um aluguel de 2 dias.
        print("\nTeste da Bicicletaria recebendo pedido por Dia")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoDia(1, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 19, 00, 00, 00)), 50)

    def testeReceberPedidoDiaValueError(self):
        print("\nTeste da Bicicletaria recebendo pedido por Dia. - Erro ValueError")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoDia(-1, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 0)

    def testeReceberPedidoDiaSystemError(self):
        print("\nTeste da Bicicletaria recebendo pedido por Dia. - System Error")
        self.loja = Loja(20, 20)
        self.assertEqual(self.loja.receberPedidoDia(22, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 0)


    def testeReceberPedidoSemanaFamilia(self):
        print("\nTeste da Bicicletaria recebendo pedido por Semana")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoSemana(4, datetime.datetime(2021, 8, 20, 18, 00, 00, 00), datetime.datetime(2021, 8, 27, 17, 00, 00, 00)), 280)

    def testeReceberPedidoSemanaSemana(self):
        print("\nTeste da Bicicletaria recebendo pedido por Semana")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoSemana(2, datetime.datetime(2021, 8, 20, 18, 00, 00, 00), datetime.datetime(2021, 8, 27, 17, 00, 00, 00)), 200)
    
    def testeReceberPedidoSemanaValueError(self):
        print("\nTeste da Bicicletaria recebendo pedido por Semana. - Erro ValueError")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoDia(-1, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 0)

    def testeReceberPedidoSemanaSystemError(self):
        print("\nTeste da Bicicletaria recebendo pedido por Semana. - System Error")
        self.loja = Loja(20, 20)
        self.assertEqual(self.loja.receberPedidoDia(22, datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 18, 00, 00, 00)), 0)

    def testeReceberPedidoSemanaSemana2(self): # neste teste, simulamos o periodo de 8 dias, portanto, resultando em um aluguel de 2 semanas.
        print("\nTeste da Bicicletaria recebendo pedido por Semana")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedidoSemana(2, datetime.datetime(2021, 8, 20, 18, 00, 00, 00), datetime.datetime(2021, 8, 27, 19, 00, 00, 00)), 400)

    def testeReceberPagamento(self):
        print("\nTeste da Bicicletaria recebendo pagamento")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(600, 600), 0)  

    def testeReceberPagamentoMenorQueZero(self):
        print("\nTeste da Bicicletaria recebendo pagamento menor que Zero. Value Error")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(600, -10), 600)  

    def testeReceberContaMenorQueZero(self):
        print("\nTeste da Bicicletaria recebendo conta menor que Zero Value Error")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(-10, 50), -10)  

    def testeReceberContaMenorQueValorPago(self):
        print("\nTeste da Bicicletaria recebendo valor maior que a conta")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(190, 200), 10)  

    def testeReceberPgtoMenorValorConta(self):
        print("\nTeste da Bicicletaria recebendo pagamento menor que o valor da Conta.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(200, 150), 50) 
    
    def testeAlugarBike(self):
        print("\nTeste Cliente - Alugar Bike")
        self.loja = Cliente("Marcelo", 32) 
        self.assertEqual(self.cliente.alugarBike(2, Loja(200, 20)), )




if __name__ == "__main__":
    unittest.main()
