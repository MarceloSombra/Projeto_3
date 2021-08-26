import unittest
from Projeto_3_Codigo_Base import Cliente, Loja

class Testes(unittest.TestCase):

    def setUp(self): # prepara o terreno de teste para todos os testes. O Setup roda primeiro e depois roda o teste abaixo. 
                     # Sempre o setUp Primeiro e depois o teste.
        self.loja = Loja(200, 20)  
        self.cliente = Cliente("Marcelo", 32) 

    def testeRecebePedidoHora(self):
        print("\nTeste da Bicicletaria recebendo pedido")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido("h", 2, 2), 20)

    def testeRecebePedidoDia(self): #
        print("\nTeste da Bicicletaria recebendo pedido")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido("D", 2, 2), 100) 

    def testeRecebePedidoSemana(self):
        print("\nTeste da Bicicletaria recebendo pedido")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido("s", 2, 2), 400)

    def testeRecebePedidoFamiliaHora(self): 
        print("\nTeste da Bicicletaria recebendo pedido")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido("h", 3, 2), 21)

    def testeRecebePedidoFamiliaDia(self): 
        print("\nTeste da Bicicletaria recebendo pedido")
        self.loja = Loja(50, 20)
        self.assertEqual(self.loja.receberPedido("d", 5, 2), 175)

    def testeRecebePedidoFamiliaSemana(self): 
        print("\nTeste da Bicicletaria recebendo pedido")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPedido("S", 4, 2), 560)

    def testeRecebePagamentoComTroco(self):
        print("\n Teste da Bicicletaria recebendo pagamento")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(560, 600), 40)
    
    def testeRecebePagamentoValorExato(self):
        print("\n Teste da Bicicletaria recebendo pagamento")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(560, 560), 0)

    def testeRecebePagamentoValorMenorQueConta(self):
        print("\n Teste da Bicicletaria recebendo pagamento")
        self.loja = Loja(200, 20)
        self.assertEqual(self.loja.receberPagamento(560, 500), 60)

    def testeAlugarBike(self):
        print("\n Quantidade de bicicletas a serem alugadas")
        self.cliente = Cliente("Marcelo", 10000)
        self.assertEqual(self.cliente.alugarBike(2, "Marcelo"), 0)

    def testePagarConta(self):
        print("\n Valor total da conta")
        self.cliente = Cliente("Marcelo", 10000)
        self.assertEqual(self.cliente.pagarConta(1, "Marcelo"), 0)



if __name__ == "__main__":
    unittest.main()

