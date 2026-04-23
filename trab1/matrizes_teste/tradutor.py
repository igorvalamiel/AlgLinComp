"""
        OBS: Esse código foi gerado 100% pela Claude.ai!!!!

Conversor de arquivo Matrix Market (.mtx) para .txt
no formato de entrada do sistema linear:
  - Linha 1: N (tamanho da matriz)
  - Linhas 2..N+1: linhas da matriz separadas por espaço
  - Última linha: vetor aleatório gerado (N números separados por espaço)
"""

import sys
import random


def ler_matrix_market(nome_arquivo):
    """
    Lê um arquivo .mtx no formato Matrix Market (coordinate ou array).
    Retorna (n_linhas, n_colunas, matriz densa como lista de listas).
    """
    with open(f"../matrizes_teste/{nome_arquivo}", 'r') as f:
        linhas = f.readlines()

    # Processar cabeçalho
    header = None
    idx = 0
    for i, linha in enumerate(linhas):
        linha = linha.strip()
        if linha.startswith("%%MatrixMarket"):
            header = linha.lower()
            idx = i + 1
        elif linha.startswith("%"):
            idx = i + 1  # pular comentários
        else:
            idx = i
            break

    if header is None:
        raise ValueError("Arquivo não possui cabeçalho %%MatrixMarket válido.")

    # Ler dimensões
    partes = linhas[idx].split()
    n_rows = int(partes[0])
    n_cols = int(partes[1])
    idx += 1

    # Inicializar matriz densa com zeros
    matriz = [[0.0] * n_cols for _ in range(n_rows)]

    if "coordinate" in header:
        # Formato esparso: cada linha é "i j valor"
        for linha in linhas[idx:]:
            linha = linha.strip()
            if not linha or linha.startswith("%"):
                continue
            partes = linha.split()
            i = int(partes[0]) - 1  # 1-indexed → 0-indexed
            j = int(partes[1]) - 1
            v = float(partes[2])
            matriz[i][j] = v

    elif "array" in header:
        # Formato denso: valores coluna a coluna
        valores = []
        for linha in linhas[idx:]:
            linha = linha.strip()
            if not linha or linha.startswith("%"):
                continue
            valores.append(float(linha.strip()))
        k = 0
        for j in range(n_cols):
            for i in range(n_rows):
                matriz[i][j] = valores[k]
                k += 1
    else:
        raise ValueError("Formato Matrix Market não suportado (esperado: coordinate ou array).")

    return n_rows, n_cols, matriz


def gerar_vetor_aleatorio(n, min_val=-10, max_val=10):
    """Gera vetor aleatório de inteiros entre min_val e max_val."""
    return [random.randint(min_val, max_val) for _ in range(n)]


def formatar_numero(v):
    """Formata número: inteiro se não tiver parte decimal, float caso contrário."""
    if v == int(v):
        return str(int(v))
    else:
        # Remove zeros à direita desnecessários
        return f"{v:.6g}"


def salvar_txt(n, matriz, vetor, nome_saida):
    """
    Salva o arquivo .txt no formato:
      N
      linha_0
      linha_1
      ...
      linha_N-1
      vetor
    """
    with open(nome_saida, 'w') as f:
        f.write(f"{n}\n")
        for linha in matriz:
            f.write(" ".join(formatar_numero(v) for v in linha) + "\n")
        f.write(" ".join(formatar_numero(v) for v in vetor) + "\n")


def imprimir_matriz(matriz):
    n = len(matriz)
    print(f"\n  Matriz {n}×{n} lida:")
    for linha in matriz:
        print("    " + " ".join(f"{formatar_numero(v):>6}" for v in linha))


def imprimir_vetor(vetor):
    print(f"\n  🎲 Vetor aleatório gerado ({len(vetor)} elementos):")
    print("    [ " + "  ".join(str(v) for v in vetor) + " ]")


def main():
    print("=" * 50)
    print("   CONVERSOR .MTX → .TXT")
    print("=" * 50)

    # Obter nome do arquivo de entrada
    if len(sys.argv) >= 2:
        nome_entrada = sys.argv[1]
    else:
        nome_entrada = input("\nNome do arquivo .mtx de entrada: ").strip()

    # Obter nome do arquivo de saída
    if len(sys.argv) >= 3:
        nome_saida = sys.argv[2]
    else:
        nome_saida = input("Nome do arquivo .txt de saída [saida.txt]: ").strip()
        if not nome_saida:
            nome_saida = "saida.txt"

    # Ler .mtx
    print(f"\nLendo '{nome_entrada}'...")
    try:
        n_rows, n_cols, matriz = ler_matrix_market(nome_entrada)
    except FileNotFoundError:
        print(f"✗ Arquivo '{nome_entrada}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Erro ao ler o arquivo: {e}")
        sys.exit(1)

    if n_rows != n_cols:
        print(f"⚠ Atenção: matriz não é quadrada ({n_rows}×{n_cols}). Usando N={n_rows}.")

    n = n_rows
    imprimir_matriz(matriz)

    # Gerar vetor aleatório
    vetor = gerar_vetor_aleatorio(n)
    imprimir_vetor(vetor)

    # Salvar .txt
    salvar_txt(n, matriz, vetor, nome_saida)

    print(f"\n✓ Arquivo '{nome_saida}' gerado com sucesso!")
    print("\n  Prévia do arquivo gerado:")
    print("  " + "─" * 30)
    with open(nome_saida, 'r') as f:
        for linha in f:
            print("  " + linha, end="")
    print("\n  " + "─" * 30)
    print("=" * 50)


if __name__ == "__main__":
    main()
