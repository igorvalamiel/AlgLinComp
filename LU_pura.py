from estruturas import Matriz

def cria_matriz(n, M):
    return Matriz(n, n, M)

def cria_vetor(n, M):
    return Matriz(n, 1, M)

def LU_pura(n, M, V):
    matr = cria_matriz(n, M)
    vec = cria_vetor(n, V)

    print(matr, '\n')

    # derivando matriz em LU (usando algoritmo do slide do prof)
    # não é necessário criar mais de uma matriz, já que L e U ocupam espaços diferentes

    for i in range(n-1):
        # montando a parte L da matriz
        for j in range(i+1, n):
            matr.mat[j][i] = matr.mat[j][i]/matr.mat[i][i]
        
        # montando a parte U da matriz
        for k in range(i+1, n):
            for x in range(i+1, n):
                matr.mat[x][k] -= matr.mat[x][i] * matr.mat[i][k]
    
    print(matr) 
        