class Cliente():

    def __init__ (self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._contaC = 0
        self._contaP = 0
        self._seguro = []
        self._qtde_seguro = 0
        self._qtde_contas = 0

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

    @property
    def seguro(self):
        return self._seguro

    @seguro.setter
    def seguro(self, novo_seguro):
        self._seguro.append(novo_seguro)

    @property
    def qtde_contas(self):
        if self._contaC == 0 and self._contaP == 0:
            return 0
        elif self._contaC != 0 and self._contaP != 0:
            return 2
        else:
            return 1

    @property
    def qtde_seguro(self):
        return self._qtde_seguro

    @qtde_seguro.setter
    def qtde_seguro(self, nova_qtde_seguro):
        self._qtde_seguro = nova_qtde_seguro    
        
    def imprimir(self):
        print("Nome: ",self.nome)
        print("CPF: ",self.cpf)

    def __str__(self):
        return f"{self.cpf}"



