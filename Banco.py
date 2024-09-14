import datetime as dt
from abc import ABC, abstractclassmethod

# Variáveis globais
numero_agencia = "0005"
lista_de_cpfs_cadastrados = []
usuarios = []
contas = []

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = numero_agencia
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente):
        numero_da_conta = len(contas) + 1
        conta = cls(numero_da_conta, cliente)
        contas.append(conta)
        return conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente!")
            return False
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Valor inválido!")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Valor inválido!")
            return False

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

class Transacao(ABC):
    @property
    @abstractclassmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(self)

# Funções de interação (mantidas)
def cadastro_usuario():
    nome = input("Digite o nome do usuário:\n")
    cpf = input("Digite o CPF do usuário (11 dígitos):\n")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA):\n")
    endereco = input("Digite o endereço do usuário:\n")

    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Deve conter 11 dígitos numéricos.")
        return

    if cpf in lista_de_cpfs_cadastrados:
        print("Usuário já cadastrado.")
        return

    cliente = Cliente(nome, cpf, data_nascimento, endereco)
    usuarios.append(cliente)
    lista_de_cpfs_cadastrados.append(cpf)
    print("Usuário cadastrado com sucesso!")

def cadastro_conta():
    cpf = input("Digite o CPF do usuário:\n")

    cliente = next((usuario for usuario in usuarios if usuario.cpf == cpf), None)

    if not cliente:
        print("Usuário não existe!")
    else:
        conta = Conta.nova_conta(cliente)
        cliente.adicionar_conta(conta)
        print(f"Conta número {conta.numero} cadastrada com sucesso!")

def listar_usuarios():
    print("\nUsuários cadastrados:")
    if usuarios:
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}, CPF: {usuario.cpf}, Data de Nascimento: {usuario.data_nascimento}, Endereço: {usuario.endereco}")
    else:
        print("Nenhum usuário cadastrado.")

def listar_contas():
    print("\nContas cadastradas:")
    if contas:
        for conta in contas:
            print(f"Número da Conta: {conta.numero}, CPF: {conta.cliente.cpf}, Saldo: R$ {conta.saldo:.2f}")
    else:
        print("Nenhuma conta cadastrada.")

def menu():
    print("Banco".center(17, "-"))
    print("Selecione uma opção\n")
    print("[1] - Depósito\n[2] - Saque\n[3] - Extrato\n[4] - Cadastrar usuário\n[5] - Cadastrar conta\n[6] - Listar usuários\n[7] - Listar contas\n[8] - Sair\n")

menu()
escolha_do_cliente = int(input())

while escolha_do_cliente != 8:
    if escolha_do_cliente > 7 or escolha_do_cliente < 1:
        print("Escolha Inválida\n")
    elif escolha_do_cliente == 1:
        cpf = input("Digite o CPF do cliente:\n")
        valor_deposito = float(input("Digite o valor do depósito:\n"))
        cliente = next((usuario for usuario in usuarios if usuario.cpf == cpf), None)
        if cliente and cliente.contas:
            deposito = Deposito(valor_deposito)
            deposito.registrar(cliente.contas[0])
        else:
            print("Cliente ou conta não encontrados!")
    elif escolha_do_cliente == 2:
        cpf = input("Digite o CPF do cliente:\n")
        valor_saque = float(input("Digite o valor do saque:\n"))
        cliente = next((usuario for usuario in usuarios if usuario.cpf == cpf), None)
        if cliente and cliente.contas:
            saque = Saque(valor_saque)
            saque.registrar(cliente.contas[0])
        else:
            print("Cliente ou conta não encontrados!")
    elif escolha_do_cliente == 3:
        cpf = input("Digite o CPF do cliente:\n")
        cliente = next((usuario for usuario in usuarios if usuario.cpf == cpf), None)
        if cliente and cliente.contas:
            print("\nExtrato".center(15, "-"))
            for transacao in cliente.contas[0].historico.transacoes:
                print(transacao)
            print(f"\nSaldo atual: R$ {cliente.contas[0].saldo:.2f}\n")
        else:
            print("Cliente ou conta não encontrados!")
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
