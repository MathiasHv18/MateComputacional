import random

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


def generarMatriz():
    #Diccionar (Hash table)
    matrizAd = {}

    dimensiones = int(input('Indique las dimensiones de la matriz a generar: '))
    
    # Crea una matriz de X*X dimensiones con valor infinito en cada conexión
    for i in range(dimensiones):
        for j in range(dimensiones):
            matrizAd[(i, j)] = float('inf')

    opcionGenerar = input('Desea generar los valores de manera manual o aleatoria? M = Manual / A = Aleatoria: ')
    
    if opcionGenerar.upper() == 'M':
        for i in range(dimensiones):
            print('Ingrese los valores de la fila numero ' + str(i) + ': ')
            for j in range(dimensiones):
                if i != j:
                    valor = input('Casilla ' + str(j) + ' de ' + str(dimensiones) + ': ')
                    matrizAd[(i, j)] = int(valor)
    else:
        for i in range(dimensiones):
            for j in range(dimensiones):
                if i != j:
                    matrizAd[(i, j)] = random.randint(1, 20)  # Asigna pesos aleatorios de 1 a 20

    return matrizAd

def dijkstra(grafo, puntoInicial):
    numNodos = len(grafo)

matrizAd = generarMatriz()
print(matrizAd)

#puntoInicial = input('Ingrese el punto inicial: ')
# 0 = A / 1 = B / 2 = C ...
#dijkstra(matrizAd, puntoInicial)