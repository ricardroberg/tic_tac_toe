"""
Minha primeira tentativa de criar jogoda velha, para duas pessoas.
"""
# Monta tabuleiro e numera as posições para facilitar a jogada e resultados


def monta_tabuleiro():
    tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    jogador1 = []
    jogador2 = []
    return tabuleiro, jogador1, jogador2


# Resultados que fecham a trinca levando a vitória
vence = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# 1     0,0 0,1 0,2
# 2                 
# 3                             2,0 2,1 2,2           
# 4                                        0,0 1,0 2,0 mesmos valores de #1 mas invertidos (x,y) para (y,x)                                                            
# 5                                                                          
# 6                                                              0,2 1,2 2,2 mesmos valores de #2 mas invertidos
# 7                                                                         0,0 1,1 2,2 x = y
# 8                                                                                     0,2 1,1 2,0

# Descompacta as variáveis
tabuleiro, jogador1, jogador2 = monta_tabuleiro()
posicoes = [x for x in range(1, 10)]

# Jogador 1 sempre começa
jogador = 'X'

# Imprime o tabuleiro a primeira vez
for i in tabuleiro:
    print(i)

while True:
    jogada = int(input(f'Qual posição quer jogar? {posicoes}\n'
                       f'(0) para reiniciar:'))

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
    else:
        print('Posição já foi ocupada. Escolha outra!')
    # REIMPRIME O TABULEIRO
    print()
    for i in tabuleiro:
        print(i)
    # SE NÃO HOUVER MAIS JOGADAS, TERMINA!
    if len(posicoes) == 0:
        break

    if jogador1 in vence:
        print('JOGADOR 1 VENCEU!')
        break
    elif jogador2 in vence:
        print('JOGADOR 2 VENCEU!')
        break

