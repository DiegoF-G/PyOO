# De modo a deixar a sintaxe mais interessante, podemos usar os decoradores @property e @atributo.setter para realizar
# as mesmas funcionalidades dos getters e setters.
# Usarei @property para deixar disponível para validação os atributos titular e saldo e @atributo.setter para mudar o
# atributo limite, que no contexto da classe é plausível.
# Importante salientar que os decoradores @property e @atributo.setter não violam a privacidade dos atributos! Apenas
# permitem um acesso controlado e não direto aos mesmos, servem como uma camada intermediária!
class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, destino, valor):
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


conta_diego = ContaCorrente(1234, 'Diego', 7000, 3000)
testes = (print(conta_diego.titular), print(f'Saldo: {conta_diego.saldo}'), print(f'Limite: {conta_diego.limite}'))
conta_diego.limite = 6000
print(f'Novo limite: {conta_diego.limite}')
