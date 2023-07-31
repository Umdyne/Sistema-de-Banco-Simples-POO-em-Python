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





banco.qtde_contas += 1
conta_poupanca = Conta_Poupanca(cpf, banco.qtde_contas)
banco.clientes[0].contaP = conta_poupanca
banco._contasP.append(conta_poupanca)

banco.qtde_contas += 1
conta_poupanca = Conta_Poupanca(cpf, banco.qtde_contas)
banco.clientes[1].contaP = conta_poupanca
banco._contasP.append(conta_poupanca)
