from aula80 import produtos, pessoas, lista

# # nova_lista = map(lambda x: x * 2, lista)  # um jeito alternativo a list comprehension, mas list comprehension é a melhor opção.
# nova_lista = [x*2 for x in lista]
# print(lista)
# print(list(nova_lista))

# def aumento_preco(p):
#     p['valor'] = round(p['valor'] * 1.05, 2)
#     return p
# novos_produtos = map(aumento_preco, produtos)
# for produto in novos_produtos:
#     print(produto)


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade']*1.20)
    return p
nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)
