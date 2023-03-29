import time

class Conta:
    def __init__(self, id_conta, saldo):
        self.id_conta = id_conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    
    def verificar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")
    
class ContaCorrente(Conta):
    def __init__(self, id_conta, saldo, limite=100000):
        super().__init__(id_conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Limite de saque excedido.")
    
class ContaPoupanca(Conta):
    def __init__(self, id_conta, saldo, taxa_de_rendimento=0.1):
        super().__init__(id_conta, saldo)
        self.taxa_de_rendimento = taxa_de_rendimento
    
    def verificar_rendimento_ao_ano(self):
        print(f"Rendimento ao ano: R$ {self.saldo * self.taxa_de_rendimento:.2f}")
    
    def verificar_rendimento_por_periodo(self, periodo):
        if periodo == 'segundos':
            segundos_no_ano = 365 * 24 * 60 * 60
            rendimento = self.saldo * self.taxa_de_rendimento / segundos_no_ano
        elif periodo == 'minutos':
            minutos_no_ano = 365 * 24 * 60
            rendimento = self.saldo * self.taxa_de_rendimento / minutos_no_ano
        elif periodo == 'horas':
            horas_no_ano = 365 * 24
            rendimento = self.saldo * self.taxa_de_rendimento / horas_no_ano
        elif periodo == 'dias':
            rendimento = self.saldo * self.taxa_de_rendimento / 365
        elif periodo == 'semanas':
            rendimento = self.saldo * self.taxa_de_rendimento / 52
        elif periodo == 'meses':
            rendimento = self.saldo * self.taxa_de_rendimento / 12
        elif periodo == 'anos':
            rendimento = self.saldo * self.taxa_de_rendimento
        else:
            print("Período inválido.")
            return
        
        print(f"Rendimento por {periodo}: R$ {rendimento:.2f}")
        
def criar_conta():
    id_conta = input("Digite o ID da conta: ")
    saldo = float(input("Digite o saldo inicial da conta: "))
    tipo_conta = input("Digite o tipo de conta (corrente/poupanca): ")
    
    if tipo_conta == "corrente":
        conta = ContaCorrente(id_conta, saldo)
    elif tipo_conta == "poupanca":
        conta = ContaPoupanca(id_conta, saldo)
    else:
        print("Tipo de conta inválido.")
        return

    print("Conta criada com sucesso!")
    return conta


def menu():
    print("\n---------- MENU ----------")
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Verificar saldo")
    print("5 - Verificar rendimento")
    print("0 - Sair")
    opcao = input("Digite uma opção: ")
    return opcao
contas = []

while True:
    
    opcao = menu()


    if opcao == '1':
        conta = criar_conta()
        if conta:
            contas.append(conta)
        
    elif opcao == '2':
        id_conta = input("Digite o ID da conta: ")
        valor = float(input("Digite o valor a depositar: "))
    
        for conta in contas:
            if conta.id_conta == id_conta:
                conta.depositar(valor)
                break
        else:
            print("Conta não encontrada.")
        
        
    elif opcao == '3':
        id_conta = input("Digite o ID da conta: ")
        valor = float(input("Digite o valor a sacar: "))
    
        for conta in contas:
            if conta.id_conta == id_conta:
                conta.sacar(valor)
                break
        else:
            print("Conta não encontrada.")

    elif opcao == '4':
        id_conta = input("Digite o ID da conta: ")
    
        for conta in contas:
            if conta.id_conta == id_conta:
                conta.verificar_saldo()
                break
        else:
            print("Conta não encontrada.")

    elif opcao == '5':
        id_conta = input("Digite o ID da conta: ")
    
        for conta in contas:
            if conta.id_conta == id_conta and isinstance(conta, ContaPoupanca):
                periodo = input("Digite o período (segundos/minutos/horas/dias/semanas/meses/anos): ")
                conta.verificar_rendimento_por_periodo(periodo)
                break
        else:
            print("Conta poupança não encontrada.")

    elif opcao == '0':
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")



