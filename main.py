import numpy as np
import graphviz as gv
import random

def createVisualGraph(matrizPesos):
    grafo = gv.Graph('grafo')
    n = len(matrizPesos)

    for i in range(n):
        for j in range(i+1, n):
            peso = matrizPesos[i][j]
            if peso != 0:
                grafo.edge(str(i), str(j), label=str(peso))

    return grafo
def generarMatrizSimetrica():
    tamano = random.randint(5, 15)
    
    matriz = np.zeros((tamano, tamano))
    
    for i in range(tamano):
        for j in range(i, tamano):
            valor = random.randint(0, 7)  # Valores entre 0 y 7
            matriz[i][j] = valor
            matriz[j][i] = valor
    
    for i in range(tamano):
        for j in range(i, tamano):
            if i == j:
                matriz[i][j] = 0
    cantidad_ceros = int(tamano * tamano * 0.4)  # Ajusta este valor según tus necesidades
    for _ in range(cantidad_ceros):
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)
        matriz[fila][columna] = 0
        matriz[columna][fila] = 0
    return matriz

class AlgortimoDeDijkstra:
    def __init__(self, matriz):
        self.matrizPesos = matriz
        self.nodoInicio = 0
        self.nodoFinal = 0

    def crearVisitados(self, dimensiones, puntoInicial):
        listaVisitados = [False] * dimensiones
        listaVisitados[puntoInicial] = True
        return listaVisitados

    def actualizarVisitados(self, listaVisitados, index):
        listaVisitados[index] = True
        return listaVisitados

    def crearDiccionario(self, dimensiones, puntoInicial):
        tiemposNodos = {}
        for i in range(dimensiones):
            tiemposNodos[i] = float('inf')
        tiemposNodos[puntoInicial] = 0
        return tiemposNodos

    def ordenarLista(self, lista):
        return sorted(lista, key=lambda x: x[0])

    def actualizarMinimo(self, lista, tiempoNodos, peso, nodeToMove):
        for value in lista:
            if value[0] < tiempoNodos[value[1]]:
                tiempoNodos[value[1]] = value[0]
        return tiempoNodos

    def getAdyacentes(self, array, listaVisitados, nodeToMove, tiemposNodos, nodoProveniente):
        listaAdyacentes = []
        for i, value in enumerate(array[nodeToMove, :]):
            if value != 0 and listaVisitados[i] == False:
                listaAdyacentes.append(
                    [value + tiemposNodos[nodeToMove], i, nodeToMove])

        listaAdyacentes = sorted(listaAdyacentes, key=lambda x: x[0])
        return listaAdyacentes, listaVisitados

    def costoUniforme(self, puntoInicial):
        nodeToMove = puntoInicial
        nodoProveniente = puntoInicial
        tiempoNodos = self.crearDiccionario(len(self.matrizPesos), puntoInicial)
        listaVisitados = self.crearVisitados(len(self.matrizPesos), puntoInicial)
        colaAdyacentes = []
        while not all(listaVisitados):

            listaAdyacentes, listaVisitados = self.getAdyacentes(
                self.matrizPesos, listaVisitados, nodeToMove, tiempoNodos, nodoProveniente)

            for value in listaAdyacentes:
                colaAdyacentes.append(value)

            if not colaAdyacentes:  # Verifica si la lista está vacía
                break

            colaAdyacentes = self.ordenarLista(colaAdyacentes)

            listaVisitados = self.actualizarVisitados(
                listaVisitados, colaAdyacentes[0][1])

            self.actualizarMinimo(colaAdyacentes, tiempoNodos,
                            self.matrizPesos[colaAdyacentes[0][2], colaAdyacentes[0][1]], nodeToMove)
            nodeToMove = colaAdyacentes[0][1]
            nodoProveniente = colaAdyacentes[0][2]
            colaAdyacentes.pop(0)
        return tiempoNodos
    def encontrarCaminoMinimo(self, nodoInicio, nodoFinal):
        tiemposNodos = self.costoUniforme(nodoInicio)

        camino = [nodoFinal]
        while camino[-1] != nodoInicio:
            nodoActual = camino[-1]
            nodoAnterior = None
            pesoMinimo = float('inf')
            for i, peso in enumerate(self.matrizPesos[:, nodoActual]):
                if peso != 0 and tiemposNodos[i] + peso == tiemposNodos[nodoActual] and tiemposNodos[i] < tiemposNodos[nodoActual]:
                    if peso < pesoMinimo:
                        pesoMinimo = peso
                        nodoAnterior = i
            if nodoAnterior is None:
                return None, None 
            camino.append(nodoAnterior)
        camino.reverse()

        return camino, tiemposNodos[nodoFinal]

    def actualizarMatriz(self):
        nuevaMatriz = generarMatrizSimetrica()
        self.matrizPesos = nuevaMatriz
        grafo = createVisualGraph(self.matrizPesos)
        grafo.render('MyGrafo', format='png')

#matrizPesos = generarMatrizSimetrica()
#dijkstra = AlgortimoDeDijkstra(matrizPesos)

#grafo = createVisualGraph(matrizPesos)
#grafo.render('MyGrafo', format='png')

#tiempoNodos = dijkstra.costoUniforme(1)
#print(tiempoNodos)