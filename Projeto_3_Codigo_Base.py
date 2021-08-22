class Loja(object):

    def __init__(self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        self.aluguelHora = 5
        self.aluguelDia = 25
        self.aluguelSemana = 100
        self.aluguelFamilia = 0
      
       
    def receberPedido(self, qtdeBike, tipoAluguel, periodo):
        self.estoque -= qtdeBike
        self.qtdeBike = qtdeBike
        self.tipoAluguel = tipoAluguel  # tipoAluguel = H - hora, D - dia, S - semana, F - familia
        self.periodo = periodo # Horas, Dias ou Semanas

        if self.tipoAluguel == "H":
            print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) do tipo {self.tipoAluguel} pelo periodo de {self.aluguelHora*periodo}.")
            return self.aluguelHora*periodo

        if self.tipoAluguel == "D":
            print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) do tipo {self.tipoAluguel} pelo periodo de {self.aluguelDia*periodo}.")
            return self.aluguelDia*periodo
        
        if self.tipoAluguel == "S":
            print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) do tipo {self.tipoAluguel} pelo periodo de {self.aluguelSemana*periodo}.")
            return self.aluguelSemana*periodo

        if qtdeBike >= 3 <= 5:
            if self.tipoAluguel == "F":
                print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) do tipo {self.tipoAluguel} pelo periodo de {periodo}.")
                return (qtdeBike*(self.aluguelHora) + qtdeBike*(self.aluguelDia) + qtdeBike*(self.aluguelSemana))*0.70
            
        else:
            print("Tipo de aluguel inválido")
              

    def receberPagamento(self, valorConta, valorPgto):
        try:
            if valorPgto <= 0 or valorConta <= 0:
                raise ValueError("Valor inválido")

            if valorConta == valorPgto:
                self.caixa += valorPgto

            if valorConta < valorPgto:
                self.caixa += valorConta
                return (valorPgto - valorConta)

            print("Extrato de Locação de Bicicleta")
            print("Tipo Plano\tQtdeBike\tDuração da Locação\t")

        except ValueError:
            print(f"Valor inválido. Valor da Conta: R$ {valorConta}. Valor Pago: R$ {valorPgto}.")
            return valorConta

        except:
            print("Aconteceu alguma coisa. Favor realizar o pagamento. ")
            return valorConta
    

class Cliente(object):

    def __init__(self, nome, saldoContaCorrente):
        self.nome = nome
        self.saldoContaCorrente = saldoContaCorrente
        self.contaLocacao = 0.0

    
        
    def alugarBike(self, qtdeBike, objetoBicicletaria):
        try:
            if qtdeBike <= 0:
                raise ValueError("Quantidade inválida. Por favor escolha a quantidade de Bike(s) que deseja alugar. ")

            if not isinstance(objetoBicicletaria, Loja):
                raise SystemError("Não recebeu ma Bicicletaria ")     

            self.contaLocacao += objetoBicicletaria.receberPedido(qtdeBike, self.tipoAluguel, self.periodo)   

        except ValueError:
            print(f"Cliente {self.nome}. Impossivel realizar o pedido pois a quantidade escolhida {qtdeBike} é inválida.")
            return 0

        except SystemError:
            print(f"Cliente {self.nome}. Impossivel realizar o pedido pois a bicicletaria não é válida.")
            return 0

        except:
            print(f"Cliente - {self.nome}. Pedido não efetuado. Conta {self.conta}")
            return 0


    def pagarConta(self, valorPgto, objetoBicicletaria):
        try:

            if valorPgto <= 0:
                raise ValueError("Valor inválido")
            
            if valorPgto > self.saldoContaCorrente:
                raise ArithmeticError("Valor da conta superior ao saldo disponivel em conta corrente para pagamento. ")

            if not isinstance(objetoBicicletaria, Loja):
                raise SystemError("Não recebeu uma Bicicletaria ")     

            self.saldoContaCorrente -= valorPgto
            divida = objetoBicicletaria.receberPagamento(self.contaLocacao, valorPgto)

            if divida == 0:
                self.contaLocacao = 0
            if divida > 0:
                self.contaLocacao = divida
            else:
                self.saldoContaCorrente -= divida
                self.contaLocacao = 0
            print(f"Cliente{self.nome} - Pagamento de R$ {valorPgto} da conta de R$ {self.contaLocacao} feito. Conta: R$ {self.contaLocacao}. Saldo conta corrente: R$ {self.saldoContaCorrente}")

        
        except ValueError:
            print(f"Cliente - {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado. {valorPgto} deve ser compativel com o valor da conta {self.contaLocacao} ")
            return 0

        except ArithmeticError:
            print(f"Cliente - {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado. {valorPgto} superior ao saldo da conta corrente {self.saldoContaCorrente} ")
            return 0

        except SystemError:
            print(f"Cliente - {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado pois a bicicletaria não é válida. Valor pagamento {valorPgto}. Saldo em conta {self.contaLocacao}. ")
            return 0

        except:
            print(f"Cliente - {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado. Conta {self.contaLocacao}, saldo conta corrente {self.saldoContaCorrente} ")
            return 0

    