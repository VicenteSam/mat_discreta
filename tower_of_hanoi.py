import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

def tabela_binaria(n):
    return [[int(b) for b in format(i, f'0{n}b')] for i in range(2**n)]

def discos_movimento_grafico(tabela, n):
    movimentos = []
    for i in range(1, len(tabela)):
        for disco in range(n):
            if tabela[i-1][disco] == 0 and tabela[i][disco] == 1:
                movimentos.append((disco + 1, i))
    return movimentos

def torre_grafico(ax, posicoes, n, movimento_num, texto=""):
    ax.clear()
    largura_haste = 0.1
    altura_disco = 0.1
    altura_haste = n * altura_disco + 0.5

    for i in range(3):
        ax.add_patch(patches.Rectangle((1 + 2 * i - largura_haste / 2, 0), largura_haste, altura_haste, edgecolor='black', facecolor='grey'))

    cores = ['red', 'orange', 'yellow', 'green', 'blue']

    altura_nas_hastes = {1: 0, 2: 0, 3: 0}

    for disco in range(1, n + 1):
        posicao = posicoes[disco]
        altura_nas_hastes[posicao] += 1

        largura_disco = 0.3 * (n - disco + 1)
        centro_x = (posicao * 2) - 1
        altura_atual = (altura_nas_hastes[posicao] - 1) * altura_disco

        cor_atual = cores[(disco - 1) % len(cores)]
        ax.add_patch(patches.Rectangle((centro_x - largura_disco / 2, altura_atual), largura_disco, altura_disco, facecolor=cor_atual, edgecolor='black'))

    ax.set_xlim(0, 6)
    ax.set_ylim(0, altura_haste)
    ax.set_xticks([1, 3, 5])
    ax.set_xticklabels(['A', 'B', 'C'])
    ax.set_yticks([])

def rastrear_movimentos(n, origem, destino, auxiliar, movimentos, ax, anim_frames):
    posicoes = {i: 1 for i in range(1, n + 1)}
    anim_frames.append((posicoes.copy(), 0, "Início"))

    for movimento_num, (disco, _) in enumerate(movimentos, 1):
        haste_atual = posicoes[disco]
        if haste_atual == 1:
            nova_posicao = 3 if disco % 2 == 1 else 2
        elif haste_atual == 2:
            nova_posicao = 1 if disco % 2 == 1 else 3
        else:
            nova_posicao = 2 if disco % 2 == 1 else 1

        torres = {1: 'A', 2: 'B', 3: 'C'}
        texto_movimento = f"Mover disco {disco} da torre {torres[haste_atual]} para a torre {torres[nova_posicao]}"

        posicoes[disco] = nova_posicao
        anim_frames.append((posicoes.copy(), movimento_num, texto_movimento))

def grafico_torre(n):
    fig, ax = plt.subplots()
    tabela = tabela_binaria(n)
    movimentos = discos_movimento_grafico(tabela, n)

    origem, destino, auxiliar = 'A', 'C', 'B'
    anim_frames = []
    rastrear_movimentos(n, origem, destino, auxiliar, movimentos, ax, anim_frames)

    def atualizar(frame):
        posicoes, movimento_num, texto = frame
        torre_grafico(ax, posicoes, n, movimento_num, texto)

    anim = FuncAnimation(fig, atualizar, frames=anim_frames, interval=1000, repeat=False)
    plt.show()

def main():
    n = int(input("Número de discos (máx.5): "))
    grafico_torre(n)

if __name__ == "__main__":
    main()
