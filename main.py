from gaussiana_pura import gaussiana_pura
from gaussiana import gaussiana

# -----------------------------------------------------------------------------------------------------
def linha(): print('='*90)

def coleta_matriz(n):
    m = []
    for i in range(n):
        linha = [int(j) for j in input(f"Linha {i+1}: ").split()]

        if len(linha) != n: raise IndexError #trantando erro se a linha tiver mais q n itens

        m += linha
    return m

def coleta_vetor(n):
    v = [int(j) for j in input(f"Vetor: ").split()]

    if len(v) != n: raise IndexError #tratando erro se o vetor tiver mais q n valores

    return v

# função que criei para ajustar ao input da biblioteca Numpy
def arruma_matvec(n, M, is_vector=0):
    v = []
    passo = n
    if is_vector: passo = 1
    i0 = 0

    for i in range(passo, len(M)+1, passo):
        v.append(M[i0:i])
        i0 = i
    
    print(v)
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

# escolhendo método de solução
linha()
print("Esse programa usa 4 tipos de métodos para solução de Equações Lineares:")
print("a) Eliminação Gaussiana")
print("b) Eliminação Gaussiana otimizada")
print("c) Fatoração LU")
print("d) Fatoração LU otimizada")
print("e) Método de Jacobi")
print("f) Método de Gauss-Seidl")
metodo = str(input("\nEscolha o método [a, b, c, d]: ").lower())
linha()

if metodo == 'a':
    print("Método escolhido: Eliminação Gaussiana")
    gaussiana_pura(n, M, V)
elif metodo == 'b':
    print("Método escolhido: Eliminação Gaussiana Otimizada")
    gaussiana(n, arruma_matvec(n, M), arruma_matvec(n, V, 1))
elif metodo == 'c':
    print("Método escolhido: Fatoração LU")
elif metodo == 'd':
    print("Método escolhido: Fatoração LU Otimizada")
elif metodo == 'e':
    print("Método escolhido: Método de Jacobi")
elif metodo == 'f':
    print("Método escolhido: Método de Gauss-Seidl")
else:
    raise ValueError
