"""
dicionário:
Um vetor associativo em que chaves arbitrárias
são mapeadas para valores. As chaves podem ser
quaisquer objetos que possuam os métodos __hash__() e __eq__().
Dicionários são estruturas chamadas de hash na linguagem Perl.
"""

# d1 = {'chave': 'valor', 'chave': 'valor', 'chave': 'valor final'}  # mesma nome de chave exibe apenas o valor final.
# d1 = {1: 'valor', 2: 'valor', 3: 'valor final'}  # mesma nome de chave exibe apenas o valor final.
# d1['nova chave'] = 'valor1'
# print(d1)
# print(d1[3])

# d1 = {
#     'str': 'valor',
#     123: 'outro valor',
#     (1,2,3,4): 'tupla'
# }

# d1.update({'Nova chave': 'novo valor'})
# if d1.get('Nova chave') is not None:
#     print(d1.get('Nova chave'))

# print('str' in d1)
# print('str' in d1.keys())
# print('valor' in d1.values())
# print(len(d1))

# for k in d1:  # iterando sobre as keys.
#     print(k)
# print()  # apenas para espaçar entre keys e values.
# for v in d1.values():  # iterando sobre os values.
#     print(v)
# print()
# for k, v in d1.items():
#     print(k, v)

clientes = {
        'cliente1': {
             'nome': 'Ane',
             'sobrenome': 'Caroline'
        },
        'cliente2': {
                'nome': 'Jefferson',
                'sobrenome': 'Vinícius'
        }
}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')