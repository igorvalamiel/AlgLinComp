from estruturas import Matriz

def cria_matriz(n, M):
    return Matriz(n, n, M)

def cria_vetor(n, M):
    return Matriz(n, 1, M)

def gaussiana_pura(n, M, V):
    mat = cria_matriz(n, M)
    vec = cria_vetor(n, V)

    for i in range(0, n-1):
        new_mat = Matriz(n, n, identity=True)
        for j in range(i, n):
            v = mat.mat[i][i]
            new_mat.mat[j][i] = float((-1*(mat.mat[j][i]))/v)
        mat = new_mat * mat
        vec = new_mat * vec
        print(mat, vec)
        print('~~~~')
