import math
import sympy as sp

# Função geradora de matriz eletrônica
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

# Função geradora de matriz de combinação e suas respectivas combinações de variáveis
def matriz_combinacao(variaveis):
    n = len(variaveis)
    linhas = 2 ** n
    
    for i in range(linhas):
        linha_binaria = []
        subconjunto = []
        for j in range(n):
            if math.floor(i / (2 ** j)) % 2 == 1:
                linha_binaria.append(1)
                subconjunto.append(variaveis[j])
            else:
                linha_binaria.append(0)
        
        print(f"{linha_binaria} = {subconjunto}")

# Função geradora da fórmula Bernoulli
def bernoulli(m):
    numeros_bernoulli = {0: 1, 1: -1/2, 2: 1/6, 4: -1/30, 6: 1/42, 8: -1/30}
    soma = 0
    n = sp.symbols('n')

    for j in range (m+1):
        soma += ((-1)**j)*sp.binomial(m+1, j)*numeros_bernoulli.get(j, 0)*(n**(m+1-j))
    
    return sp.pretty(sp.factor(sp.simplify(soma / (m+1), rational=True)))


if __name__ == '__main__':
    # Teste Matriz da Eletrônica Digital
    # qtd_elementos = 4
    # print(matriz_eletronica(qtd_elementos))

    expoente = 1
    print(bernoulli(expoente))
    expoente = 2
    print(bernoulli(expoente))
    expoente = 3
    print(bernoulli(expoente))
    expoente = 4
    print(bernoulli(expoente))

    # Teste Gráfico Combinações
    # lista_variaveis = ["a0", "a1", "a2", "a3"]
    # print(matriz_combinacao(lista_variaveis))

