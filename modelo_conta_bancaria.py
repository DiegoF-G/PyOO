# Classe "ContaCorrente" criada para instanciar os objetos "conta", somente com atributos ainda...
class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


# Testando...
conta1, conta2 = ContaCorrente(1234, 'Nico', 1050.00), ContaCorrente(1235, 'Diego', 10000.50, 3000)
testes = (print(conta1.numero), print(conta1.titular), print(conta1.saldo), print(conta1.limite), print(),
          print(conta2.numero), print(conta2.titular), print(conta2.saldo), print(conta2.limite))
