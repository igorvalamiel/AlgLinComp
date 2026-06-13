from CG_estruturas import CG_Matriz, teste_de_aplicacao, CG_transpose
from estruturas import Matriz
from random import randint

def calling_CG_method(n, A, b, r_min, it_max):
    x = Matriz(n, 1)
    v = b - (A * x)
    r = b - (A * x)

    Beta = 0
    it = 0
    it_list = [0]
    r_list = [r.module()]

    r_old = CG_transpose(r) * r

    for it in range(1, it_max + 1):

        Av = A * v
        vAv = CG_transpose(v) * Av

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

        r_new = CG_transpose(r) * r
        Beta = r_new/r_old # atualizacao de Beta (fator correcao)
        r_old = r_new
        v = r + (v.multiplicar(Beta)) # ataulizacao do v (vetor de direcao)

    return x, it_list, r_list


def make_graph(dados_dos_testes):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    
    for tau, (itList, rList) in dados_dos_testes.items():
        plt.plot(itList, rList, label=f'tau = {tau}', marker='o', markersize=3)
    
    plt.xlabel('Iterações')
    plt.ylabel('Módulo do Resíduo (r)')
    plt.title('Convergência do Gradiente Conjugado para diferentes valores de Tau')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()


def CG_method(n=500, A=None, b=None, r_min=1e-16, it_max=20):

    if A is None:
        A = CG_Matriz(500, 500)
    
    if b is None:
        random_list = [randint(-10, 10) for _ in range(n)]
        b = Matriz(n, 1, random_list)

    data_dict = {}
    
    for tau in [0.01, 0.05, 0.1, 0.2]:
        print(f"tau = {tau}")
        print('_'*50)

        # testando matriz
        A_filtrada = A.filtro_de_corte(tau)
        teste = teste_de_aplicacao(A_filtrada, n)
        if not teste[0]: raise teste[1]
        else: print(teste[1])

        # fazendo o metodo
        M, itList, rList = calling_CG_method(n, A_filtrada, b, r_min, it_max)
        data_dict[tau] = (itList, rList)

        # printando os resultados
        for i in range(1, n+1):
            print(f"x{i}: {M.mat[i-1][0]}")

        print('~'*50)

        for i in range(len(itList)):
            print(f"it [{itList[i]}] :    r ~> {rList[i]}")

        print('~'*50)
        
    make_graph(data_dict)

