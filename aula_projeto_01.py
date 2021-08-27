class Sorveteria(object):
    def __init__(self, estoque, precoUnitario, caixa):
        self.estoque = estoque
        self.precoUnitario = precoUnitario
        self.caixa = caixa

    def receberPedido(self, numSorvetes):
        try:
            if numSorvetes <= 0:
                raise ValueError("Quantidade inválida")
            if numSorvetes > self.estoque:
                raise SystemError("Estoque indisponível.")

            self.estoque = self.estoque - numSorvetes
            print(f"Sorveteria = Pedido de {numSorvetes} de sorvetes efetuados. Estoque: {self.estoque}. Valor do pedido: R$ {numSorvetes * self.precoUnitario:.2f}")
            return numSorvetes * self.precoUnitario
        except ValueError:
            print(f"Sorveteria = Pedido não efetuado por quantidade inválida. Estoque: {self.estoque}.")
            return 0
        except SystemError:
            print(f"Sorveteria = Pedido não efetuado por falta de estoque. Estoque: {self.estoque}.")
        except:
            print(f"Sorveteria = Pedido não efetuado. Estoque: {self.estoque}.")
            return 0


class Cliente(object):
    pass


pessoa = Sorveteria(50, 5, 200)
pessoa.receberPedido(5)
