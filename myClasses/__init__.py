class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def data_formatada(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


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
