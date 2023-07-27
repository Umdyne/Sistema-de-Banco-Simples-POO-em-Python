import abc
from Cliente import Cliente

class Conta(abc.ABC):

    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo
        self._historico = []

class Conta_Corrente(Conta):

    def __init__(self, cliente, numero, saldo):
        super().__init__(numero, saldo)
        self._cliente = cliente

    @property
    def get_numero(self):
        return str(self._numero)

    @property
    def get_saldo(self):
        return self._saldo
    
    def imprimir(self):
        self._cliente.imprimir()
        print("Numero da Conta:",self.get_numero)
        print("Saldo da Conta:",self.get_saldo)

class Conta_Poupança(Conta):

    def __init__(self, cpf_cliente, numero, saldo):
        super().__init__(numero, saldo)
        self._cpf_cliente = cpf_cliente        

        
