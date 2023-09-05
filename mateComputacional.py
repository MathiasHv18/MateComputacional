import random
import heapq

"""
Matriz adjacencia ejemplo
        H o r i z o n 
  V      A   B   C   D
  e  A   0   1   0   5
  r  B   1   0   0   2
  t  C   0   0   0   3
  i  D   5   2   3   0

Se lee de 'A' hacia 'B'. Primero el horizontal y luego el vertical
Cada valor es el peso que toma de X lugar a Y lugar
En caso haya un 0 es porque no hay conexion directa entre ambas aristas
"""


def getShortestPath(matrizPesos, puntoInicial):
    shortestPath = []
    index = 0

    for i,  value in enumerate(matrizPesos[puntoInicial]):
        if value != 0:
            shortestPath.append((value, i))
            index = i

    return shortestPath


def updateVisited(visited, indices, puntoInicial):

    for i, indexJ in enumerate(indices):
        visited[puntoInicial][indexJ[1]] = True
        visited[i+1][puntoInicial] = True
    return visited


def dijkstra(matrizPesos, puntoInicial, dimensiones):

    currentIndex = puntoInicial
    visited = []
    for i in range(dimensiones):
        visited.append([])
    for list in visited:
        for i in range(dimensiones):
            list.append(False)
    visited[puntoInicial][puntoInicial] = True

    nextNode = getShortestPath(matrizPesos, puntoInicial)
    visited = updateVisited(visited, nextNode, puntoInicial)

    print(nextNode)
    heapq.heapify(nextNode)
    print(visited)


def generarMatriz():
    matrizAd = []

    dimensiones = int(
        input('Indique las dimensiones de la matriz a generar: '))
    # Crea una matriz de X*X dimensiones con valor 0 en cada casilla
    for i in range(dimensiones):
        matrizAd.append([0] * dimensiones)

    opcionGenerar = input(
        'Desea generar los valores de manera manual o aleatoria? M = Manual / A = Aleatoria: ')

    if opcionGenerar.upper() == 'M':
        for i in range(dimensiones):
            print('Ingrese los valores de la fila numero ' + str(i) + ': ')
            for j in range(dimensiones):
                valor = input('Casilla ' + str(j) + ' de ' +
                              str(dimensiones) + ': ')
                matrizAd[i][j] = int(valor)
    else:
        for i in range(dimensiones):
            for j in range(dimensiones):
                if i != j:
                    matrizAd[i][j] = random.randint(0, 20)
                else:
                    matrizAd[i][j] = 0

    # Convierte la matriz en simétrica
    for i in range(dimensiones):
        for j in range(i):
            matrizAd[i][j] = matrizAd[j][i]

    return matrizAd, dimensiones


# matrizPesos, n = generarMatriz()

matrizPesos = [[0,  7,  5,  0, 0],
               [7,  0,  10, 15, 12],
               [5,  10, 0,  19, 4],
               [0,  15, 19,  0, 9],
               [0, 12, 4,  9, 0]]

# print(matrizPesos)

dijkstra(matrizPesos, 0, 5)
