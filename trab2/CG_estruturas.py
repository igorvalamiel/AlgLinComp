from estruturas import Matriz
import random
from copy import deepcopy

class CG_Matriz(Matriz):
    def __init__(self, n, m, v=0, identity=False):
        super().__init__(n, m, v, identity=True)

        for i in range(n-1):
            for j in range(i+1, m):
                if i == j: print("Deu merda")
                valor = random.uniform(-1,1)
                self.mat[i][j] = valor
                self.mat[j][i] = valor
    
    def filtro_de_corte(self, t):

        nova = CG_Matriz(self.lin, self.col)
        nova.mat = deepcopy(self.mat)

        for i in range(self.lin - 1):
            for j in range(i + 1, self.lin):

                if abs(nova.mat[i][j]) > t:
                    nova.mat[i][j] = 0
                    nova.mat[j][i] = 0

        return nova
    
def CG_transpose(M):
    Mt = CG_Matriz(M.m, M.n)
    for i in range(M.n):
        for j in range(M.m):
            Mt.mat[j][i] = M.mat[i][j]

    return Mt

def teste_de_aplicacao(A, n):

    # verificando simetria 
    B = A - CG_transpose(A)
    maior = 0
    for i in range(B.lin):
        for j in range(B.col):
            maior = max(maior, abs(B.mat[i][j]))

    # verificando positividade
    y = Matriz(n,1,[1]*n)
    v2 = CG_transpose(y)*A*y

    if maior != 0:
        if v2 <= 0:
            return False, "Matriz não simétrica, e não positiva definida."
        else:
            return False, "Matriz positiva definida, mas não simetrca."
    else:
        if v2 <= 0:
            return False, "Matriz simétrica, mas nao positiva definida."
        else:
            return True, "Matriz simétrica, e positiva definida!"
    