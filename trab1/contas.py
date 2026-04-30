from gaussiana_pura import gaussiana_pura
from gaussiana import gaussiana
from LU_pura import LU_pura
from LU import LU
from jacobi import jacobi
from GaussSeidl import gauss_seidl

from verifica import verifica
from estruturas import Matriz
from time import time


def coleta_matriz(n):
    m = []
    for i in range(n):
        linha = [float(j) for j in input(f"Linha {i+1}: ").split()]

        if len(linha) != n: raise IndexError #trantando erro se a linha tiver mais q n itens

        m += linha
    return m

def coleta_vetor(n):
    v = [float(j) for j in input(f"Vetor: ").split()]

    if len(v) != n: raise IndexError #tratando erro se o vetor tiver mais q n valores

    return v



n = int(input("N = "))
M = coleta_matriz(n)
V = coleta_vetor(n)
m = Matriz(n, n, M)
v = Matriz(n, 1, V)
metodo = str(input("\nEscolha o método [a, b, c, d, e, f]: ").lower())

sum = 0
time_list = []

for i in range(10):

    if metodo == 'a':
        ti = time()
        xList_gaussPura = gaussiana_pura(n, m, v)
        tf = time()
        time_list.append(tf-ti)

    elif metodo == 'b':
        ti = time()
        xList_gauss = gaussiana(n, m.mat, v.mat)
        tf = time()
        time_list.append(tf-ti)

    elif metodo == 'c':
        ti = time()
        xList_luPura = LU_pura(n, M, V) # sim aqui é M e V pra nao ficar moddificando as matrizes originais
        tf = time()
        time_list.append(tf-ti)

    elif metodo == 'd':
        ti = time()
        xList_lu = LU(n, m.mat, v.mat)
        tf = time()
        time_list.append(tf-ti)

    elif metodo == 'e':
        ti = time()
        xList_jacobi, tf = jacobi(n, m.mat, v.mat, salvar_chart=False) # tive que colocar o tf aqui pra nao contar o tempo de fazer o gráfico
        time_list.append(tf-ti)

    elif metodo == 'f':
        ti = time()
        xList_gauss_seidl, tf = gauss_seidl(n, m.mat, v.mat, salvar_chart=False) # tive que colocar o tf aqui pra nao contar o tempo de fazer o gráfico
        time_list.append(tf-ti)

    else:
        raise ValueError

print(time_list)

for i in time_list:
    print(f"- {i}")
    sum += i

print(f"Média: {sum/10}")
