import heapq

def dijkstra(matrizPesos, puntoInicial):
    n = len(matrizPesos)
    visitados = [False] * n
    distancias = [float('inf')] * n
    distancias[puntoInicial] = 0

    cola_prioridad = [(0, puntoInicial)]  # Una cola de prioridad de tuplas (distancia, nodo)

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if visitados[nodo_actual]:
            continue  # Si el nodo ya ha sido visitado, pasa al siguiente

        visitados[nodo_actual] = True

        for vecino in range(n):
            if not visitados[vecino] and matrizPesos[nodo_actual][vecino] > 0:
                nuevaDistancia = distancia_actual + matrizPesos[nodo_actual][vecino]
                if nuevaDistancia < distancias[vecino]:
                    distancias[vecino] = nuevaDistancia
                    heapq.heappush(cola_prioridad, (nuevaDistancia, vecino))

    print(distancias)

# Ejemplo de uso
matrizPesos = [[0, 7, 5, 5, 19], [7, 0, 10, 15, 12], [5, 10, 0, 19, 4], [5, 15, 19, 0, 9], [19, 12, 4, 9, 0]]
puntoInicial = 0
dijkstra(matrizPesos, puntoInicial)
