from estruturas import Matriz

def cria_matriz(n, M):
    return Matriz(n, n, M)

def cria_vetor(n, M):
    return Matriz(n, 1, M)

def back_solving(n, M, V):
    x = [0]*n
    m = M.mat[:]
    v = V.mat[:]
    for j in range(n-1, -1, -1):
        x[j] = (v[j][0])/(m[j][j])
        for i in range(j):
            m[i][j] *= x[j]
            v[i][0] -= m[i][j]
    return x

def front_solving(n, M, V): # nome merda mas é a vida
    y = Matriz(n, 1, [0]*n)
    m = M.mat[:]
    v = V.mat[:]
    for j in range(n):
        y.mat[j][0] = v[j][0]
        for i in range(j+1, n):
            m[i][j] *= y.mat[j][0]
            v[i][0] -= m[i][j]
    return y

def LU_pura(n, M, V):
    matr = cria_matriz(n, M)
    vec = cria_vetor(n, V)

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
    
    print(matr, '\n')
    L_solved = front_solving(n, matr, vec)
    print(L_solved)
    solution = back_solving(n, matr, L_solved)
    print(solution)
        