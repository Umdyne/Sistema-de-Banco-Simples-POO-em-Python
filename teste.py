def cadastro_cliente():
    nome = input("Digite o nome do Cliente: ")
    cpf = "0"
    while type(cpf) != int or cpf < 9999999999 or cpf > 99999999999:
        try:
            cpf = int(input("Digite os numeros CPF: "))
        except:
            print("CPF invalido.") 

cadastro_cliente()
