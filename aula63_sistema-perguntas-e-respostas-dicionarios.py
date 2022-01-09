perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '7'},
        'resposta_certa': 'b'
    },
    'Pergunta2': {
        'pergunta': 'Quanto é 8 * 4?',
        'respostas': {'a': '34', 'b': '31', 'c': '32'},
        'resposta_certa': 'c'
    },
}
print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHHH !!!!!!!!! Você acertou !!!!!!!!!!')
        respostas_certas += 1  # incrementar no valor das respostas certas.
    else:
        print('IXIIII !!! Você ERROU !')

    print()

qtd_perguntas = len(perguntas)
porcentagem_certo = (respostas_certas / qtd_perguntas) * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_certo} %.')