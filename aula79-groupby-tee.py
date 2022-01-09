from itertools import groupby, tee

alunos = [
    {'nome': 'Ane', 'nota': 'A'},
    {'nome': 'Caroline', 'nota': 'B'},
    {'nome': 'Jefferson', 'nota': 'A'},
    {'nome': 'Vinícius', 'nota': 'C'},
    {'nome': 'Valéria', 'nota': 'D'},
    {'nome': 'Vanessa', 'nota': 'B'},
    {'nome': 'Pedro', 'nota': 'C'},
    {'nome': 'Miguel', 'nota': 'A'},
    {'nome': 'Lucas', 'nota': 'D'},
    {'nome': 'Kobe', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
