class Cliente():

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._conta_corrente = 0
        self._conta_poupanca = 0

    @property
    def get_nome(self):
        return str(self._nome)

    @property
    def get_cpf(self):
        return self._cpf

    def imprimir(self):
        print("Nome:",self.get_nome)
        print("CPF:",self.get_cpf)

    def criar_conta_corrente(self):
        if self._conta_corrente == 0:
            criarC = input("Digite 'sim' para criar uma Conta Corrente: ")
            if criarC.lower() == 'sim':
                self._conta_corrente = 1
                print("Conta Corrente criada com sucesso")



    

