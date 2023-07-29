class Cliente():

    def __init__ (self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._contaC = 0
        self._ContaP = 0

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def contaC(self):
        return self._contaC

    @property
    def ContaP(self):
        return self._ContaP
    
    def imprimir(self):
        print("Nome: ",self.nome)
        print("CPF: ",self.cpf)

    def __str__(self):
        return f"{self.cpf}"



