from estruturas import Matriz

def cria_matriz(n, M):
    return Matriz(n, n, M)

def cria_vetor(n, M):
    return Matriz(n, 1, M)

def diagonalize(n, M):
    for i in range(n):
        for j in range(i):
            print(M.mat[i][j], end=', ')
        print()

def gaussiana_pura(n, M, V):
    mat = cria_matriz(n, M)
    vec = cria_vetor(n, V)

    print(mat, '\n')
    diagonalize(n, mat)
    print(mat)