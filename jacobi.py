from estruturas import Matriz

def jacobizinho(n, m, v, x0, iter):
    xi = [0 for _ in range(n)]

    for i in range(n):
        bi = v[i][0]
        ai = m[i][i]
        soma = 0
        for j in range(n):
            if i != j : soma += (m[i][j] * x0[i])
        xi[i] = (bi-soma)/ai
    
    vec_x0 = Matriz(n, 1, x0)
    vec_xi = Matriz(n, 1, xi)
    subt_vec = vec_xi - vec_x0
    R = subt_vec.module() / vec_xi.module()

    return [iter+1, x0, xi, R]

def jacobi(N, M, V):

    # contando as iterações
    iterations = 0
    
    # Vetor inicial
    x0 = [1]*N
    
    res = jacobizinho(N, M, V, x0, iterations)
    
    print(res)
