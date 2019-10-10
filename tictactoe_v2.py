"""
Minha primeira tentativa de criar jogo da velha, para duas pessoas.
"""
# Monta tabuleiro e numera as posições para facilitar a jogada e resultados


def monta_tabuleiro():
    tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    jogador1 = []
    jogador2 = []
    return tabuleiro, jogador1, jogador2


# Resultados que fecham a trinca levando a vitória
vence = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
         [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

tabuleiro, jogador1, jogador2 = monta_tabuleiro()
posicoes = [x for x in range(1, 10)]
jogador = 'X'
for i in tabuleiro:
    print(i)

while True:
    jogada = int(input(f'Qual posição quer jogar? {posicoes}\n (0) para reiniciar:'))
    if jogada in posicoes:
        for p in range(3):
            for i in range(3):
                if tabuleiro[p][i] == jogada:
                    tabuleiro[p][i] = jogador
                    if jogador == 'X':
                        jogador1.append(jogada)
                        jogador = 'O'
                    elif jogador == 'O':
                        jogador2.append(jogada)
                        jogador = 'X'
                    posicoes.remove(jogada)
    elif jogada == 0:
        tabuleiro, jogador1, jogador2 = monta_tabuleiro()
        posicoes = [x for x in range(1, 10)]
    elif jogada < 0 or jogada > 9:
        print(f'Número inválido! Utilize apenas as posições {posicoes}.')

    else:
        print('Posição já foi ocupada. Escolha outra!')
    print()
    for i in tabuleiro:
        print(i)
    # Verifica vitória
    for v in vence:
        if list(set(v).intersection(jogador1)) == v:
            print('JOGADOR 1 VENCEU!')
            break
        elif list(set(v).intersection(jogador2)) == v:
            print('JOGADOR 2 VENCEU!')
            break
    # Acabaram as jogadas
    if len(posicoes) == 0:
        break
