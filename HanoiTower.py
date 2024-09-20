# Torre de Hanói em Python
class hanoiTower:
    def __init__(self) -> None:
        self.numeroDeDiscos = 0
        self.numeroDeMovimentos = 0
        self.movimentos_binarios = []
    # Getters e Setters
    def getNumeroDeDiscos(self):
        return self.numeroDeDiscos
    
    def setNumeroDeDiscos(self, numeroDeDiscos):
        self.numeroDeDiscos = numeroDeDiscos

    def getNumeroDeMovimentos(self):
        return self.numeroDeMovimentos
    
    def setNumeroDeMovimentos(self, numeroDeMovimentos):
        self.numeroDeMovimentos = numeroDeMovimentos
    # Recebe número de discos (máx. 5)
    def inputQtd(self):
        self.numeroDeDiscos = int(input("Número de discos (máximo 5): "))
        if self.numeroDeDiscos > 5:
            print("Número máximo de discos é 5.")
            self.numeroDeDiscos = 5
    # Faz as trocas entre as torres
    def trocas(self, numDiscos, A, B, C):
        if numDiscos == 1:
            self.setNumeroDeMovimentos(self.getNumeroDeMovimentos()+1)
            print(f"Mover Disco {numDiscos} da torre {A} para a torre {C}")
            print(f"Movimentos: {self.getNumeroDeMovimentos()}\n")
            self.atualiza_matriz_binaria(numDiscos)
        else:
            self.trocas(numDiscos-1, A, C, B)
            self.setNumeroDeMovimentos(self.getNumeroDeMovimentos()+1)
            print(f"Mover Disco {numDiscos} da torre {A} para a torre {C}")
            print(f"Movimentos: {self.getNumeroDeMovimentos()}\n")
            self.atualiza_matriz_binaria(numDiscos)
            self.trocas(numDiscos-1, B, A, C)
    # Atualiza a matriz
    def atualiza_matriz_binaria(self, disco_movido):
        linha_movimento = [0] * self.numeroDeDiscos
        linha_movimento[disco_movido - 1] = 1
        self.movimentos_binarios.append(linha_movimento)
    # Retorna total de movimentos
    def totalMovimentos(self):
        print(f"Total de movimentos: {self.getNumeroDeMovimentos()}\n")
    # Retorna matriz binária
    def exibir_matriz_binaria(self):
        print("\nMatriz Binária de Movimentos:")
        for linha in self.movimentos_binarios:
            print(linha)

def jogar():
    k = hanoiTower()
    k.inputQtd()
    k.trocas(k.getNumeroDeDiscos(), 'A', 'B', 'C')
    k.totalMovimentos()
    k.exibir_matriz_binaria()

if __name__ == '__main__':
    jogar()
