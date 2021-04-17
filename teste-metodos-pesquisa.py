import numpy as np
import random
import time
import os


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def bubble_sort(vetor):  # ordena o vetor pelo método de bolha
    troca = 0
    comp = 0
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            comp += 1
            if vetor[j] > vetor[j + 1]:
                troca += 1
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    print(f'Bolha: {comp} comparações e {troca} trocas')
    return vetor


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def insertion_sort(vetor):  # ordena o vetor pelo método de inserção (Direita para Esquerda)
    troca = 0
    comp = 0
    for i in range(0, len(vetor)):  # Percorre todo o vetor
        atual = vetor[i]
        comp += 1
        while i > 0 and vetor[
            i - 1] > atual:  # Enquanto ele for maior que 0 (se for 0, automaticamente será realocado) e
            comp += 1  # o vetor na posição anterior for maior que a var atual, será feita a troca
            troca += 1
            vetor[i] = vetor[i - 1]
            i -= 1

        vetor[i] = atual  # Troca novamente para add o valor retirado
    print(f'Inserção: {comp} comparações e {troca} trocas')
    return vetor


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def merge_sort(vetor):  # ordena o vetor pelo método de partição
    inicio = 0
    fim = len(vetor) - 1
    aux = [0] * len(vetor)  # cria um vetor aux com a mesma quantidade de elementos do vetor principal
    mergesort(vetor, aux, inicio, fim)
    return vetor


def mergesort(vetor, aux, inicio, fim):  # ordena o vetor pelo método de partição
    global comp
    comp += 1
    if fim <= inicio:  # quando fim for igual ao inicio, finaliza as repartições do vetor
        return
    meio = (inicio + fim) // 2

    mergesort(vetor, aux, inicio, meio)  # Ordena a primeira metade do arranjo.

    mergesort(vetor, aux, meio + 1, fim)  # Ordena a segunda metade do arranjo.

    merge(vetor, aux, inicio, meio, fim)  # Combina as duas metades ordenadas anteriormente.


def merge(vetor, aux, inicio, meio, fim):
    global comp
    global troca
    for k in range(inicio, fim + 1):  # copia o vetor e define j como meio+1
        troca += 1
        aux[k] = vetor[k]  # copia o vetor principal para o aux
    j = meio + 1
    for k in range(inicio, fim + 1):
        if inicio > meio:  # se inicio é maior que meio
            comp += 1
            troca += 1
            vetor[k] = aux[j]  # troca o elemento index pelo meio+1
            j += 1
        elif j > fim:  # se meio é maior que fim
            comp += 2
            troca += 1
            vetor[k] = aux[inicio]  # troca elemento index pelo inicio
            inicio += 1
        elif aux[j] < aux[inicio]:  # se meio é menor que inicio
            comp += 3
            troca += 1
            vetor[k] = aux[j]  # troca elemento index pelo meio
            j += 1
        else:  # se não for nenhuma opção anterior
            comp += 3
            troca += 1
            vetor[k] = aux[inicio]  # troca elemento index pelo inicio
            inicio += 1


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def selection_sort(vetor):  # ordena o vetor pelo método de seleção (Esquerda para Direita)
    troca = 0
    comp = 0
    for i in range(0, len(vetor)):  # Percorrer toda a lista
        min = i  # Add valor de i
        for prox in range(i + 1, len(vetor)):  # Percorre a lista fazendo verificações
            comp += 1
            if vetor[prox] < vetor[min]:  # Caso o valor da posição da var min for menor
                min = prox  # "Salva" a posição encontrada na var min
        troca += 1
        vetor[i], vetor[min] = vetor[min], vetor[i]  # Realiza a troca
    print(f'Seleção: {comp} comparações e {troca} trocas')
    return vetor


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def shell_sort(vetor):  # ordena o vetor por mais de um método
    troca = 0  # zera trocas
    comp = 0  # e comparações
    intervalo = len(
        vetor) // 2  # tamanho do intervalo a ser usado para as trocas futuras, a cada iteracao ele diminuira ate chegar a 1
    while intervalo > 0:
        for i in range(intervalo):  # de 0 até metade do vetor
            for j in range(i + intervalo, len(vetor) + 1,
                           intervalo):  # de i+metade até o final do vetor, aumentando a quantidade de intervalo em intervalo
                atual = vetor[j - 1]  # atual recebe o valor anterior
                posicao = j - 1  # posição do anterior
                comp += 1  # add uma comparação a cada for
                while posicao >= intervalo and vetor[posicao - intervalo] > atual:
                    comp += 1  # add uma comparação a cada while
                    troca += 1  # add uma troca a cada while
                    vetor[posicao] = vetor[posicao - intervalo]  # troca os dois valores
                    posicao -= intervalo
                troca += 1
                vetor[posicao] = atual
        intervalo = intervalo // 2  # vai diminuindo o intervalo cada vez mais
    print(f'Shell: {comp} comparações e {troca} trocas')
    return vetor


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def partition(vetor, menor, maior):
    global troca  # variavel de controle para contabilização de trocas
    global comp  # variavel de controle para contabilização de comparações

    i = (menor - 1)  # index do menor elemento
    pivo = vetor[maior]  # pivô

    for j in range(menor, maior):
        comp += 1  # adiciona uma comparação no contador
        if vetor[j] <= pivo:  # verifica se o elemento atual é menor ou igual ao pivô
            i = i + 1  # incrementa o index do menor
            troca += 1  # adiciona uma troca no contador
            vetor[i], vetor[j] = vetor[j], vetor[i]  # faz a troca dos valores

    troca += 1  # adiciona uma troca no contador
    vetor[i + 1], vetor[maior] = vetor[maior], vetor[i + 1]  # troca o menor pelo maior
    return (i + 1)  # retorna o index do local correto


