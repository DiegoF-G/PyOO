# Nesse arquivo há a utilização do polimorfismo das subclasses "Filme" e "Serie" para inseri-las numa única lista.
# Assim é possível iterar ela sem se preocupar com os tipos dos objetos, visto que todos pertencem a mesma superclasse.
# Há também a utilização dos métodos especiais __str__ e __repr__ para representar os objetos como strings ou verificá-los.
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def __str__(self):
        return f'Nome: {self._nome} Likes: {self._likes}'

    def __repr__(self):
        return f'Programa(nome={self._nome}, ano={self.ano})'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

    def __repr__(self):
        return f'Filme(nome={self._nome}, ano={self.ano}, duração={self.duracao})'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

    def __repr__(self):
        return f'Serie(nome={self._nome}, ano={self.ano}, temporadas={self.temporadas})'


vingadores, atlanta = Filme('vingadores - guerra infinita', 2018, 160), Serie('atlanta', 2018, 2)
lista = [atlanta, vingadores]
for i in range(1000):
    vingadores.dar_likes()
for i in range(600):
    atlanta.dar_likes()
for programa in lista:
    prog = (print(programa), print(repr(programa)))
