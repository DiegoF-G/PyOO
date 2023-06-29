# Apesar de os atributos da classe "ContaCorrente" serem privados, eles podem ser acessados por métodos especiais...
# Esses métodos, os getters e setters, só devem ser utilizados para validar e modificar atributos que realmente
# necessitam disso, como no exemplo de uma conta, o limite pode mudar e é útil saber apenas do saldo, porém o titular
# dificilmente muda assim como o número de sua conta
class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def get_saldo(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    # Getter criado somente para verificação do setter set_limite!!!
    def get_limite(self):
        return self.__limite


conta_diego = ContaCorrente(1234, 'Diego', 7000, 2000)
conta_diego.set_limite(10000)
testes = (print(f'Novo limite: {conta_diego.get_limite()}'), print(f'Saldo: {conta_diego.get_saldo()}'))
