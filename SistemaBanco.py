from abc import ABC, abstractmethod
from random import randint


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
    def __init__(self):
        self.saldo = self.getSaldo()
        self.gastos = self.getGastos()

    def mostrarExtrato(self):
        print("Você está vendo seu extrato. Gastando muito com Ifood!.")
        print("Dia | Gasto")
        for i in range(0, len(self.gastos)):
            print(str(i) + " " + str(self.gastos[i]))

    def mostrarSaldo(self):
        print("Você está completamente milionário e seu saldo segue abaixo.")
        print(self.saldo)

    def envia(self, valor):
        if (self.saldo < valor):
            print("Consiga mais dinheiro. Saldo insuficiente")
            return
        print(str(valor) + " " + "reais enviados para o destino solicitado. Aproveite as novidades com PIX!")
        self.updateSaldo(valor, '-')
        self.mostrarSaldo()

    def getSaldo(self):
        # Em um sistema de verdade, aqui puxaria do DB
        valor = 929478/25
        return valor

    def getGastos(self):
        gastos = []
        for i in range(0, 30):
            gastos.append(randint(100, 150))
        return gastos

    def updateSaldo(self, valor, op):
        if op == '+':
            self.saldo = self.saldo+valor
        if op == '-':
            self.saldo = self.saldo-valor


class Agent: # Invoker
    def __init__(self):
        self.__order_queue = []

    def trabalha(self, acao):
        self.acao = acao
        acao.execute()


if __name__ == "__main__":
    #Cliente
    sistema = Sistema()
    ver_saldo = VerificaSaldo(sistema)
    ver_extrato = VerificaExtrato(sistema, )
    transfere_valor = Transfere(sistema, 1000)

    #Agente
    trabalhador = Agent()
    trabalhador.trabalha(ver_saldo)
    trabalhador.trabalha(ver_extrato)
    trabalhador.trabalha(transfere_valor)