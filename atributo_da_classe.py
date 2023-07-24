class Circulo:
    pi = 3.18  # atributo da classe, que não é incorporado nas instâncias


circulo1 = Circulo()  # instânciando a classe "Circulo", criando o objeto "circulo1"

print(circulo1.pi)  # aqui o py procurou o atributo na instância e não achou, então foi buscar esse atributo na classe

circulo1.pi = 3.14  # aqui definimos o atributo da instância, como uma atribuição normal, porém o da classe muda? ...

print(circulo1.pi)  # exibindo o atributo da instância

print(Circulo.pi)  # exibindo o atributo da classe

Circulo.pi = 3.14  # para mudar o atributo da classe devemos chamar pela classe e não instância

print(Circulo.pi)  # e aqui temos o novo valor do atributo "pi" na classe "Circulo"
