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

    def BuscaBinaria_VetorOrdenado(self, numero):
        inicio = 0
        fim = self.capacidade - 1
        meio = (inicio + fim) // 2
        while numero != self.valores[meio] and inicio <= fim:
            meio = (inicio + fim) // 2
            if numero == self.valores[meio]:
                return meio
            elif numero < self.valores[meio]:
                fim = meio - 1
            elif numero > self.valores[meio]:
                inicio = meio + 1
        return -1

    def BuscaBinaria_Recursiva(self, numero, inicio, fim):
        meio = (inicio + fim) // 2
        if numero == self.valores[meio]:
            return meio
        elif inicio == fim:
            return -1
        elif numero < self.valores[meio]:
            fim = meio - 1
        elif numero > self.valores[meio]:
            inicio = meio + 1
        return self.BuscaBinaria_Recursiva(numero, inicio, fim)

    def Hashing(self, valor):
        return (valor % 31) + 1






x = VetorNaoOrdenado(50)
for i in range(49):
  x.inserir(random.randrange(0, 2000)) #inserindo valores aleatórios

x.inserir(575)
x.ordena_bolha()
x.imprimir()
# posicao = x.BuscaBinaria_Recursiva(575, 0, 50)
posicao = x.BuscaBinaria_VetorOrdenado(575)
print(f'Valor encontrado na posição {posicao}')