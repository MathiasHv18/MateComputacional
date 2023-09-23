import numpy as np
import graphviz as gv


def createVisualGraph(matrizPesos):
    grafo = gv.Graph('grafo')
    n = len(matrizPesos)

    for i in range(n):
        for j in range(i+1, n):
            peso = matrizPesos[i][j]
            if peso != 0:
                grafo.edge(str(i), str(j), label=str(peso))

    return grafo


def IDS(matrizPesos, valor):
    profundidad = 0

    while True:
        result = DLS(matrizPesos, 0, profundidad)
        for tupla in result:
            if valor == tupla[0]:
                return tupla
        profundidad += 1


def DLS(adjMatrix, startNode, depthLimit):
    n = len(adjMatrix)
    visited = [False] * n
    stack = []
    result = []

    stack.append((startNode, 0))  # Tupla: (nodo, profundidad)
    visited[startNode] = True

    while stack:
        node, depth = stack.pop()
        result.append((node, depth))

        if depth < depthLimit:
            for i in range(n):
                if adjMatrix[node, i] != 0 and not visited[i]:
                    visited[i] = True
                    stack.append((i, depth + 1))

    return result


def crearVisitados(dimensiones, puntoInicial):
    listaVisitados = [False] * dimensiones
    listaVisitados[puntoInicial] = True
    return listaVisitados


def actualizarVisitados(listaVisitados, index):
    listaVisitados[index] = True
    return listaVisitados


def crearDiccionario(dimensiones, puntoInicial):
    tiemposNodos = {}
    for i in range(dimensiones):
        tiemposNodos[i] = float('inf')
    tiemposNodos[puntoInicial] = 0
    return tiemposNodos


def ordenarLista(lista):
    return sorted(lista, key=lambda x: x[0])


def actualizarMinimo(lista, tiempoNodos, peso, nodeToMove):
    for value in lista:
        if value[0] < tiempoNodos[value[1]]:
            tiempoNodos[value[1]] = value[0]
    return tiempoNodos


def getAdyacentes(array, listaVisitados, nodeToMove, tiemposNodos, nodoProveniente):
    listaAdyacentes = []
    for i, value in enumerate(array[nodeToMove, :]):
        if value != 0 and listaVisitados[i] == False:
            listaAdyacentes.append(
                [value + tiemposNodos[nodeToMove], i, nodeToMove])

    listaAdyacentes = sorted(listaAdyacentes, key=lambda x: x[0])
    return listaAdyacentes, listaVisitados


def costoUniforme(array, puntoInicial):
    nodeToMove = puntoInicial
    nodoProveniente = puntoInicial
    tiempoNodos = crearDiccionario(len(matrizPesos), puntoInicial)
    listaVisitados = crearVisitados(len(matrizPesos), puntoInicial)
    colaAdyacentes = []
    while not all(listaVisitados):

        listaAdyacentes, listaVisitados = getAdyacentes(
            array, listaVisitados, nodeToMove, tiempoNodos, nodoProveniente)

        for value in listaAdyacentes:
            colaAdyacentes.append(value)

        colaAdyacentes = ordenarLista(colaAdyacentes)

        listaVisitados = actualizarVisitados(
            listaVisitados, colaAdyacentes[0][1])

        actualizarMinimo(colaAdyacentes, tiempoNodos,
                         array[colaAdyacentes[0][2], colaAdyacentes[0][1]], nodeToMove)
        nodeToMove = colaAdyacentes[0][1]
        nodoProveniente = colaAdyacentes[0][2]
        colaAdyacentes.pop(0)
    return tiempoNodos


matrizPesos = np.array([[0,  0,  3,  0, 0, 2, 0],
                        [0,  0,  0, 1, 2, 0, 2],
                        [3,  0, 0,  4, 1, 2, 0],
                        [0,  1, 4,  0, 0, 0, 0],
                        [0, 2, 1,  0, 0, 3, 0],
                        [2, 0, 2,  0, 3, 0, 5],
                        [0, 2, 0,  0, 0, 5, 0]])

grafo = createVisualGraph(matrizPesos)
grafo.render('MyGrafo', format='png')

tiempoNodos = costoUniforme(matrizPesos, 0)
print('Diccionario de los tiempos nodos: ', tiempoNodos)

recorridoDFS = DLS(matrizPesos, 0, float('inf'))
valorIDS = IDS(matrizPesos, 1)

print('Recorrido DFS: ' , recorridoDFS)
print('Valos por IDS: ' , valorIDS)

