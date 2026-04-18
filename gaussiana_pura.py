from estruturas import Matriz

def cria_matriz(n, M):
    return Matriz(n, n, M)

def cria_vetor(n, M):
    return Matriz(n, 1, M)

def back_solving(n, M, V):
    x = [0]*n
    m = M.mat.copy()
    v = V.mat.copy()
    for j in range(n-1, -1, -1):
      x[j] = (m[j][j])/(v[j][0])
      for i in range(j):
          m[j][i] *= x[j]
          v[j][0] += m[j][i]

    return x

def gaussiana_pura(n, M, V):
    matr = cria_matriz(n, M)
    vec = cria_vetor(n, V)

    for i in range(0, n-1):
        new_mat = Matriz(n, n, identity=True)
        for j in range(i, n):
            v = matr.mat[i][i]
            new_mat.mat[j][i] = float((-1*(matr.mat[j][i]))/v)
        matr = new_mat * matr
        vec = new_mat * vec

    print(f"Soluções: {back_solving(n, matr, vec)}")
