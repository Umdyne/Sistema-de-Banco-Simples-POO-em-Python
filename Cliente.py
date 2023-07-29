class Cliente():

    def __init__ (self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._contaC = 0
        self._contaP = 0

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def contaC(self):
        return self._contaC
    
    @contaC.setter
    def contaC(self, valor):
        self._contaC = valor

    @property
    def contaP(self):
        return self._contaP

    @contaP.setter
    def contaP(self, valor):
        self._contaP = valor
        
    def imprimir(self):
        print("Nome: ",self.nome)
        print("CPF: ",self.cpf)

    def __str__(self):
        return f"{self.cpf}"



