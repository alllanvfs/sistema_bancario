valor_saque = 0
valor_extrato = 0

def deposito():
    global valor_extrato

    print("\n")
    print("Deposito".center(16,"-"))
    valor_extrato += float(input("Digite o valor do deposito:\n"))
    print("Deposito realizado com sucesso!\n")

def extrato():
    global valor_extrato

    print("\n")
    print("Extrato".center(15,"-"))
    print(f"O valor do extrato:{valor_extrato}\n")

def saque():
    global valor_extrato
    global valor_saque

    print("\n")
    print("Saque".center(11,"-"))
    valor_saque = float(input("Digite o valor do saque:\n"))
    if(valor_saque <= valor_extrato):
        valor_extrato -= valor_saque
        print("Saque realizado com sucesson\n")
    else:
        print("saldo insuficiente\n")


print("Santander".center(17,"-"))
print("Selecione uma opcao\n")
print("1-Deposito\n2-Saque\n3-Extrato\n4-Sair\n")
escolha_do_cliente = int(input())

while(escolha_do_cliente != 4):
        
    if(escolha_do_cliente > 4 or escolha_do_cliente < 1):
        print("Escolha Invalida\n")
    elif(escolha_do_cliente == 1):
        deposito()
    elif(escolha_do_cliente == 2):
        saque()
    elif(escolha_do_cliente == 3):
        extrato()

    print("Santander".center(17,"-"))
    print("Selecione uma opcao\n")
    print("1-Deposito\n2-Saque\n3-Extrato\n4-Sair\n")
    escolha_do_cliente = int(input())


