class Loja(object):

    def __init__(self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        self.aluguelHora = 5
        self.aluguelDia = 25
        self.aluguelSemana = 100
        self.aluguelFamilia = 0

    def receberPedido(self, tipoAluguel, qtdeBike, periodo):  # bicicletaria1.receberPedido("H", 5, 10)
        self.estoque -= qtdeBike
        self.qtdeBike = qtdeBike
        self.tipoAluguel = tipoAluguel  # tipoAluguel = H - hora, D - dia, S - semana
        self.periodo = periodo  # Horas, Dias ou Semanas

        try:
            if qtdeBike < 0:
                raise ValueError("Quantidade inválida.")
            elif qtdeBike > self.estoque:
                raise SystemError("Quantidade inválida.")
            elif 3 <= qtdeBike <= 5:
                if tipoAluguel == "H" or tipoAluguel == "h":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bikes por {self.periodo} hora(s). Você ganhou um desconto de 30% por ter escolhido nosso plano Familia.")
                    return qtdeBike*(self.aluguelHora*periodo)*0.70
                elif tipoAluguel == "D" or tipoAluguel == "d":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bikes por {self.periodo} dia(s). Você ganhou um desconto de 30% por ter escolhido nosso plano Familia.")
                    return qtdeBike*(self.aluguelDia*periodo)*0.70
                elif tipoAluguel == "S" or tipoAluguel == "s":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bikes por {self.periodo} semana(s). Você ganhou um desconto de 30% por ter escolhido nosso plano Familia.")
                    return qtdeBike*(self.aluguelSemana*self.periodo)*0.70
            elif 1 <= qtdeBike < 3:
                if tipoAluguel == "H" or tipoAluguel == "h":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) pelo periodo de {self.periodo} hora(s).")
                    return qtdeBike*self.aluguelHora*periodo
                elif self.tipoAluguel == "D" or tipoAluguel == "d":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) pelo periodo de {periodo} dia(s).")
                    return qtdeBike*self.aluguelDia*periodo
                elif self.tipoAluguel == "S" or tipoAluguel == "s":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) pelo periodo de {periodo} semana(s).")
                    return qtdeBike*self.aluguelSemana*periodo
            else:
                print("Tipo de aluguel, quantidade ou período inválido.")
        except ValueError:
            print("Bicicletaria - Quantidade de bike inválida. Deve-se escolher uma quantidade de bikes para aluguel maior que zero.")
            return 0
        except SystemError:
            print(f"Bicicletaria - Quantidade de bikes indisponivel em estoque. Escolha uma quantidade de acordo com a disponibilidade.")
            return 0
        except:
            print(f"Bicicletaria - Pedido não efetuado. Quantidade de bikes disponiveis para locação: {self.estoque}.")

    def receberPagamento(self, valorConta, valorPgto):
        self.valorConta = valorConta
        self.valorPgto = valorPgto
        try:
            if (self.valorPgto <= 0) or (self.valorConta <= 0):
                raise ValueError("Valor(es) inválido(s)")
            elif self.valorConta == self.valorPgto:
                self.caixa = self.caixa + self.valorPgto
                print(f"Bicicletaria - O valor da conta é R$ {self.valorConta}. O valor pago foi R$ {self.valorPgto}. Obrigado e volte sempre!")
                return self.valorConta - self.valorPgto
            elif self.valorConta < self.valorPgto:
                self.caixa = self.caixa + self.valorConta
                print(f"Bicicletaria - O valor da conta é R$ {self.valorConta}. O valor pago foi R$ {self.valorPgto}. O valor do troco é R$ {self.valorPgto - self.valorConta}.")
                return self.valorPgto - self.valorConta
            elif self.valorPgto < self.valorConta:
                self.caixa = self.caixa + self.valorPgto
                print(f"Bicicletaria - O valor da conta é R$ {self.valorConta}. O valor pago foi R$ {self.valorPgto}. Portanto, ainda há um saldo de R$ {self.valorConta - self.valorPgto} em aberto.")
                return self.valorConta - self.valorPgto
            print("Extrato de Locação de Bicicleta")
            print("Tipo Plano\tQtdeBike\tDuração da Locação\t")
        except ValueError:
            print(f"Valor(es) inválido(s). Valor da Conta: R$ {self.valorConta}. Valor Pago: R$ {self.valorPgto}.")
            return self.valorConta
        except:
            print("Aconteceu alguma coisa. Favor realizar o pagamento. ")
            return self.valorConta


