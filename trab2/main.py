from estruturas import Matriz
from CG_method import *
from CG_estruturas import CG_Matriz
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
print("Boas Vindas ao solucionador de Equações Lineares por Gradientes Conjugados!\n")
print("Para o bom funcionamento do programa, siga as seguintes regras:")
print('1) Insira o valor inteiro N da matriz NxN;')
print('2) Aparecerão N linhas de input, insira os valores de cada linha separando com um espaço;')
print('3) Insira os valores do vetor em uma única linha, separando os números com um espaço.')
linha()

if int(input("Você quer inserir sua matriz? [0 : não  -  1 : sim] ")) == 0:
    print("""
Ok, realizando teste padrão:
  - Matriz A:          500x500
  - Vetor b:           500x1
  - Resíduo mínimo:    1e-16
  - Iterações máximas: 20
""")
    CG_method()
else:
    # pegando matriz e vetor
    n = int(input("N = "))
    M = coleta_matriz(n)
    V = coleta_vetor(n)
    m = CG_Matriz(n, n, M)
    v = CG_Matriz(n, 1, V)

    linha()

    print("\nRealizando Método Iterativo de Gradientes Conjugados:\n")
    CG_method(n, m, v)

