import datetime as dt

valor_extrato = 0
movimentacoes = []
numero_de_transacoes = 0
data_atual = dt.datetime.now().date()

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

print("Santander".center(17, "-"))
print("Selecione uma opcao\n")
print("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n")
escolha_do_cliente = int(input())

while escolha_do_cliente != 4:
        
    if escolha_do_cliente > 4 or escolha_do_cliente < 1:
        print("Escolha Invalida\n")
    elif escolha_do_cliente == 1:
        deposito()
    elif escolha_do_cliente == 2:
        saque()
    elif escolha_do_cliente == 3:
        extrato()

    print("Santander".center(17, "-"))
    print("Selecione uma opcao\n")
    print("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n")
    escolha_do_cliente = int(input())
