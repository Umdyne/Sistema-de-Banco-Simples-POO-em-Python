import abc
from Conta import Conta_Corrente
from Conta import Conta_Poupanca
from Cliente import Cliente
from Seguro import Seguro_Vida

class Banco():
    def __init__(self):
        self._qtde_contas = 0
        self._clientes = []
        self._qtde_clientes = 0
        self._contasC = []
        self._contasP = []
        self._qtde_contas_seguros = 0
        self._tributacoes = []
    

    @property
    def qtde_clientes(self):
        return self._qtde_clientes

    @qtde_clientes.setter
    def qtde_clientes(self, novo):
        self._qtde_clientes = novo

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
        self.qtde_clientes += 1
        print("Cadastro Concluido.")

    def criarContaC(self):
        if self.qtde_clientes == 0:
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
                    self.qtde_contas += 1
                    conta_corrente = Conta_Corrente(cpf, self.qtde_contas)
                    cliente_encontrado.contaC = conta_corrente
                    self._contasC.append(conta_corrente)
                    print("Conta corrente criada com sucesso.")
                else:
                    print("Esse cliente já possui uma conta corrente.")
            else:
                print("CPF digitado está incorreto ou não encontrado.")

    def criarContaP(self):
        if self.qtde_clientes == 0:
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
                    self.qtde_contas += 1
                    conta_poupanca = Conta_Poupanca(cpf, self.qtde_contas)
                    cliente_encontrado.contaP = conta_poupanca
                    self._contasP.append(conta_poupanca)
                    print("Conta poupança criada com sucesso.")
                else:
                    print("Esse cliente já possui uma conta poupança.")
            else:
                print("CPF digitado está incorreto ou não encontrado.")                

    def criarSeguro(self):
        if self.qtde_clientes == 0:
            print("Nenhuma cliente cadastrado para criar seguros")
        else:
            cpf = int(input("Digite o CPF do cliente para criar o Seguro de vida: "))
            cliente_encontrado = None
            for cliente in self._clientes:
                if cpf == cliente.cpf:    
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado:
                mensal = int(input("Digite o valor mensal do seguro: "))
                total = int(input("Digite o valor total do seguro: "))
                cliente_encontrado.qtde_seguro += 1
                self._qtde_contas_seguros += 1
                seguro = Seguro_Vida(mensal, total)
                cliente_encontrado.seguro = seguro
                print("Seguro de vida criado.")

            else:
                print("CPF digitado está incorreto ou não encontrado.")    

    def tributacao(self):
        soma_seguro = 0
        soma_corrente = 0

        if self._qtdeC == 0 and self._qtde_contas_seguros == 0:
            print("Não há valores para serem calculados.")
        else:
            for conta in self._contasC:
                soma_corrente += conta.saldo / 100

            for cliente in self._clientes:
                if cliente.seguro:
                    for seguros in cliente.seguro:       
                        soma_seguro += seguros.valor_mensal / 50

            total = soma_seguro + soma_corrente + (len(self._clientes) * 10)
            self._tributacoes.append(total)
            cont = 1
            for tributacao in self._tributacoes: 
                print(f"{cont}º tributação = {total:.2f}")
                cont += 1

    def sacar(self):
        if self.qtde_clientes == 0 or self.qtde_contes == 0:
            print("Nenhuma cliente ou conta cadastrado para sacar")
        else:
            cpf = int(input("Digite o CPF do cliente para realizar o saque: "))
            cliente_encontrado = None
            for cliente in self._clientes:
                if cpf == cliente.cpf:    
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado:
                if cliente_encontrado.contaP == 0 and cliente_encontrado.contaC == 0:
                    print("Este cliente não possui contas para realizar saques.")
                elif cliente_encontrado.contaP != 0 and cliente_encontrado.contaC != 0:
                    opc = int(input("Seleciona a conta da qual deseja realizar o saque\n1 - Poupança\n2 - Corrente: "))
                    if opc == 1:
                        print("Saldo atual: ",cliente_encontrado.contaP.saldo)
                        valor = int(input("Digite o valor que deseja sacar: "))
                        cliente_encontrado.contaP.saque(valor)

                    elif opc == 2:
                        print("Saldo atual: ",cliente_encontrado.contaC.saldo)
                        valor = int(input("Digite o valor que deseja sacar: "))
                        cliente_encontrado.contaC.saque(valor)
                    else:
                        print("Opção invalida.")

                else:
                    if cliente_encontrado.contaP != 0:
                        print("Saldo atual: ",cliente_encontrado.contaP.saldo)
                        valor = int(input("Digite o valor que deseja sacar: "))
                        cliente_encontrado.contaP.saque(valor)
                    else:
                        print("Saldo atual: ",cliente_encontrado.contaC.saldo)
                        valor = int(input("Digite o valor que deseja sacar: "))
                        cliente_encontrado.contaC.saque(valor)
                           

            else:
                print("CPF digitado está incorreto ou não encontrado.")                
        

    def depositar(self):
        if self.qtde_clientes == 0 or self.qtde_contes == 0:
            print("Nenhuma cliente ou conta cadastrado para sacar")
        else:
            cpf = int(input("Digite o CPF do cliente para realizar o deposito: "))
            cliente_encontrado = None
            for cliente in self._clientes:
                if cpf == cliente.cpf:    
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado:
                if cliente_encontrado.contaP == 0 and cliente_encontrado.contaC == 0:
                    print("Este cliente não possui contas para realizar deposito.")
                elif cliente_encontrado.contaP != 0 and cliente_encontrado.contaC != 0:
                    opc = int(input("Seleciona a conta da qual deseja realizar o deposito\n1 - Poupança\n2 - Corrente: "))
                    if opc == 1:
                        valor = int(input("Digite o valor que deseja depositar: "))
                        cliente_encontrado.contaP.deposito(valor)
                        print("Saldo atual: ",cliente_encontrado.contaP.saldo)

                    elif opc == 2:
                        valor = int(input("Digite o valor que deseja depositar: "))
                        cliente_encontrado.contaC.deposito(valor)
                        print("Saldo atual: ",cliente_encontrado.contaC.saldo)
                    else:
                        print("Opção invalida.")

                else:
                    if cliente_encontrado.contaP != 0:
                        valor = int(input("Digite o valor que deseja depositar: "))
                        cliente_encontrado.contaP.deposito(valor)
                        print("Saldo atual: ",cliente_encontrado.contaP.saldo)
                    else:
                        valor = int(input("Digite o valor que deseja depositar: "))
                        cliente_encontrado.contaC.deposito(valor)
                        print("Saldo atual: ",cliente_encontrado.contaC.saldo)
                   
                 
            else:
                print("CPF digitado está incorreto ou não encontrado.")

    def tranferir(self):
        if self.qtde_clientes == 0 or self.qtde_contas == 0:
            print("Nenhuma cliente ou conta cadastrado para sacar")
        else:
            envia = recebe = False
            conta_partida = int(input("Digite o numero da conta que ira transferir: "))
            for conta in self._contasC:
                print(conta.numero)
                if conta.numero == conta_partida:
                    envia = conta
                    

            for conta in self._contasP:
                print(conta.numero)
                if conta.numero == conta_partida:
                    envia = conta
                     
                
            #tranferencia seleciona qual o tipo do destino
            conta_destino = int(input("Digite o numero da conta destino: "))
            for conta in self._contasC:
                print(conta.numero)
                if conta.numero == conta_destino:
                    recebe = conta
                    

            for conta in self._contasP:
                print(conta.numero)
                if conta.numero == conta_destino:
                    recebe = conta
                                     
 
            if envia and recebe:
                print("Saldo atual: ",envia.saldo)
                valor = int(input("Digite o valor para transferir: "))
                envia.transferencia(recebe,50)
                     
                 
            else:
                print("Um dos/Os dois numeros das contas estão incorretos.")

    def print_historico(self):
        if self.qtde_clientes == 0 or self.qtde_contas == 0:
            print("Nenhuma cliente ou conta cadastrado para sacar")
        else:
            
            conta_encontrada = False
            numero = int(input("Digite o numero da conta: "))
            for conta in self._contasC:
                if conta.numero == numero:
                    conta_encontrada = conta            
  
            for conta in self._contasP:
                if conta.numero == numero:
                    conta_encontrada = conta

            if conta_encontrada:
                print(conta_encontrada.historico)
                print("Saldo atual: ",conta_encontrada.saldo)

            else:
                print("Numero digitado esta incorreto")

    def info(self):
        print("\nInformções do Banco")
        print("\nNumero de contas: ",self.qtde_contas)
        print("\nNome dos clientes")
        for cliente in self.clientes:
            print("Nome: ",cliente.nome," | Quantidade de contas:",cliente.qtde_contas," | Quantidade de seguros:",cliente.qtde_seguro)
              
                
    def menu(self):

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
            print(" 0 - Sair")
            opc = int(input("Selecione uma opção: "))

            if opc == 1:
                self.cadastro_cliente()

            elif opc == 2:
                self.criarContaC()
                
            elif opc == 3:
                self.criarContaP()

            elif opc == 4:
                criarSeguro()

            elif opc == 5:
                tributacao()
                
            elif opc == 6:
                sacar()

            elif opc == 7:
                depositar()

            elif opc == 8:
                tranferir()
                
            elif opc == 9:
                print_historico()

            elif opc == 10:
                info()
           
banco = Banco()
banco.menu()
