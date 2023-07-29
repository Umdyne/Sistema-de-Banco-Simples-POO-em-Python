import abc

class Conta(abc.ABC):

    def __init__(self, titular, numero):
        self._numero = numero
        self._saldo = 0
        self._historico = []
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo):
        self._saldo = novo
        
    @property
    def historico(self):
        return self._historico
    
    @historico.setter
    def historico(self, novo):
        self._historico.append(novo)
        
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico=("Deposito", valor)
            
        else:
            print("Não pode depositar valor negatico.")
            
    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico=("Saque", valor)
        else:
            print("Saldo insuficiente.")

    def transferencia(self, destino, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            self.historico=("Transferencia -", valor)
            destino.historico=("Transferencia +", valor)
        else:
            print("Saldo insuficiente.")

    @abc.abstractmethod
    def tributacao(self):
        pass

class Conta_Corrente(Conta):

    def __init__(self, titular, numero):
        super().__init__( titular, numero)

    def tributacao(self):
        return 10 + (self.saldo)/100    

class Conta_Poupanca(Conta):

    def __init__(self, titular, numero):
        super().__init__( titular, numero)

    def tributacao(self):
        return 10 + (self.saldo)/50


'''        
c1 = Conta_Corrente("oie", 1)
c2 = Conta_Corrente("oie2", 2)

c1.deposito(10) 
print(c1.saldo)
c1.saque(5) 
print(c1.saldo)
c1.transferencia(c2,5) 
print(c1.saldo , c2.saldo ) 
print(c1.historico)
'''
