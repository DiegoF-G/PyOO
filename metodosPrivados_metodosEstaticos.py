class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor=0):
        self.__saldo += valor

    def __pode_sacar(self, saque):
        saque_maximo = self.__saldo + self.__limite
        return saque <= saque_maximo

    def sacar(self, valor=0):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('\033[0:31mO saque solicitado não é possível, pois limite foi ultrapassado.\033[m')

    def transferir(self, destino, valor=0):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        codigos = "{'BB': '001', 'Caixa': '104', 'Bradesco': '237'}".replace("'", "").replace("{", "").replace("}", "")
        return codigos


# Teste
conta_diego = ContaCorrente(1134, 'Diego', 5000)
conta_diego.sacar(6000)
print(conta_diego.saldo)
conta_diego.sacar(1)
print(ContaCorrente.codigos_bancos())
