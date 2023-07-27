""" Nem todas linguagens possuem suporte para herança de mais de uma superclasse (herança múltipla), porém o Python é chique e possuí :)
    Isso pode ajudar a deixar o código mais organizado, porém é preciso saber algumas particularidades, como o MRO (Method Resolution Order):
    algoritmo interno do Python que decide que método usar com mesmo nome entre classes mães e filhas relacionadas.
    Além disso, temos classes que não são instanciadas e somente servem para serem herdadas chamadas Mixins,
    que no caso seguinte é a classe "Hipster" que transmite um comportamento mais geral que o da classe mãe "Funcionario",
    assim mantendo a coesão das classes sem abrir mão desse comportamento alheio, mas desejado."""


# Classe vó
class Funcionario:
    def __init__(self, nome):
        self._nome = nome.title()
        self._horas = 0

    @property
    def nome(self):
        return self._nome

    @property
    def horas(self):
        return self._horas

    def registra_horas(self, horas_trabalhadas):
        self._horas += horas_trabalhadas
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


# Classes mães
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def buscar_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def buscar_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


# Classe Mixin
class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'


# Classes filhas
class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass


class Senior(Caelum, Alura, Hipster):
    pass


"""Trocando a ordem das heranças das classes filhas aqui, na hora de chamar o método comum "mostrar_tarefas" entre as classes mães "Alura" e "Caelum",
   o MRO irá pegar o metodo chamado encontrado primeiro da esquerda para direita (ordem dos argumentos da classe) 
   e também procurar na classe vó caso não encontre o método na respectiva classe mãe ("se não encontrar na mãe vai procurar na vó") 
   além de analisar nesse caso se a classe vó em questão é uma "Good Head" (esteja na mesma hierarquia das outras classes mães),
   caso não seja, irá procurar na proxima classe mãe na ordem mencionada (esquerda para direita). 
   Caso nenhuma classe mãe tenha o método chamado, é usado o da classe vó (se tiver o método nela é claro). 
   
   Resumindo as três etapas do MRO de prioridade na procura de métodos:
   1)Na ordem dos argumentos da passagem de herança.
   2)Se é uma "Good Head" a classe vó caso o método não seja encontrado na classe mãe para pegar o método dela, caso contrário, segue a ordem.
   3)Se nenhuma classe mãe tiver o método, usa-se o da classe vó.
   
   No caso das classes filhas em questão: Junior: Alura > Funcionario
                                          Pleno: Alura > (Funcionario if is Good Head) > Caelum > Funcionario 
                                          Senior: Caelum > (Funcionario if is Good Head) > Alura > Funcionario
"""
# Testando...
jose = Junior('Jose')
jose.buscar_perguntas_sem_resposta()
jose.mostrar_tarefas()
print()
luan = Pleno('luan')
luan.buscar_perguntas_sem_resposta()
luan.buscar_cursos_do_mes()
luan.mostrar_tarefas()
print(luan)
print()
nico = Senior('nico')
nico.registra_horas(10)
nico.mostrar_tarefas()
print(nico)
