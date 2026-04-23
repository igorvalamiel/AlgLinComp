from gaussiana_pura import gaussiana_pura
from gaussiana import gaussiana
from LU_pura import LU_pura
from LU import LU
from jacobi import jacobi
from GaussSeidl import gauss_seidl

from verifica import verifica
from estruturas import Matriz
from time import time

# -----------------------------------------------------------------------------------------------------
def linha(): print('='*90)

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

# -----------------------------------------------------------------------------------------------------
# introdução
linha()
print("Boas Vindas ao solucionador de Equações Lineares!\n")
print("Para o bom funcionamento do programa, siga as seguintes regras:")
print('1) Insira o valor inteiro N da matriz NxN;')
print('2) Aparecerão N linhas de input, insira os valores de cada linha separando com um espaço;')
print('3) Insira os valores do vetor em uma única linha, separando os números com um espaço.')
linha()

# pegando matriz e vetor
n = int(input("N = "))
M = coleta_matriz(n)
V = coleta_vetor(n)
m = Matriz(n, n, M)
v = Matriz(n, 1, V)

# escolhendo método de solução
linha()
print("Esse programa usa 4 tipos de métodos para solução de Equações Lineares:")
print("a) Eliminação Gaussiana")
print("b) Eliminação Gaussiana (NumPy)")
print("c) Fatoração LU")
print("d) Fatoração LU (SciPy)")
print("e) Método de Jacobi")
print("f) Método de Gauss-Seidl")
metodo = str(input("\nEscolha o método [a, b, c, d, e, f]: ").lower())
linha()


#lembrar de comparar os tempos com e sem biblioteca
if metodo == 'a':
    print("Método escolhido: Eliminação Gaussiana")
    ti = time()
    xList_gaussPura = gaussiana_pura(n, m, v)
    tf = time()
    print(f"\nTempo de execução: {tf-ti} segundos.")
    print(verifica(n, m, v, xList_gaussPura))

elif metodo == 'b':
    print("Método escolhido: Eliminação Gaussiana Otimizada (Numpy)")
    ti = time()
    xList_gauss = gaussiana(n, m.mat, v.mat)
    tf = time()
    print(f"\nTempo de execução: {tf-ti} segundos.")
    print(verifica(n, m, v, xList_gauss))

elif metodo == 'c':
    print("Método escolhido: Fatoração LU")
    ti = time()
    xList_luPura = LU_pura(n, M, V) # sim aqui é M e V pra nao ficar moddificando as matrizes originais
    tf = time()
    print(f"\nTempo de execução: {tf-ti} segundos.")
    print(verifica(n, m, v, xList_luPura))

elif metodo == 'd':
    print("Método escolhido: Fatoração LU Otimizada (SciPy)")
    ti = time()
    xList_lu = LU(n, m.mat, v.mat)
    tf = time()
    print(f"\nTempo de execução: {tf-ti} segundos.")
    print(verifica(n, m, v, xList_lu))

elif metodo == 'e':
    print("Método escolhido: Método de Jacobi")
    ti = time()
    xList_jacobi, tf = jacobi(n, m.mat, v.mat, salvar_chart=False) # tive que colocar o tf aqui pra nao contar o tempo de fazer o gráfico
    print(f"\nTempo de execução: {tf-ti} segundos.")
    print(verifica(n, m, v, xList_jacobi))  # ver com professor se precisa mesmo de verificar o jacobi ou poded só usar o R

elif metodo == 'f':
    print("Método escolhido: Método de Gauss-Seidl")
    ti = time()
    xList_gauss_seidl, tf = gauss_seidl(n, m.mat, v.mat, salvar_chart=False) # tive que colocar o tf aqui pra nao contar o tempo de fazer o gráfico
    print(f"\nTempo de execução: {tf-ti} segundos.")
    print(verifica(n, m, v, xList_gauss_seidl))

else:
    raise ValueError
