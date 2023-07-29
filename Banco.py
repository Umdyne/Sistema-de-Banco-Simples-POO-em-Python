import abc
from Conta import Conta_Corrente
from Conta import Conta_Poupanca
from Cliente import Cliente 

class Banco():
    def __init__(self):
        self._qtde_contas = 0
        self._clientes = []
        self._contasC = []
        self._qtdeC = 0
        self._contasP = []
        self._qtdeP = 0
        self._qtde_contas_seguros = []
    

    @property
    def qtde_contas(self):
        return self._qtde_contas

    @qtde_contas.setter
    def qtde_contas(self, novo):
        self._qtde_contas = novo

    @property
    def clientes(self):
        return self._clientes
        
    def cadastro_cliente(self):
        nome = input("Digite o nome do Cliente: ")
        cpf = "0"
        while type(cpf) != int  : #or cpf < 9999999999 or cpf > 99999999999
            try:
                cpf = int(input("Digite os numeros CPF: "))
                while any(cpf == cliente.cpf for cliente in self._clientes):
                    cpf = int(input("Este CPF ja esta cadastrado, insira outro: "))               
            except:
                pass 
         
        cliente  = Cliente(nome, cpf)
        self._clientes.append(cliente)
        self.qtde_contas += 1
        print("Cadastro Concluido.")

    def criarContaC(self):
        if self.qtde_contas == 0:
            print("Nenhuma cliente cadastrado para criar contas")
        else:
            cpf = int(input("Digite o CPF do cliente para criar a Conta Corrente: "))
            cliente_encontrado = None
            for cliente in self._clientes:
                if cpf == cliente.cpf:    
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado:
                if cliente_encontrado.contaC == 0:
                    self._qtdeC += 1
                    conta_corrente = Conta_Corrente(cpf, self._qtdeC)
                    cliente_encontrado.contaC = self._qtdeC
                    self._contasC.append(conta_corrente)
                    print("Conta corrente criada com sucesso.")
                else:
                    print("Esse cliente já possui uma conta corrente.")
            else:
                print("CPF digitado está incorreto ou não encontrado.")

    def criarContaP(self):
        if self.qtde_contas == 0:
            print("Nenhuma cliente cadastrado para criar contas")
        else:
            cpf = int(input("Digite o CPF do cliente para criar a Conta Poupança: "))
            cliente_encontrado = None
            for cliente in self._clientes:
                if cpf == cliente.cpf:    
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado:
                if cliente_encontrado.contaP == 0:
                    self._qtdeP += 1
                    conta_poupanca = Conta_Poupanca(cpf, self._qtdeP)
                    cliente_encontrado.contaP = self._qtdeP
                    self._contasP.append(conta_poupanca)
                    print("Conta poupança criada com sucesso.")
                else:
                    print("Esse cliente já possui uma conta poupança.")
            else:
                print("CPF digitado está incorreto ou não encontrado.")                
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
banco._clientes.append(Cliente("c1",1))
banco.qtde_contas += 1
banco.criarContaC()
