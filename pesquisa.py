import time
import random
import numpy as np


class VetorNaoOrdenado:  # classe para trabalhar com vetores estáticos (sem as listas do Python)

    def __init__(self, capacidade):  # método construtor
        self.capacidade = capacidade  # quantos elementos vou poder guardar no meu vetor

        self.ultimaPosicao = -1  # pois o vetor começa vazio

        self.valores = np.empty(capacidade, dtype=int)  # criando o vetor

    def inserir(self, valor):  # insere um elemento no final
        self.ultimaPosicao = self.ultimaPosicao + 1
        self.valores[self.ultimaPosicao] = valor

    def imprimir(self):  # imprime todo o vetor
        for i in range(self.ultimaPosicao + 1):
            print('posição ', i, ' valor ', self.valores[i])

    def ordena_bolha(self):  # ordena o vetor pelo método Bubble Sort
        troca = True
        while troca:  # repito enquanto houver ao menos uma troca
            troca = False
            for i in range(self.ultimaPosicao):
                if self.valores[i] > self.valores[i + 1]:  # se o da esquerda é maior então troca
                    aux = self.valores[i]
                    self.valores[i] = self.valores[i + 1]
                    self.valores[i + 1] = aux
                    troca = True

    def Busca_VetorNaoOrdenado(self, valor):  # faz uma busca sequencial até o fim do vetor
        for i in range(self.ultimaPosicao + 1):
            if self.valores[i] == valor:
                return i

        return -1  # se chegou até aqui não encontrou

    def Busca_VetorOrdenado(self, valor):  # faz uma busca sequencial até o fim do vetor
        for i in range(self.ultimaPosicao + 1):
            if self.valores[i] == valor:
                return i
            elif self.valores[i] > valor:
                return -1  # já não tenho chance de encontrar

        return -1  # se chegou até aqui não encontrou

    def BuscaBinaria_VetorOrdenado(self, valor):
        meio = int((len(self.valores) / 2))
        print(f'meio == {meio}')
        if valor == self.valores[meio]:
            return meio
        if valor < self.valores[meio]:
            for i in range(meio):
                if valor == self.valores[meio - i]:
                    return meio - i
        if valor > self.valores[meio]:
            for i in range(meio+1):
                if valor == self.valores[meio + i]:
                    return meio + i

    def BuscaBinaria_Recursiva(self, valor, inicio, fim):
        meio = int((fim - inicio) / 2)
        print(f'meiorec == {meio}')
        if valor == self.valores[meio]:
            return meio
        if valor < self.valores[meio]:
            self.BuscaBinaria_Recursiva(self, valor, 0, meio)
        if valor > self.valores[meio]:
            self.BuscaBinaria_Recursiva(self, valor, meio, len(self.valores))

    def Hashing(self, valor):
        pass



x = VetorNaoOrdenado(11)
#for i in range(9000000):
    #x.inserir(random.randrange(0, 555))  # inserindo valores aleatórios
x.inserir(3)
x.inserir(4)
x.inserir(11)
x.inserir(12)
x.inserir(21)
x.inserir(34)
x.inserir(65)
x.inserir(77)
x.inserir(78)
x.inserir(89)
x.inserir(112)


#posrec = x.BuscaBinaria_Recursiva(4, 0, len(x.valores))
#print(f'posrec == {posrec}')
#pos = x.BuscaBinaria_VetorOrdenado(4)
#print(f'pos == {pos}')

#x.inserir(556)
# x.ordena_bolha()
# x.imprimir()

#antes = time.time()  # timestamp de antes de chamar a busca
#pos = x.Busca_VetorNaoOrdenado(556)

#segundos = time.time() - antes
#print(f'Levou {segundos} segundos')

#if pos >= 0:
#    print(f'Valor encontrado na posição {pos}')
#else:
#    print('Valor não encontrado')