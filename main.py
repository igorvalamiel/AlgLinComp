def linha(): print('='*90)

def cria_matriz(n):
    m = []
    for i in range(n):
        linha = [int(j) for j in input(f"Linha {i+1}: ").split()]
        
        if len(linha) != n: raise IndexError #trantando erro se a linha tiver mais q n itens

        m.append(linha)
    return m

def cria_vetor(n):
    v = [int(j) for j in input(f"Vetor: ").split()]

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
M = cria_matriz(n)
V = cria_vetor(n)

# escolhendo método de solução
linha()
print("Esse programa usa 4 tipos de métodos para solução de Equações Lineares:")
print("a) Eliminação Gaussiana")
print("b) Fatoração LU")
print("c) Método de Jacobi")
print("d) Método de Gauss-Seidl")
metodo = str(input("\nEscolha o método [a, b, c, d]: ").lower())
linha()

if metodo == 'a':
    print("Método escolhido: Eliminação Gaussiana")
elif metodo == 'b':
    print("Método escolhido: Fatoração LU")
elif metodo == 'c':
    print("Método escolhido: Método de Jacobi")
elif metodo == 'd':
    print("Método escolhido: Método de Gauss-Seidl")
else:
    raise ValueError


# vendo andamento
#print(n)
#print(M)
#print(V)