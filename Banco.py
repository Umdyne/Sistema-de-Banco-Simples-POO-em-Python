import abc
import Conta
from Cliente import Cliente 

class Banco():
    def __init__(self):
        self._qtde_contas = 0
        self._clientes = []
        self._qtde_contas_seguros = []
    
    @property
    def qtde_contas(self):
        return self._qtde_contas

    @qtde_contas.setter
    def qtde_contas(self, novo):
        self._qtde_contas = novo


    def cpfcadastrado(self , cpf):
        existe = 0
        print('ento')
        for contas in self._clientes:
            if cpf == contas.cpf:
                existe += 1
        if existe == 1:
            print("s")
            return 1
        else:
            print("n")
            return 0

        
    def cadastro_cliente(self):
        nome = input("Digite o nome do Cliente: ")
        cpf = "0"
        while type(cpf) != int : #or cpf < 9999999999 or cpf > 99999999999
            try:
                cpf = int(input("Digite os numeros CPF: "))
                existe = 0
                for contas in self._clientes:
                    if cpf == contas.cpf:
                        existe += 1
                    if existe != 0:   
                        print("Este CPF ja esta cadastrado, insira outro.")
                        cpf = '0'
                        break
            except:
                pass 
         
        cliente  = Cliente(nome, cpf)
        self._clientes.append(cliente)
        self.qtde_contas += 1
        print("Cadastro Concluido.")

    
        
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
banco.cadastro_cliente()
banco.cadastro_cliente()
