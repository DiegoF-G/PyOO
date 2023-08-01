"""Além da classe, possuir atributos que não são de instâncias, ela também pode ter métodos independentes de instâncias
   que utilizam atributos da própria classe. No lugar do "self", usa-se "cls" como argumento fixo para passar a
   referência da classe na memória em vez de ser do objeto. Usa-se também o decorador "@clasmethod" para definir esse
   método."""


class Circulo:
    pi = '3.1415'

    @classmethod
    def pi_aproximado(cls):
        return f'O valor de pi até a quarta casa decimal é {cls.pi}'


print(Circulo.pi_aproximado())
