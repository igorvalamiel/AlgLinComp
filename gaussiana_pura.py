from estruturas import Matriz

def cria_matriz(n, M):
    return Matriz(n, n, M)

def cria_vetor(n, M):
    return Matriz(n, 1, M)

def gaussiana_pura(n, M, V):
    mat = cria_matriz(n, M)
    vec = cria_vetor(n, V)