def quick_sort(vetor, menor, maior):
    if len(vetor) == 1:  # verifica se o vetor só um valor, então não precisa ordenar
        return vetor
    if menor < maior:
        pi = partition(vetor, menor, maior)  # particiona o index e leva o vetor[p] para o local correto
        quick_sort(vetor, menor, pi - 1)  # ordena os elementos antes e depois das repartições
        quick_sort(vetor, pi + 1, maior)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def ordenar(vetor):
    global comp
    global troca

    start = time.time()
    bubble_sort(np.array(vetor))
    end = time.time()
    print(f'Bolha demorou {end - start} segundos\n')

    start = time.time()
    insertion_sort(np.array(vetor))
    end = time.time()
    print(f'Inserção demorou {end - start} segundos\n')

    start = time.time()
    merge_sort(np.array(vetor))
    print(f'Partição: {comp} comparações e {troca} trocas')
    end = time.time()
    print(f'Partição demorou {end - start} segundos\n')

    start = time.time()
    selection_sort(np.array(vetor))
    end = time.time()
    print(f'Seleção demorou {end - start} segundos\n')

    start = time.time()
    shell_sort(np.array(vetor))
    end = time.time()
    print(f'Shell demorou {end - start} segundos\n')

    comp = 0
    troca = 0
    start = time.time()
    quick_sort(np.array(vetor), 0, len(np.array(vetor)) - 1)
    print(f'Quick: {comp} comparações e {troca} trocas')
    end = time.time()
    print(f'Quick demorou {end - start} segundos\n')

    input('Aperte <Enter> para continuar...')


troca = 0
comp = 0
opcao = 1
while (opcao != 0):
    os.system('cls')
    print('-=-=-=-=-=-=-=-=-=-')
    print('1 - Criar novo Vetor de 1.000 Elementos')
    print('2 - Criar novo Vetor de 10.000 Elementos')
    print('3 - Criar novo Vetor de 50.000 Elementos')
    print('4 - Criar novo Vetor de 100.000 Elementos')
    print('5 - Iniciar as Ordenações')
    print('0 - sair')
    print('-=-=-=-=-=-=-=-=-=-')
    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        vetor = [0] * 1000
        for i in range(999):
            vetor[i] = random.randint(0, 1000)
        print('Vetor criado com sucesso!')
        input('Aperte <Enter> para continuar...')

    elif (opcao == 2):
        vetor = [0] * 10000
        for i in range(9999):
            vetor[i] = random.randint(0, 1000)
        print('Vetor criado com sucesso!')
        input('Aperte <Enter> para continuar...')

    elif (opcao == 3):
        vetor = [0] * 50000
        for i in range(49999):
            vetor[i] = random.randint(0, 1000)
        print('Vetor criado com sucesso!')
        input('Aperte <Enter> para continuar...')

    elif (opcao == 4):
        vetor = [0] * 100000
        for i in range(99999):
            vetor[i] = random.randint(0, 1000)
        print('Vetor criado com sucesso!')
        input('Aperte <Enter> para continuar...')

    elif (opcao == 5):
        ordenar(vetor)

    elif (opcao == 0):
        print('Até mais!')
        break
