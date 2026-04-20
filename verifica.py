def verifica(n, matr, vec, xList):
    for h in range(n):
        linha = matr.mat[h]
        s = 0
        for i in range(n):
            s += linha[i]*xList[i]
        if s != vec.mat[h][0]: return f"O resultado está errado. Erro encontrado na linha {h} ~> ({s} != {vec.mat[h][0]})."
    return "O resultado está correto!"
