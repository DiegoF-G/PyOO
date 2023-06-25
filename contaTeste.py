# Funções criadas para simular uma dinâmica de uma conta bancária, ou tentar simular uma classe "conta-corrente".
# Porém, a váriavel "conta" atribuída no escopo da função "criar_conta_bancaria" pode ser modificada sem a chamada
# das outras funções (deposita, sacar e extrato) alterando os seus itens existentes ou adicionando novos.
# Assim, essa "falha" no paradigma procedural motiva a POO.

def criar_conta_corrente(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print(f'Saldo {conta["saldo"]}')
