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

    visited[i][j] = True
    visited[j][i] = True
    return visited


def crearDiccionario(dimensiones):
    tiemposNodos = {}
    for i in range(dimensiones):
        tiemposNodos[i] = float('inf')
    return tiemposNodos


def actualizarPesos(distancias, indice, oldPeso, newPeso):

    if oldPeso == float('inf'):
        distancias[indice] = newPeso
        return distancias
    elif newPeso+distancias[indice] >= oldPeso + distancias[indice]:
        return distancias
    else:
        distancias[indice] = newPeso + distancias[indice]
        return distancias


def getShortestPath(matrizPesos, currentIndex, distanciasFinales, visited):
    shortestPath = []

    for i,  value in enumerate(matrizPesos[currentIndex]):
        if value != 0 and visited[currentIndex][i] == False:
            shortestPath.append((value, i))

    # Actualiza los tiempos estimados por cada nodo observado desde otro nodo
    for nodeToUpdate in shortestPath:
        actualizarPesos(
            distanciasFinales, nodeToUpdate[1], distanciasFinales[nodeToUpdate[1]], nodeToUpdate[0])

    return shortestPath, distanciasFinales


def dijkstra(matrizPesos, puntoInicial, dimensiones, puntoFinal):

    stepsList = []

    currentIndex = puntoInicial
    # Canvas de distancias finales todo INFINITO
    distanciasFinales = crearDiccionario(dimensiones)
    distanciasFinales[puntoInicial] = 0

    # Todo FALSO porque no hemos visitado ni un Nodo
    visited = initializeVisitedMatrix(dimensiones, puntoInicial)

    tiempoFinal = 0

    while distanciasFinales[puntoFinal] == float('inf'):

        stepsList.append(currentIndex)
        # Lista de nodos visitados desde el i actual junto a sus pesos
        nextNode, distanciasFinales = getShortestPath(
            matrizPesos, currentIndex, distanciasFinales, visited)
        heapq.heapify(nextNode)
        nodeAt = heapq.heappop(nextNode)

        # Actualiza de todo FALSO a nodo visitado TRUE
        visited = updateVisited(visited, nodeAt[1], currentIndex)

        currentIndex = nodeAt[1]
        #Se vacea la lista de nodos posibles a visitar
        nextNode = ()

    for node in stepsList:
        tiempoFinal = tiempoFinal + distanciasFinales[node]

    tiempoFinal = tiempoFinal + distanciasFinales[puntoFinal]

    return tiempoFinal, distanciasFinales


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


#matrizPesos, n = generarMatriz()
n = 5

matrizPesos_ejemplo = [[0,  7,  5,  0, 0],
                       [7,  0,  10, 15, 12],
                       [5,  10, 0,  19, 4],
                       [0,  15, 19,  0, 9],
                       [0, 12, 4,  9, 0]]

#print(matrizPesos)

tiempoFinal = 0
distanciasFinales = {}



puntoInicial = int(input('Ingrese el punto inicial: '))
puntoFinal =  int(input('Ingrese el punto final: '))

tiempoFinal, distanciasFinales = dijkstra(matrizPesos_ejemplo, puntoInicial, n, puntoFinal)

print(distanciasFinales)
print('Demora ', tiempoFinal, ' minutos en llegar al punto ', puntoFinal)