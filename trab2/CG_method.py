from CG_estruturas import CG_Matriz, teste_de_aplicacao
from estruturas import Matriz, transpose
from random import randint

def calling_CG_method(A, b, r_min, it_max):
    x = Matriz(500, 1)
    v = b - (A * x)
    r = b - (A * x)

    Beta = 0
    it = 0
    it_list = [0]
    r_list = [r.module()]

    r_old = transpose(r) * r

    for it in range(1, it_max + 1):

        Av = A * v
        vAv = transpose(v) * Av

        # passo
        ai = r_old/vAv

        # atualizacao de x (solucao)
        x += v.multiplicar(ai)

        # atualizacao de r (residuo)
        r -= Av.multiplicar(ai)

        r_mod = r.module() # modulo do vetor de residuo
        it_list.append(it)
        r_list.append(r_mod)

        if r_mod <= r_min:
            break

        r_new = transpose(r) * r

        # atualizacao de Beta (fator correcao)
        Beta = r_new/r_old

        r_old = r_new

        # ataulizacao do v (vetor de direcao)
        v = r + (v.multiplicar(Beta))

    return x, it_list, r_list



def CG_method(r_min=1e-16, it_max=20):
    # iniciando matrizes para o teste
    A = CG_Matriz(500, 500)
    
    random_list = [randint(-10, 10) for _ in range(500)]
    b = Matriz(500, 1, random_list)
    
    for tau in [0.01, 0.05, 0.1, 0.2]:
        print(f"tau = {tau}")
        print('_'*50)

        # testando matriz
        A_filtrada = A.filtro_de_corte(tau)
        teste = teste_de_aplicacao(A_filtrada)
        if not teste[0]: raise teste[1]
        else: print(teste[1])

        # fazendo o metodo
        M, itList, rList = calling_CG_method(A_filtrada, b, r_min, it_max)

        # printando os resultados
        for i in range(1, 501):
            print(f"x{i}: {M.mat[i-1][0]}")

        print('~'*50)

        for i in range(len(itList)):
            print(f"it [{itList[i]}] :    r ~> {rList[i]}")

        print('~'*50)

CG_method()
