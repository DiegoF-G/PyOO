class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def data_formatada(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


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


class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1