class Cliente(object):

    def __init__(self, nome, saldoContaCorrente):
        self.nome = nome
        self.saldoContaCorrente = saldoContaCorrente
        self.contaLocacao = 0
        
    def alugarBike(self, qtdeBike, classeLoja):  # pessoa2.alugarBike(5, bicicletaria1)
        try:
            if qtdeBike <= 0:
                raise ValueError("Quantidade inválida. Por favor escolha a quantidade de Bike(s) que deseja alugar. ")
            elif not isinstance(classeLoja, Loja):
                raise SystemError("Não recebeu uma Bicicletaria ")
            elif 1 <= qtdeBike <= 5:
                self.contaLocacao = self.contaLocacao + classeLoja.receberPedido(self.tipoAluguel, qtdeBike, self.periodo)
                print(f"Cliente {self.nome} - Pedido de {qtdeBike} bicicleta(s) feita. Conta: {self.contaLocacao}")
                return self.contaLocacao

        except ValueError:
            print(f"Cliente {self.nome}. Impossivel realizar o pedido pois a quantidade escolhida {qtdeBike} é inválida.")
            return 0
        except SystemError:
            print(f"Cliente {self.nome}. Impossivel realizar o pedido pois a bicicletaria não é válida.")
            return 0
        except:
            print(f"Cliente {self.nome}. Pedido não efetuado. Conta {self.contaLocacao}")
            return 0

    def pagarConta(self, valorPgto, classeLoja):
        try:
            if valorPgto <= 0:
                raise ValueError("Valor inválido")
            elif valorPgto > self.saldoContaCorrente:
                raise ArithmeticError("Valor da conta superior ao saldo disponivel em conta corrente para pagamento. ")
            elif not isinstance(classeLoja, Loja):
                raise SystemError("Não recebeu uma Bicicletaria ")
            self.saldoContaCorrente = self.saldoContaCorrente - valorPgto
            divida = classeLoja.receberPagamento(self.contaLocacao, valorPgto)
            if divida == 0:
                self.contaLocacao = 0
            elif divida > 0:
                self.contaLocacao = divida
            else:
                self.saldoContaCorrente = self.saldoContaCorrente - divida
                self.contaLocacao = 0
            print(f"Cliente {self.nome} - Pagamento de R$ {valorPgto} da conta de R$ {self.contaLocacao} feito. Conta: R$ {self.contaLocacao}. Saldo conta corrente: R$ {self.saldoContaCorrente}")
        except ValueError:
            print(f"Cliente {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado. {valorPgto} deve ser compativel com o valor da conta {self.contaLocacao} ")
            return 0
        except ArithmeticError:
            print(f"Cliente {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado. {valorPgto} superior ao saldo da conta corrente {self.saldoContaCorrente} ")
            return 0
        except SystemError:
            print(f"Cliente {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado pois a bicicletaria não é válida. Valor pagamento {valorPgto}. Saldo em conta {self.contaLocacao}. ")
            return 0
        except:
            print(f"Cliente {self.nome}. Pagamento da conta {self.contaLocacao} não foi efetuado. Conta {self.contaLocacao}, saldo conta corrente {self.saldoContaCorrente} ")
            return 0


bicicletaria1 = Loja(50, 1000)  # Loja - def __init__(self, estoque, caixa)
pessoa2 = Cliente("Fábio", 1000)  # Cliente - def __init__(self, nome, saldoContaCorrente)
bicicletaria1.receberPedido("H", 5, 10)  # OK  def receberPedido(self, tipoAluguel, qtdeBike, periodo)
pessoa2.alugarBike(5, bicicletaria1)  # def alugarBike(self, qtdeBike, classeLoja)
pessoa2.pagarConta(300, bicicletaria1)  # def pagarConta(self, valorPgto, classeLoja):
bicicletaria1.receberPagamento(300, 300)  # OK  def receberPagamento(self, valorConta, valorPgto)










