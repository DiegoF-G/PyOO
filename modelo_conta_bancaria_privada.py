# Até agora a classe "ContaCorrente" possuía os seus atributos acessíveis e modificaveis... agora são privados e assim
# não são acessíveis e suscetíveis a mudança sem ser por métodos. Também temos o novo método "transferir" para
# encapsular o uso dos métodos "depositar" e "sacar" para transferir saldo, note que com ele a classe continua coesa.
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


# Testando...
conta1, conta2 = ContaCorrente(123, 'Diego', 10000), ContaCorrente(321, 'Diogo', 5000)
testes = (conta1.extrato(), conta2.extrato(), print('Transferindo 1000 do Diego para o Diogo'),
          conta1.transferir(conta2, 1000), conta1.extrato(), conta2.extrato(),
          print('Note que os metodos estão públicos e os atributos não:'), print(dir(ContaCorrente)))
raise AttributeError('Ops! Esse atributo é privado.')
conta1.saldo -= 1000
