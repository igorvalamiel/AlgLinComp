from estruturas import Matriz

def jacobizinho(n, m, v, x0, iter, r_min, it_max):
    xi = [0 for _ in range(n)]

    for i in range(n):
        bi = v[i][0]
        ai = m[i][i]
        soma = 0
        for j in range(n):
            if i != j : soma += (m[i][j] * x0[j])
        xi[i] = (bi-soma)/ai
    
    vec_x0 = Matriz(n, 1, x0)
    vec_xi = Matriz(n, 1, xi)
    subt_vec = vec_xi - vec_x0
    R = subt_vec.module() / vec_xi.module()

    print(f"Iteração: {iter+1}  -   Resíduo: {R}")

    if R > r_min and iter < it_max: return jacobizinho(n, m, v, xi, iter+1, r_min, it_max)

    return [iter+1, x0, xi, R]

def jacobi(N, M, V, R_min=0.0001, iter_max=50):

    # contando as iterações
    iterations = 0
    
    # Vetor inicial
    x0 = [1]*N
    
    # fazendo recursão
    xList = jacobizinho(N, M, V, x0, iterations, R_min, iter_max)

    for i in range(N):
        print(f'x{i+1} = {xList[2][i]}' )
    
    return xList[2]
