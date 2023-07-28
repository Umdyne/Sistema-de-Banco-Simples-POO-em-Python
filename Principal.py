from Cliente import Cliente 
from Banco import Conta_Corrente

def cadastro_cliente():

    nome = input("Digite o nome do Cliente: ")
    cpf = input("Digite o CPF do Cliente: ")
    while type(cpf) != int:
        try:
            cpf = int(input("Digite os numeros CPF: "))
        except:
            print("CPF invalido.")


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

def menu():

    opc = -1
    while opc != 0:
        print("\n----------Menu------------\n")
        print("1  - Cadastrar Cliente")
        print("2  - Criar conta corrente")
        print("3  - Criar conta poupança")
        print("4  - Criar seguro de vida")
        print("5  - Calcular tributação")
        print("6  - Sacar")
        print("7  - Depositar")
        print("8  – Transferir")
        print("9  – Imprimir histórico")
        print("10 - Exibir informações do banco")
        opc = int(input("Selecione uma opção: "))

        if opc == 1:
            cadastro_cliente()
        
cadastro_cliente()
