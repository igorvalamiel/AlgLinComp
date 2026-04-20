import numpy as np

def gaussiana(n, M, V):
    mat = np.array(M)
    vec = np.array(V)
    xList = np.linalg.solve(mat, vec)
    xList = xList.ravel()

    for i in range(n):
        print(f'x{i+1} = {xList[i]}' )
    
    return xList
