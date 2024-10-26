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