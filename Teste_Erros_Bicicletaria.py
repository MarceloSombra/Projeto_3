import unittest
import datetime
from Projeto_3_Codigo_Base import Loja, Cliente

class Testes(unittest.TestCase):

    def setUp(self): # prepara o terreno de teste para todos os testes. O Setup roda primeiro e depois roda o teste abaixo. 
                     # Sempre o setUp Primeiro e depois o teste.
        self.loja = Loja(200, 20)  
        self.cliente = Cliente("Marcelo", 32) 

    def testeRecebePedidoIdeal(self):
        print("\nTeste Loja - Recebendo pedido em um cenário ideal")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido(150), 0)

    def testeRecebePedidoQtdeMenorQueZero(self):
        print("\nTeste Loja - Recebendo pedido inválido (ValueError) - Quantidade menor que zero.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido(-10), 0)

    def testeRecebePedidoQtdeMaiorQueEstoque(self):
        print("\nTeste Loja - Recebendo pedido inválido (SystemError) - Quantidade do pedido maior que estoque.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido(210), 0)

    #def calcularConta(self, qtdeBike, tipoAluguel, retiraBike, devolveBike):
    def testeCalculaContaCenarioIdealHora(self):
        print("\nTeste Loja - Calculando conta em um caso de aluguel de bike por HORA - Cenário Ideal.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(2, "H", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 17, 00, 00, 00)), 230)

    def testeCalculaContaCenarioIdealDia(self):
        print("\nTeste Loja - Calculando conta em um caso de aluguel de bike por DIA - Cenário Ideal.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(2, "d", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 25, 19, 00, 00, 00)), 150)

    def testeCalculaContaCenarioIdealSemana(self):
        print("\nTeste Loja - Calculando conta em um caso de aluguel de bike por SEMANA - Cenário Ideal.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(1, "S", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 31, 18, 00, 00, 00)), 200)

    def testeCalculaContaCenarioIdealHoraFamilia(self):
        print("\nTeste Loja - Calculando conta em um caso de aluguel de bike por HORA - Cenário Ideal.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(4, "H", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 17, 00, 00, 00)), 322)
    
    def testeCalculaContaCenarioIdealDiaFamilia(self):
        print("\nTeste Loja - Calculando conta em um caso de aluguel de bike por DIA - Cenário Ideal.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(5, "d", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 25, 19, 00, 00, 00)), 262.5)
    
    def testeCalculaContaCenarioIdealSemanaFamilia(self):
        print("\nTeste Loja - Calculando conta em um caso de aluguel de bike por SEMANA - Cenário Ideal.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(3, "s", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 31, 18, 00, 00, 00)), 420)

    def testeCalculaContaValueError(self):
        print("\nTeste Loja - Calculando conta. Qtde de Bike solicitada inválida (Inferior ou igual a zero).")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(0, "s", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 31, 18, 00, 00, 00)), 0)
    
    def testeCalculaContaSystemError(self):
        print("\nTeste Loja - Calculando conta. Qtde de Bike solicitada inválida (Qtde Superior ao estoque disponivel).")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.calcularConta(201, "s", datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 31, 18, 00, 00, 00)), 0)


    def testeRecebePagamentoCenarioIdeal(self):
        print("\nTeste Loja - Recebendo pagamento cenário ideal.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(400, 400), 0)

    def testeRecebePagamentoValueError(self):
        print("\nTeste Loja - Recebendo pagamento. Valor pago menor que o zero.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(400, -10), 400)

    def testeRecebePagamentoMenorQueConta(self):
        print("\nTeste Loja - Recebendo pagamento. Valor pago menor que o valor da Conta.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(400, 300), 100)

    def testeRecebePagamentoMaiorQueConta(self):
        print("\nTeste Loja - Recebendo pagamento. Valor pago maior que o valor da Conta.")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(300, 350), 50)
    
    def testeFazerPedido(self):
        print("\nTeste CLIENTE - Fazendo Pedido. ")
        self.cliente = Cliente("Marcelo", 150)
        self.assertEqual(self.cliente.fazerPedido(5, "H"), -1)

    # def devolverBike(self,  retiraBike, devolveBike):
    def testeDevolverBike(self):
        print("\nTeste CLIENTE - Devolvendo Bike.")
        self.cliente = Cliente("Marcelo", 150)
        self.assertEqual(self.cliente.devolverBike(datetime.datetime(2021, 8, 23, 18, 00, 00, 00), datetime.datetime(2021, 8, 24, 17, 00, 00, 00)), 23)
    
    # def pagarConta(self, valorPgto, objetoLoja):
    def testePagarConta(self):
        print("\nTeste CLIENTE - Pagar Conta.")
        self.cliente - Cliente("Marcelo", 150)
        self.assertEqual(self.cliente.pagarConta(150, 150), 0)

if __name__ == "__main__":
    unittest.main()

