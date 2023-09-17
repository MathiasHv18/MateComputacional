import random
import heapq
import numpy as np

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


def initializeVisitedMatrix(dimensiones, puntoInicial):
    visited = []

    for i in range(dimensiones):
        visited.append([])
    for list in visited:
        for i in range(dimensiones):
            list.append(False)

    visited[puntoInicial][puntoInicial] = True
    return visited


def updateVisited(visited, i, j):

    visited[j][j] = True
    visited[i][j] = True
    visited[j][i] = True
    return visited


def crearDiccionario(dimensiones):
    tiemposNodos = {}
    for i in range(dimensiones):
        tiemposNodos[i] = float('inf')
    return tiemposNodos


def actualizarPesos(distanciasFinales, nodeToUpdate, stepsList, iteration, visited, currentIndex):

    pesoFinal = 0
    for value in stepsList:
        pesoFinal = pesoFinal + distanciasFinales[value]
    pesoFinal = pesoFinal + nodeToUpdate[0]

    if iteration == 0:
        updateVisited(visited, currentIndex, nodeToUpdate[1])
        if distanciasFinales[nodeToUpdate[1]] == float('inf') or distanciasFinales[nodeToUpdate[1]] > distanciasFinales[currentIndex] + nodeToUpdate[0]:
            distanciasFinales[nodeToUpdate[1]] = distanciasFinales[currentIndex] + nodeToUpdate[0]
    else:
        if distanciasFinales[nodeToUpdate[1]] == float('inf') or distanciasFinales[nodeToUpdate[1]] > distanciasFinales[currentIndex] + nodeToUpdate[0]:
            distanciasFinales[nodeToUpdate[1]] = distanciasFinales[currentIndex] + nodeToUpdate[0]
    return distanciasFinales, visited


def getShortestPath(matrizPesos, currentIndex, distanciasFinales, visited, stepsList):

    shortestPath = []

    for i,  value in enumerate(matrizPesos[currentIndex]):
        if value != 0 and visited[currentIndex][i] == False:
            shortestPath.append((value, i))

    shortestPath = sorted(shortestPath, key=lambda x: x[0])

    print(shortestPath)

    # shortestPath(VALOR, NODO)
    # distanciasFinales(NODO) -> Peso Actual

    # Actualiza los tiempos estimados por cada nodo observado desde otro nodo
    for i, nodeToUpdate in enumerate(shortestPath):
        distanciasFinales, visited = actualizarPesos(
            distanciasFinales, nodeToUpdate, stepsList, i, visited, currentIndex)

    return shortestPath[0][1], distanciasFinales, visited


def dijkstra(matrizPesos, puntoInicial, puntoFinal):

    dimensiones = len(matrizPesos_ejemplo)
    stepsList = []

    currentIndex = puntoInicial
    # Canvas de distancias finales todo INFINITO
    distanciasFinales = crearDiccionario(dimensiones)
    distanciasFinales[puntoInicial] = 0

    # Todo FALSO porque no hemos visitado ni un Nodo
    visited = initializeVisitedMatrix(dimensiones, puntoInicial)

    visited = np.array(visited)

    while True:

        stepsList.append(currentIndex)
        # Lista de nodos visitados desde el i actual junto a sus pesos
        nextNode, distanciasFinales, visited = getShortestPath(
            matrizPesos, currentIndex, distanciasFinales, visited, stepsList)
        currentIndex = nextNode
        if visited[puntoFinal][puntoFinal]:
            break

    print('Steps list: ', stepsList)
    return distanciasFinales


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

matrizPesos_ejemplo = [[0,  0,  3,  0, 0, 2, 0],
                       [0,  0,  0, 1, 2, 0, 2],
                       [3,  0, 0,  4, 1, 2, 0],
                       [0,  1, 4,  0, 0, 0, 0],
                       [0, 2, 1,  0, 0, 3, 0],
                       [2, 0, 2,  0, 3, 0, 5],
                       [0, 2, 0,  0, 0, 5, 0]]

# print(matrizPesos)

matrizPesos_ejemplo = np.array(matrizPesos_ejemplo)
print(matrizPesos_ejemplo)

distanciasFinales = {}

puntoInicial = int(input('Ingrese el punto inicial: '))
puntoFinal = int(input('Ingrese el punto final: '))

distanciasFinales = dijkstra(
    matrizPesos_ejemplo, puntoInicial, puntoFinal)

print('Distancias Finales: ', distanciasFinales)
print('Demora ', distanciasFinales[puntoFinal],
      ' minutos en llegar al punto ', puntoFinal)