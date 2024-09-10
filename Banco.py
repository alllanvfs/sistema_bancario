import datetime as dt

numero_agencia = "0005"
valor_extrato = 0
movimentacoes = []
numero_de_transacoes = 0
data_atual = dt.datetime.now().date()
lista_de_cpfs_cadastrados = []
usuarios = []
contas = []

def verificar_limite_transacoes():
    global numero_de_transacoes, data_atual

    hoje = dt.datetime.now().date()
    if hoje != data_atual:
        data_atual = hoje
        numero_de_transacoes = 0
    return numero_de_transacoes < 10

def registrar_transacao(tipo, valor):
    global numero_de_transacoes

    if verificar_limite_transacoes():
        data_hora_atual = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        movimentacoes.append(f"{tipo}: R$: {valor:.2f} - {data_hora_atual}")
        numero_de_transacoes += 1 
        return True
    else:
        print("!Limite de transações diárias atingido!\n")
        return False

def deposito():
    global valor_extrato

    print("\n")
    print("Deposito".center(16, "-"))
    valor_deposito = float(input("Digite o valor do deposito:\n"))
    if registrar_transacao("Deposito", valor_deposito):
        valor_extrato += valor_deposito
        print("Deposito realizado com sucesso!\n")

def extrato():
    global valor_extrato

    print("\n")
    print("Extrato".center(15, "-"))
    if movimentacoes:
        for mov in movimentacoes:
            print(mov)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {valor_extrato:.2f}\n")

def saque():
    global valor_extrato

    print("\n")
    print("Saque".center(11, "-"))
    valor_saque = float(input("Digite o valor do saque:\n"))
    if valor_saque <= valor_extrato:
        if registrar_transacao("Saque", valor_saque):
            valor_extrato -= valor_saque
            print("Saque realizado com sucesso\n")
    else:
        print("Saldo insuficiente\n")

def verifica_cpf(cpf):
    return cpf not in lista_de_cpfs_cadastrados

def cadastro_usuario():
    cpf = input("Digite o seu CPF (somente números):\n")
    
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Deve conter 11 dígitos numéricos.\n")
        return
    
    if verifica_cpf(cpf):
        nome = input("Digite seu nome:\n")
        data_de_nascimento = input("Digite a data do seu nascimento:\n")
        endereco = input("Digite o seu endereco (logradouro, nro - bairro - cidade/estado)\n")

        lista_de_cpfs_cadastrados.append(cpf)
        usuarios.append({"nome": nome, "CPF": cpf, "data de nascimento": data_de_nascimento, "endereco": endereco})

        print("\n!Usuario cadastrado com sucesso!\n")
    else:
        print("\nEsse CPF já está cadastrado!\n")

def cadastro_conta():
    global numero_agencia
    cpf = input("Digite o CPF do usuario:\n")
    
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Deve conter 11 dígitos numéricos.\n")
        return

    if verifica_cpf(cpf):
        print("Usuário não existe!\n")
    else:
        numero_da_conta = len(contas) + 1
        contas.append({"agencia": numero_agencia, "numero_da_conta": numero_da_conta, "CPF": cpf, "saldo": 0.0})
        print(f"Conta número {numero_da_conta} cadastrada com sucesso!\n")

def listar_usuarios():
    print("\nUsuários cadastrados:")
    if usuarios:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['CPF']}, Data de Nascimento: {usuario['data de nascimento']}, Endereço: {usuario['endereco']}")
    else:
        print("Nenhum usuário cadastrado.\n")

def listar_contas():
    print("\nContas cadastradas:")
    if contas:
        for conta in contas:
            print(f"Número da Conta: {conta['numero_da_conta']}, CPF: {conta['CPF']}, Saldo: R$ {conta['saldo']:.2f}")
    else:
        print("Nenhuma conta cadastrada.\n")

def menu():
    print("Santander".center(17, "-"))
    print("Selecione uma opcao\n")
    print("[1] - Deposito\n[2] - Saque\n[3] - Extrato\n[4] - Cadastrar usuario\n[5] - Cadastrar conta\n[6] - Listar usuarios\n[7] - Listar contas\n[8] - Sair\n")

menu()
escolha_do_cliente = int(input())

while escolha_do_cliente != 8:
    if escolha_do_cliente > 7 or escolha_do_cliente < 1:
        print("Escolha Inválida\n")
    elif escolha_do_cliente == 1:
        deposito()
    elif escolha_do_cliente == 2:
        saque()
    elif escolha_do_cliente == 3:
        extrato()
    elif escolha_do_cliente == 4:
        cadastro_usuario()
    elif escolha_do_cliente == 5:
        cadastro_conta()
    elif escolha_do_cliente == 6:
        listar_usuarios()
    elif escolha_do_cliente == 7:
        listar_contas()

    menu()
    escolha_do_cliente = int(input())
