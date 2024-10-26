def define_posicoes(Linha,Coluna,Orientação,tamanho):
    L = Linha
    C = Coluna
    O = Orientação
    T = tamanho

    data = []
    if O == "vertical":
        for i in range(tamanho):
            data.append([L + i, C])
    elif O == "horizontal":
        for i in range(tamanho):
            data.append([L, C + i])
    return data
