from CG_estruturas import CG_Matriz, teste_de_aplicacao
from estruturas import Matriz, transpose
from random import randint

def CG_method(tau, r_min=1e-16, it_max=20):
    A = CG_Matriz(500, 500)
    A = A.filtro_de_corte(tau)
    
    teste = teste_de_aplicacao(A)

    if not teste[0]: raise teste[1]
    else: print(teste[1])
    
    x = Matriz(500, 1)
    b = Matriz(500, 1, [1]*500)
    v = b - (A * x)
    r = b - (A * x)
    Beta = 0
    it = 1
    it_list = [1]
    r_list = [r.module()]

    while True:
        vt = transpose(v)


        # passo
        ai_up = vt*r
        ai_down = (vt*A)*v
        ai = ai_up/ai_down

        # atualizacao de x (solucao)
        x += v.multiplicar(ai)

        # atualizacao de r (residuo)
        r -= (A*v).multiplicar(ai)

        # atualizacao de Beta (fator correcao)
        B_up = (vt*A)*r
        B_down = (vt*A)*v
        Beta = (-1*B_up)/B_down # o -1 é pra inverter a direcao do gradiente

        # ataulizacao do v (vetor de direcao)
        v = r + (v.multiplicar(Beta))

        r_mod = r.module() # modulo do vetor de residuo

        if (it < it_max and r_mod > r_min):
            it += 1
            it_list.append(it)
            r_list.append(r_mod)
        else: break

    return x, it_list, r_list



# [0.01, 0.05, 0.1, 0.2] ~> OBS: ver com professor se precisa fazer todos os testes de tau com a mesma matriz
for tau in [0.01, 0.05, 0.1, 0.2]:
    print(f"tau = {tau}")
    print('_'*50)
    M, itList, rList = CG_method(tau)

    for i in range(1, 501):
        print(f"x{i}: {M.mat[i-1][0]}")

    print('~'*50)

    for i in range(len(itList)):
        print(f"it [{itList[i]}] :    r ~> {rList[i]}")

    print('~'*50)

