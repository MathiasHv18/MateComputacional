import random
import numpy as np
import graphviz as gv
import tkinter as tk

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


def createVisualGraph(matrizPesos):
    grafo = gv.Graph('grafo')
    n = len(matrizPesos)

    for i in range(n):
        for j in range(i+1, n):
            peso = matrizPesos[i][j]
            if peso != 0:
                grafo.edge(str(i), str(j), label=str(peso))

    return grafo


def initializeVisitedMatrix(dimensiones, puntoInicial):
    visited = np.zeros((dimensiones, dimensiones))
    visited[:, puntoInicial] = True
    return visited


def crearDiccionario(dimensiones):
    tiemposNodos = {}
    for i in range(dimensiones):
        tiemposNodos[i] = float('inf')
    return tiemposNodos


def updateVisited(visited, i, j):

    visited[:, j] = True
    visited[i, j] = True
    visited[j, i] = True

    return visited


def actualizarPesos(distanciasFinales, nodeToUpdate, stepsList, iteration, visited, currentIndex):

    pesoFinal = 0
    for value in stepsList:
        pesoFinal = pesoFinal + distanciasFinales[value]
    pesoFinal = pesoFinal + nodeToUpdate[0]

    if iteration == 0:
        visited = updateVisited(visited, currentIndex, nodeToUpdate[1])
        if distanciasFinales[nodeToUpdate[1]] == float('inf') or distanciasFinales[nodeToUpdate[1]] > distanciasFinales[currentIndex] + nodeToUpdate[0]:
            distanciasFinales[nodeToUpdate[1]
                              ] = distanciasFinales[currentIndex] + nodeToUpdate[0]
    else:
        if distanciasFinales[nodeToUpdate[1]] == float('inf') or distanciasFinales[nodeToUpdate[1]] > distanciasFinales[currentIndex] + nodeToUpdate[0]:
            distanciasFinales[nodeToUpdate[1]
                              ] = distanciasFinales[currentIndex] + nodeToUpdate[0]
    return distanciasFinales, visited


def buscar_repetidos(lista_tuplas):

    valoresRepetidos = []
    contador = -1
    for tupla in lista_tuplas:
        valoresRepetidos.append(tupla[0])

    valoresRepetidos.sort()
    minimoValor = valoresRepetidos[0]

    for i in valoresRepetidos:
        if i == minimoValor:
            contador += 1
    if contador == 0:
        return -1, -1
    else:
        return minimoValor, contador


def getShortestPath(matrizPesos, currentIndex, distanciasFinales, visited, stepsList):

    shortestPath = []
    listaNodosVisitados = []

    for i,  value in enumerate(matrizPesos[currentIndex]):
        if value != 0 and visited[currentIndex][i] == True:
            listaNodosVisitados.append((value, i))
        if value != 0 and visited[currentIndex][i] == False:
            shortestPath.append((value, i))

    listaNodosVisitados = sorted(listaNodosVisitados, key=lambda x: x[0])
    shortestPath = sorted(shortestPath, key=lambda x: x[0])


    if len(shortestPath) > 0:
        valorRepetido, repeticiones = buscar_repetidos(shortestPath)
        if shortestPath[0][0] == valorRepetido:
            for i in range(repeticiones):
                visited = updateVisited(
                    visited, currentIndex, shortestPath[i+1][1])

    # Actualiza los tiempos estimados por cada nodo observado desde otro nodo
    if len(shortestPath) == 0:
        for i, nodeToUpdate in enumerate(listaNodosVisitados):
            distanciasFinales, visited = actualizarPesos(
                distanciasFinales, nodeToUpdate, stepsList, i, visited, currentIndex)
        return listaNodosVisitados[0][1], distanciasFinales, visited
    else:
        for i, nodeToUpdate in enumerate(shortestPath):
            distanciasFinales, visited = actualizarPesos(
                distanciasFinales, nodeToUpdate, stepsList, i, visited, currentIndex)
        return shortestPath[0][1], distanciasFinales, visited



def dijkstra(matrizPesos, puntoInicial, puntoFinal):

    dimensiones = len(matrizPesos)
    # Nodos que el algoritmo a tenido que recorrer
    stepsList = []
    # Punto inicial ingresado por el usuario
    currentIndex = puntoInicial
    # Diccionario de distancias finales. Inicialmente todo INFINITO menos el punto inicial
    distanciasFinales = crearDiccionario(dimensiones)
    distanciasFinales[puntoInicial] = 0

    # Todo FALSO porque no hemos visitado ni un Nodo
    visited = initializeVisitedMatrix(dimensiones, puntoInicial)

    # Mientras que el punto final no se considere visitado, aplicar dijkstra
    while True:

        stepsList.append(currentIndex)
        # Calcular los caminos desde algun nodo X
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
#
matrizPesos = [[0,  0,  3,  0, 0, 2, 0],
               [0,  0,  0, 1, 2, 0, 2],
               [3,  0, 0,  4, 1, 2, 0],
               [0,  1, 4,  0, 0, 0, 0],
               [0, 2, 1,  0, 0, 3, 0],
               [2, 0, 2,  0, 3, 0, 5],
               [0, 2, 0,  0, 0, 5, 0]]


matrizPesos = np.array(matrizPesos)
print(matrizPesos)
grafo = createVisualGraph(matrizPesos)
grafo.render('MyGrafo', format='png')


distanciasFinales = {}

puntoInicial = int(input('Ingrese el punto inicial: '))
puntoFinal = int(input('Ingrese el punto final: '))

distanciasFinales = dijkstra(
    matrizPesos, puntoInicial, puntoFinal)

print('Distancias Finales: ', distanciasFinales)
print('Demora ', distanciasFinales[puntoFinal],
      ' minutos en llegar al punto ', puntoFinal)
