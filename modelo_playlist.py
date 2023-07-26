"""Para finalizar a classe "Playlist", em vez de usar os propertys "listagem" e "tamanho" ou herdar da classe built in
   "list", sendo uma classe "maior" e mais complexa que o necessário, realizei Duck Typing através dos dunder methods
   "__getitem__" e "__len__", que garatem apenas alguns comportamentos de list (apenas os necessários). Outra possível
   solução seria importar alguma classe abstrata base (ABC)..."""


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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


# Testando...
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

lista = [atlanta, vingadores, demolidor, tmep]

minha_playlist = Playlist('fim de semana', lista)

for programa in minha_playlist:
    print(programa)
print(f'Tamanho: {len(minha_playlist)}')
