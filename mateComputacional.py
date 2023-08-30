
"""
Matriz adjacencia ejemplo
        H o r i z o n 
  V      A   B   C   D
  e  A   0   4   0   5
  r  B   1   0   0   2
  t  C   0   0   0   3
  i  D   5   2   3   0

Se lee de 'A' hacia 'B'. Primero el horizontal y luego el vertical
Cada valor es el peso que toma de X lugar a Y lugar
En caso haya un 0 es porque no hay conexion directa entre ambas aristas
"""
matrizAd = []

dimensiones = int(input('Indique las dimensiones de la matriz a generar: '))
#opcionGenerar = int(input('Desea generar los valores de manera manual o aleatoria?: '))

for i in range(dimensiones):
    for j in range(dimensiones):
        matrizAd.append([])


print(matrizAd)
