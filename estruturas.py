# reaproveitando meu código de matriz de Alg. Prog.

class Matriz():
    def __init__(self, n, m, v):
        for i in v:
            if type(i) != int or i<0:
                raise ValueError
        if len(v) != n*m: raise ValueError
        self.mat = []
        self.col = m
        self.lin = n
        self.tam = m*n
        for i in range(0, m*n, m):
            self.mat.append(v[i:i+m])

    def __add__(self, other):
        l_lin = (self.lin, other.lin)
        l_col = (self.col, other.col)
        new_mat = []
        for i in range(max(l_lin)):
            sl = []
            for j in range(max(l_col)):
                try:
                    sl.append(self.mat[i][j]+other.mat[i][j])
                except IndexError:
                    try:
                        sl.append(self.mat[i][j])
                    except IndexError:
                        sl.append(other.mat[i][j])
            new_mat.append(sl)
        new_mat = self.arrumar(new_mat, max(l_lin), max(l_col))
        return Matriz(max(l_lin), max(l_col), new_mat)
    
    def __sub__(self, other):
        l_lin = (self.lin, other.lin)
        l_col = (self.col, other.col)
        new_mat = []
        for i in range(max(l_lin)):
            sl = []
            for j in range(max(l_col)):
                try:
                    sl.append(self.mat[i][j]-other.mat[i][j])
                except IndexError:
                    try:
                        sl.append(self.mat[i][j])
                    except IndexError:
                        sl.append(other.mat[i][j])
            new_mat.append(sl)
        new_mat = self.arrumar(new_mat, max(l_lin), max(l_col))
        return Matriz(max(l_lin), max(l_col), new_mat)
    
    def __mul__(self, other):
        if self.n != other.m:
            raise ValueError
        new_mat = [[0 for _ in range(other.n)] for _ in range(self.m)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    new_mat[i][j] += self.mat[i][k] * other.mat[k][j]
        new_mat = self.arrumar(new_mat, other.n, self.m)
        return Matriz(other.n, self.m, new_mat)
    
    def __repr__(self):
        s = ''
        for i in self.mat:
            for j in i:
                s += str(j)+' '
            s+='\n'
        return s

    def __getitem__(self, key):
        if key[0]>self.lin or key[1]>self.col:
            raise IndexError
        return self.mat[key[0]][key[1]]
    
    def __setitem__(self, key, x):
        if self[key]:
            self.mat[key[0]][key[1]] = x
    
    def add_row(self, r):
        if len(r) != self.lin: raise ValueError
        self.mat.append(r)
        self.lin+=1
    
    def add_col(self, c):
        if len(c) != self.col: raise ValueError
        for i in range(self.lin):
            self.mat[i].append(c[i])
        self.col+=1
    
    def __linhas(self):
        return self.lin
    
    def __cols(self):
        return self.col
    
    def arrumar(self, p, n, m):
        r = []
        for i in range(n):
            for j in range(m):
                r.append(p[i][j])
        return r
    
    def det(self):
        return determinant(self.mat)
    
    n = property(__linhas)
    m = property(__cols)

def determinant(v):
    if len(v) == 1: return v[0][0]
    elif len(v) == 2: return (v[0][0]*v[1][1])-(v[0][1]*v[1][0])
    else:
        deter = 0
        for c in range(len(v)):
            menor = [x[:c] + x[c+1:] for x in v[1:]]
            deter += (((-1) ** c) * v[0][c] * determinant(menor))
        return deter
