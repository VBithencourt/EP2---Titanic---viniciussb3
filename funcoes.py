def define_posicoes(linha,coluna,orientação,tamanho):
    L = linha
    C = coluna
    O = orientação

    data = []
    if O == "vertical":
        for i in range(tamanho):
            data.append([L + i, C])
    elif O == "horizontal":
        for i in range(tamanho):
            data.append([L, C + i])
    return data

def preenche_frota(frota,nome_navio, linha, coluna, orientação, tamanho):
    lista = define_posicoes(linha, coluna, orientação, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(lista)
    else:
        frota[nome_navio] = [lista]
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    jogada = tabuleiro
    return jogada

def posiciona_frota(frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ] 
    for navios in frota:
        for loc_navio in frota[navios]:
            for linha, coluna in loc_navio:
                tabuleiro[linha][coluna] = 1
    return tabuleiro


def afundados(frota, tabuleiro):
    navios_afundados = 0
    for local in frota.values():
        for navio in local:
            afundado = True
            for local in navio:
                if tabuleiro[local[0]][local[1]] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1
    return navios_afundados