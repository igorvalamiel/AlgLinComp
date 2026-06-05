def is_different(x, y):
    dif = x-y
    if dif < 0: dif *= -1
    if dif < 0.001: return False
    return True


def verifica(n, matr, vec, xList):
    for h in range(n):
        linha = matr.mat[h]
        s = 0
        for i in range(n):
            s += linha[i]*xList[i]
        if is_different(s, vec.mat[h][0]): return f"O resultado está errado. Erro encontrado na linha {h} ~> ({s} != {vec.mat[h][0]})."
    return "O resultado está correto!"
