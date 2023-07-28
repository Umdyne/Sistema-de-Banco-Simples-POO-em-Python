import abc
from Cliente import Cliente

class Banco():
    def __init__(self):
        self._qtde_contas = 0
        self._clientes = []
        self._qtde_contas_seguros = []
    
    @property
    def get_qtde_contas(self):
        return self._qtde_contas

    @get_qtde_contas.setter
    def set_qtde_contas(self, novo):
        self._qtde_contas = int(novo)
        

    @property
    def get_qtde_seguros(self):
        return self._qtde_contas_seguros

    @property
    def set_qtde_seguros(self, novo):
        self._qtde_contas_seguros = novo

    def cadastro_cliente(self):
        nome = input("Digite o nome do Cliente: ")
        cpf = "0"
        while type(cpf) != int or cpf < 9999999999 or cpf > 99999999999:
            try:
                cpf = int(input("Digite os numeros CPF: "))
            except:
                print("CPF invalido.") 
        print("Cadastro Concluido.")   

        cliente  = (nome, cpf)
        self._clientes.append(cliente)
        self.set_qtde_contas( get)

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
                self.cadastro_cliente()

       
banco = Banco()
banco.cadastro_cliente()
print(banco.get_qtde_contas)
