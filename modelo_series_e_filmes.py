from minhas_classes import Serie, Filme
# Testando...
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
atlanta.nome = 'atlanta, de Grover'
for i in range(100):
    vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - {vingadores.duracao} min - {vingadores.likes} likes')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - {atlanta.temporadas} Temporadas - {atlanta.likes} likes')
