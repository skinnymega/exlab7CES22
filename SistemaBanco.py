from abc import ABC, abstractmethod


class Order(ABC): # Abstract Command
    @abstractmethod
    def execute(self):
        pass


class VerificaSaldo(Order):  # Concrete Command
    def __init__(self, saldo):
        self.saldo = saldo

    def execute(self):
        self.saldo.mostrarSaldo()


class VerificaExtrato(Order):  # Concrete Command
    def __init__(self, extrato):
        self.extrato = extrato

    def execute(self):
        self.extrato.mostrarExtrato()


class Transfere(Order): # Concrete Command
    def __init__(self, destino, valor):
        self.destino = destino
        self.valor = valor

    def execute(self):
        self.destino.envia(self.valor)


class Sistema: # Receiver
    def mostrarExtrato(self):
        print("Você está vendo seu extrato. Trate de economizar.")

    def mostrarSaldo(self):
        print("Você está completamente milionário e seu saldo segue abaixo.")

    def envia(self, valor):
        print(str(valor) + " " + "reais enviados para o destino solicitado. Aproveite as novidades com PIX!")


class Agent: #Invoker
    def __init__(self):
        self.__order_queue = []

    def trabalha(self, acao):
        self.acao = acao
        acao.execute()


if __name__ == "__main__":
    #Cliente
    sistema = Sistema()
    ver_saldo = VerificaSaldo(sistema)
    ver_extrato = VerificaExtrato(sistema)
    transfere_valor = Transfere(sistema, 1000)

    #Agente
    trabalhador = Agent()
    trabalhador.trabalha(ver_saldo)
    trabalhador.trabalha(ver_extrato)
    trabalhador.trabalha(transfere_valor)