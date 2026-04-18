from estruturas import Matriz
def cria_matriz(n, M):
    return Matriz(n, n, M)

def cria_vetor(n, M):
    return Matriz(n, 1, M)

def back_solving(n, M, V):
    x = [0]*n
    m = M.mat[:]
    v = V.mat[:]
    print(m, v, '\n')
    for j in range(n-1, -1, -1):
      x[j] = (v[j][0])/(m[j][j])
      print(x[j])
      for i in range(j):
          m[i][j] *= x[j]
          v[i][0] -= m[i][j]
      print(m, v)

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
    