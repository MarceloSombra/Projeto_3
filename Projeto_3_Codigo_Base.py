import datetime
import math
class Loja(object):
    def __init__(self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        self.aluguelHora = 5
        self.aluguelDia = 25
        self.aluguelSemana = 100
        
     
    def receberPedido(self, qtdeBike):
        try:
            if qtdeBike <= 0:
                raise ValueError("Quantidade invalida")

            if qtdeBike > self.estoque:
                raise SystemError("Estoque indisponivel")

            self.estoque -= qtdeBike
            print(f"LojaBike - Pedido de {qtdeBike} bike(s) efetuado. Estoque: {self.estoque} ")
            return 0

        except ValueError:
            print(f"LojaBike - Pedido de {qtdeBike} bike(s) não efetuado por quantidade inválida. Estoque: {self.estoque}")
            return 0
        except SystemError:
            print(f"LojaBike - Pedido de {qtdeBike} bike(s) não efetuado por falta de estoque. Estoque: {self.estoque}")
            return 0
        except:
            print(f"LojaBike - Pedido de {qtdeBike} bike(s) não efetuado. Estoque: {self.estoque}")
            return 0

    def calcularConta(self, qtdeBike, tipoAluguel, retiraBike, devolveBike):
        self.qtdeBike = qtdeBike
        self.tipoAluguel = tipoAluguel
        self.tempoLocacao = devolveBike - retiraBike
        self.totalHoras = math.ceil(self.tempoLocacao.seconds / 3600) + self.tempoLocacao.days * 24
        self.totalDias = math.ceil(self.tempoLocacao.seconds / 3600 / 24) + self.tempoLocacao.days
        self.totalSemanas = math.ceil(self.tempoLocacao.days / 7 + self.tempoLocacao.seconds / 3600 / 24 / 7)
    
        try:
            if qtdeBike <= 0:
                raise ValueError("Quantidade invalida.")

            elif qtdeBike > self.estoque:
                raise SystemError("Quantidade inválida.")

            if qtdeBike < 3:
                if tipoAluguel.upper() == "H":
                    print(f"Pedido recebido. {qtdeBike} bike(s) alugada(s) pelo plano por Hora. O valor Total é: R$ {qtdeBike*(self.aluguelHora*self.totalHoras)} ")
                    return qtdeBike*(self.aluguelHora*self.totalHoras)
                elif tipoAluguel.upper() == "D":
                    print(f"Pedido recebido. {qtdeBike} bike(s) alugada(s) pelo plano por Dia. O valor Total é: R$ {qtdeBike*(self.aluguelDia*self.totalDias)}")
                    return qtdeBike*(self.aluguelDia*self.totalDias)
                elif tipoAluguel.upper() == "S":
                    print(f"Pedido recebido. {qtdeBike} bike(s) alugada(s) pelo plano por Semana. O valor Total é: R$ {qtdeBike*(self.aluguelSemana*self.totalSemanas)}")
                    return qtdeBike*(self.aluguelSemana*self.totalSemanas)
            
            if qtdeBike >= 3:
                if tipoAluguel.upper() == "H":
                    print(f"Pedido recebido. {qtdeBike} bike(s) alugadas pelo plano por Hora--Familia. O valor Total é: R$ {(qtdeBike*(self.aluguelHora*self.totalHoras)*0.70)}.")
                    return (qtdeBike*(self.aluguelHora*self.totalHoras)*0.70)
                elif tipoAluguel.upper() == "D":
                    print(f"Pedido recebido. {qtdeBike} bike(s) alugadas pelo plano por Dia--Familia. O valor Total é: R$ {(qtdeBike*(self.aluguelDia*self.totalDias)*0.70)}.")
                    return (qtdeBike*(self.aluguelDia*self.totalDias)*0.70)
                elif tipoAluguel.upper() == "S":
                    print(f"Pedido recebido. {qtdeBike} bike(s) alugadas pelo plano por Semana--Familia. O valor Total é: R$ {(qtdeBike*(self.aluguelSemana*self.totalSemanas)*0.70)}.")
                    return (qtdeBike*(self.aluguelSemana*self.totalSemanas)*0.70)

            print(f"Loja - Pedido de {qtdeBike} bike(s) realizado. Tipo de aluguel {tipoAluguel}. ")
        
        except ValueError:
            print("LojaBike - Quantidade de bike inválida. Deve-se escolher uma quantidade de bikes para aluguel maior que zero.")
            return 0

        except SystemError:
            print(f"LojaBike - Não há bikes diposnivel em estoque. Qtde disponivel em estoque {self.estoque}. Escolha uma quantidade de acordo com a disponibilidade.")
            return 0

        except:
            print(f"LojaBike - Pedido não efetuado. Quantidade de bikes disponiveis para locação: {self.estoque}.")
            return 0
        


    def receberPagamento(self, valorConta, valorPgto):
        try:
            if valorPgto <= 0 or valorConta <= 0:
                raise ValueError("Valor(es) inválido(s)")

            elif valorConta == valorPgto:
                self.caixa = self.caixa + valorPgto
                print(f"Bicicletaria - O valor da conta é R$ {valorConta}. O valor pago foi R$ {valorPgto}. Obrigado e volte sempre!")
                return valorConta - valorPgto

            elif valorConta < valorPgto:
                self.caixa = self.caixa + valorConta
                print(f"Bicicletaria - O valor da conta é R$ {valorConta}. O valor pago foi R$ {valorPgto}. O valor do troco é R$ {valorPgto - valorConta}.")
                return valorPgto - valorConta

            elif valorPgto < valorConta:
                self.caixa = self.caixa + valorPgto
                print(f"Bicicletaria - O valor da conta é R$ {valorConta}. O valor pago foi R$ {valorPgto}. Portanto, ainda há um saldo de R$ {valorConta - valorPgto} em aberto.")
                return valorConta - valorPgto

        except ValueError:
            print(f"Valor(es) inválido(s). Valor da Conta: R$ {valorConta}. Valor Pago: R$ {valorPgto}.")
            return valorConta
        except:
            print("Aconteceu alguma coisa. Favor realizar o pagamento. ")
            return valorConta   
    

    
class Cliente(object):
    def __init__(self, nome, saldoContaCorrente):
        self.nome = nome
        self.saldoContaCorrente = saldoContaCorrente
        self.contaLocacao = 0.0
        self.retiraBike = None  
        self.devolveBike = None 
        self.tipoAluguel = None  # tipoAluguel = H - hora, D - dia, S - semana

    def fazerPedido(self, qtdeBike, tipoAluguel, objetoLoja):
    
        if qtdeBike <= 0:
            raise ValueError("Quantidade invalida")

        print(f"Cliente {self.nome} - Pedido de {qtdeBike} bike(s). Tipo de aluguel: {tipoAluguel}.")
        return -1
    
    def devolverBike(self, tipoAluguel, retiraBike, devolveBike):
        self.tempoLocacao = retiraBike - devolveBike
        self.tipoAluguel = tipoAluguel
        
        if self.tipoAluguel == "H":
            return print(f"Cliente - Tempo total de locação: {self.totalHoras} hora(s).")
        elif self.tipoAluguel == "D":
            return print(f"Cliente - Tempo total de locação: {self.totalDias} dias(s).")
        elif self.tipoAluguel == "S":
            return print(f"Cliente - Tempo total de locação: {self.totalSemanas} semana(s).")

    def pagarConta(self, valorPgto, objetoLoja):
        try:
            if not isinstance(objetoLoja, Loja):
                raise SystemError("Não recebeu uma Loja")

            self.saldoContaCorrente -= valorPgto
            divida = objetoLoja.receberPagamento(self.valorConta)
            print(f"Cliente {self.nome} - Pagamento de R${valorPgto}.")
            if divida == 0:
                self.contaLocacao = 0
            elif divida > 0:
                self.contaLocacao = divida
            else:
                self.saldoContaCorrente -= divida
                self.contaLocacao = 0
            return self.saldoContaCorrente

        except SystemError:
            print(f"Bicicletaria - Quantidade de bikes indisponivel em estoque. Escolha uma quantidade de acordo com a disponibilidade.")
          
        except:
            print(f"Bicicletaria - Pedido não efetuado. Quantidade de bikes disponiveis para locação:.")

        
#bicicletaria1 = Loja(50, 1000)  # Loja - def __init__(self, estoque, caixa)
#pessoa2 = Cliente("Fábio", 1000)  # Cliente - def __init__(self, nome, saldoContaCorrente)
#bicicletaria1.receberPedido("H", 5, 10)  # OK  def receberPedido(self, tipoAluguel, qtdeBike, periodo)
#pessoa2.alugarBike(5, bicicletaria1)  # def alugarBike(self, qtdeBike, classeLoja)
#pessoa2.pagarConta(300, bicicletaria1)  # def pagarConta(self, valorPgto, classeLoja):
#bicicletaria1.receberPagamento(300, 300)  # OK  def receberPagamento(self, valorConta, valorPgto)










