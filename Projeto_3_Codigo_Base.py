class Loja(object):

    def __init__(self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        self.aluguelHora = 5
        self.aluguelDia = 25
        self.aluguelSemana = 100
        self.aluguelFamilia = 0

    def receberPedido(self, tipoAluguel, qtdeBike, periodo):
       
        self.estoque -= qtdeBike # ´só retirar do estoque depois que validar a quantidade de bike
        #linha 13 a 15 respons do cliente

        try:
            if qtdeBike < 0:
                raise ValueError("Quantidade inválida.")
            elif qtdeBike > self.estoque:
                raise SystemError("Quantidade inválida.")
            elif 3 <= qtdeBike <= 5:
                if tipoAluguel  == "H" or tipoAluguel == "h": #(tipoAluguel.upper resolveria a questão do H ou h)
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bikes por {self.periodo} hora(s). Você ganhou um desconto de 30% por ter escolhido nosso plano Familia.")
                    return qtdeBike*(self.aluguelHora*periodo)*0.70
                elif tipoAluguel == "D" or tipoAluguel == "d":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bikes por {self.periodo} dia(s). Você ganhou um desconto de 30% por ter escolhido nosso plano Familia.")
                    return qtdeBike*(self.aluguelDia*periodo)*0.70
                elif tipoAluguel == "S" or tipoAluguel == "s":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bikes por {self.periodo} semana(s). Você ganhou um desconto de 30% por ter escolhido nosso plano Familia.")
                    return qtdeBike*(self.aluguelSemana*self.periodo)*0.70
            elif qtdeBike < 3:
                if tipoAluguel == "H" or tipoAluguel == "h":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) pelo periodo de {self.periodo} hora(s).")
                    return qtdeBike*(self.aluguelHora*periodo)
                elif self.tipoAluguel == "D" or tipoAluguel == "d":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) pelo periodo de {periodo} dia(s).")
                    return qtdeBike*(self.aluguelDia*periodo)
                elif self.tipoAluguel == "S" or tipoAluguel == "s":
                    print(f"Bicicletaria - Aluguel de {self.qtdeBike} bike(s) pelo periodo de {periodo} semana(s).")
                    return qtdeBike*(self.aluguelSemana*periodo)
            else:
                print("Tipo de aluguel, quantidade ou período inválido.")

        except ValueError:
            print("Bicicletaria - Quantidade de bike inválida. Deve-se escolher uma quantidade de bikes para aluguel maior que zero.")
            return 0

        except SystemError:
            print(f"Bicicletaria - Quantidade de bikes indisponivel em estoque. Escolha uma quantidade de acordo com a disponibilidade {self.estoque}.")
            return 0

        except:
            print(f"Bicicletaria - Pedido não efetuado. Quantidade de bikes disponiveis para locação: {self.estoque}.")  

    def receberPagamento(self, valorConta, valorPgto):
        try:
            if valorPgto <= 0 or valorConta <= 0:
                raise ValueError("Valor inválido")

            if valorConta == valorPgto:
                self.caixa += valorPgto
                print(f"Bicicletaria - O valor da conta é R$ {valorConta}. O valor pago foi R$ {valorPgto}. Obrigado e volte sempre!")
                return valorConta - valorPgto

            if valorConta < valorPgto:
                self.caixa += valorConta
                print(f"Bicicletaria - O valor da conta é R$ {valorConta}. O valor pago foi R$ {valorPgto}. O valor do troco é R$ {valorPgto - valorConta}.")
                return valorPgto - valorConta

            if valorPgto < valorConta:
                self.caixa += valorPgto
                print(f"Bicicletaria - O valor da conta é R$ {valorConta}. O valor pago foi R$ {valorPgto}. Portanto, ainda há um saldo de R$ {valorConta - valorPgto} em aberto.")   
                return valorConta - valorPgto

            print("Extrato de Locação de Bicicleta")
            print("Tipo Plano\tQtdeBike\tDuração da Locação\t")

        except ValueError:
            print(f"Valor inválido. Valor da Conta: R$ {valorConta}. Valor Pago: R$ {valorPgto}.")
            return valorConta
        except:
            print("Aconteceu alguma coisa. Favor realizar o pagamento. ")
            return valorConta
    
    def devolverBike(self):
        pass

    def calcularConta(self):
        pass

class Cliente(object):

    def __init__(self, nome, saldoContaCorrente):
        self.nome = nome
        self.saldoContaCorrente = saldoContaCorrente
        self.contaLocacao = 0.0
        self.periodo = None  # pensar em um novo nome
        self.qtdeBike = None # responsabilidade de quantidade de bike é do cliente, não da loja
        self.tipoAluguel = None  # tipoAluguel = H - hora, D - dia, S - semana

    def alugarBike(self, qtdeBike, tipoAluguel, objetoBicicletaria):

        try:
            if qtdeBike <= 0:
                raise ValueError("Quantidade inválida. Por favor escolha a quantidade de Bike(s) que deseja alugar. ")
            elif not isinstance(objetoBicicletaria, Loja):
                raise SystemError("Não recebeu uma Bicicletaria ")
            self.contaLocacao += objetoBicicletaria.receberPedido(qtdeBike, self.periodo)   

        except ValueError:
            print(f"Cliente {self.nome}. Impossivel realizar o pedido pois a quantidade escolhida {qtdeBike} é inválida.")
            return 0

        except SystemError:
            print(f"Cliente {self.nome}. Impossivel realizar o pedido pois a bicicletaria não é válida.")
            return 0

        except:
            print(f"Cliente - {self.nome}. Pedido não efetuado. Conta {self.contaLocacao}")
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

    
    def devolverBike(self):
        pass
    

"""Loja - def __init__(self, estoque, caixa):"""
"""def receberPedido(self, tipoAluguel, qtdeBike, periodo):"""
pessoa1 = Loja(50, 1000)
pessoa1.receberPedido("s", 5, 10)
