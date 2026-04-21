import numpy as np
from scipy.linalg import lu_factor, lu_solve

def LU(n, M, V):
    m = np.array(M)
    v = np.array(V)

    lu, piv = lu_factor(m)
    xList = lu_solve((lu, piv), v)
    xList = xList.ravel()

    for i in range(n):
        print(f'x{i+1} = {xList[i]}' )
    
    return xList
