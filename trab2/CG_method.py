from CG_estruturas import CG_Matriz
from estruturas import Matriz

def CG_method():
    M = CG_Matriz(500, 500)

    for t in [0.01, 0.05, 0.1, 0.2]:
        filteredM = M.filtro_de_corte(t)
        print(filteredM.mat[0])


CG_method()
