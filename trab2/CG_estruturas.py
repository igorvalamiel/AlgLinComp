from estruturas import Matriz
import random
from copy import deepcopy

class CG_Matriz(Matriz):
    def __init__(self, n, m, v=0, identity=False):
        super().__init__(n, m, v, identity=True)

        for i in range(n-1):
            for j in range(i+1, n):
                if i == j: print("Deu merda")
                self.mat[i][j] = random.uniform(-1,1)
                self.mat[j][i] = random.uniform(-1,1)
    
    def filtro_de_corte(self, t):

        nova = CG_Matriz(self.lin, self.col)
        nova.mat = deepcopy(self.mat)

        for i in range(self.lin - 1):
            for j in range(i + 1, self.lin):

                if abs(nova.mat[i][j]) > t:
                    nova.mat[i][j] = 0
                    nova.mat[j][i] = 0

        return nova


        