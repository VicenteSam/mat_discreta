import math

# Função para construir e imprimir matriz eletrônica
def matriz_eletronica(qtdVar):
    M = [[0 for _ in range(qtdVar)] for _ in range(2**qtdVar)]

    for i in range (2**qtdVar):
        for j in range (qtdVar):
            if math.floor((i)/(2**(qtdVar-j-1))) % 2 == 0:
                M[i][j] = 0
            else:
                M[i][j] = 1

    for linha in M:
        print(linha)

# Função para construir e imprimir de combinação
def matriz_combinacao(qtdVar):
    M = [[0 for _ in range(qtdVar)] for _ in range(2**qtdVar)]

    for i in range (2**qtdVar):
        for j in range (qtdVar):
            if math.floor(i/(2**j)) % 2 == 0:
                M[i][j] = 0
            else:
                M[i][j] = 1

    for linha in M:
        print(linha)

# Função n°1 - Somatório de potências 1^m+2^m+3^m+⋯+n^m
def somatorio_potencia(m, n):
    soma = 0
    for valor in range (1, n+1):
        soma += valor ** m
    return soma

# Função n°2 - Somatório de combinações a(m-j) = Σ (-1)^k*C(j,k)*(1-k+j)^m
def somatorio_combinacao(m):
    a = [0] * (m+1)
    for j in range (m+1):
        for k in range (j+1):
            a[j] += ((-1)**k)*formula_combinacao(j, k)*(1-k+j)**m
    return a

# Função n°3 - Somatório total Σ C(n, j+1)*a(m-j)
def somatorio_total(j, n, a):
    total = 0
    componentes = []
    for valor in range (j+1):
        componente = formula_combinacao(n, valor+1) * a[valor]
        total += componente
        componentes.append(f"C({n},{valor+1})*{a[valor]}")
    return total, componentes

# Função auxiliar - Cálculo de combinações C(m,k) = m!/(k!(m-k)!)
def formula_combinacao(m, k):
    if m >= k and k >= 0:
        fact_m, fact_k, fact_mk = 1, 1, 1
        for i in range(1, m+1):
            fact_m *= i
        for j in range(1, k+1):
            fact_k *= j
        for l in range(1, (m-k)+1):
            fact_mk *= l

        comb = fact_m/(fact_k*(fact_mk))
        return comb
    return 0

# Função de impressão - Imprime e prova as várias funções anteriores
def demonstracao(m, n):
    soma_potencias = somatorio_potencia(m, n)
    a = somatorio_combinacao(m)
    total, componentes = somatorio_total(m, n, a)

    print("            Verificação:")
    print(f"                     1^m + 2^m + 3^m + ⋯ + n^m = Σ C(n, j+1)*a(m-j)")
    print(f"            onde,")
    print(f"                     a(m-j) = Σ (-1)^k*C(j,k)*(1-k+j)^m")
    print("            logo:")
    
    # Expressão de a(m-j)
    a_expressao = ", ".join([f"a{m-j} = {a_val}" for j, a_val in enumerate(a)])
    print(f"                     {a_expressao}")

    # Soma total com componentes
    componentes_str = " + ".join(componentes)
    print(f"                     Σ = {componentes_str}")
    print(f"                     Σ = {total}")
    
    # Soma de potências
    potencias_str = " + ".join([f"{i}^{m}" for i in range(1, n + 1)])
    valores_str = " + ".join([f"{i**m}" for i in range(1, n + 1)])
    print(f"            em paralelo:")
    print(f"                     {potencias_str} = {valores_str} = {soma_potencias}")

    # Resultado final
    print(f"            por fim:")
    print(f"                     1^m + 2^m + 3^m + ⋯ + n^m = Σ C(n, j+1)*a(m-j)")

if __name__ == '__main__':
    # Teste Gráfico Eletrônico
    # qtd_elementos = 4
    # print(matriz_eletronica(qtd_elementos))

    # Teste Gráfico Combinações
    # qtd_elementos = 4
    # print(matriz_combinacao(qtd_elementos))
    
    # Teste Indução
    n = 10
    m = 3
    print(demonstracao(m, n))
