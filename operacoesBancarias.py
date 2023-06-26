# Classe "ContaCorrente" criada com atributos e também funções agora, conhecidas como métodos!
class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta1234 = ContaCorrente(1234, 'Diego', 10000, 2500)
testes = (print('Extrato inicial...'), conta1234.extrato(), print('Depositando 1000...'), conta1234.depositar(1000),
          conta1234.extrato(), print('Sacando 1500...'), conta1234.sacar(1500), conta1234.extrato())
