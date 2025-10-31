"""
Problema: Recorrido en Espiral Spiral Matrix Traversal
Dada una matriz m * n, devuelve todos sus elementos en orden de espiral (comenzando desde el elemento superior izquierdo y avanzando hacia el centro). 
You are given a 2D matrix of size m x n. Your task is to return all elements of the matrix in spiral order, starting from the top-left corner and moving clockwise toward the center.
1    2    3
4    5    6
7    8    9
Salida Esperada: [1, 2, 3, 6, 9, 8, 7, 4, 5] 
Estrategia (Mecánica de Two Pointers en 2D) 
La forma más eficiente y controlada de realizar el recorrido en espiral es usando cuatro punteros que definen los límites de la matriz (la "ventana" que se reduce en cada paso). 
top: Índice de la fila superior (comienza en 0). 
bottom: Índice de la fila inferior (comienza en R-1). 
left: Índice de la columna izquierda (comienza en 0). 
right: Índice de la columna derecha (comienza en C-1). 
En cada iteración, recorremos un borde y luego movemos ese puntero hacia adentro, reduciendo la ventana. 
Los 4 Pasos del Recorrido: 
Recorrer a la DERECHA (de left a right) en la fila top. Incrementa top. 
Recorrer ABAJO (de top a bottom) en la columna right. Decrementa right. 
Recorrer a la IZQUIERDA (de right a left) en la fila bottom. Decrementa bottom. 
Recorrer ARRIBA (de bottom a top) en la columna left. Incrementa left. 
La condición clave es asegurar que el ciclo continúa mientras top <= bottom y left <= right. Además, el Paso 3 y 4 requieren verificación adicional en el bucle principal para manejar matrices de una sola fila o columna. 
Usa extend() para agregar múltiples elementos de una fila directamente.
Usa slicing con [::-1] para invertir filas sin bucles.
"""
def spiral_traversal(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Izquierda → Derecha
        result.extend(matrix[top][left:right+1])
        top += 1

        # Arriba → Abajo
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        # Derecha → Izquierda
        if top <= bottom:
            result.extend(matrix[bottom][left:right+1][::-1])
            bottom -= 1

        # Abajo → Arriba
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

# Test
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(spiral_traversal(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""
¿Cuándo aplicar este patrón?
Cuando el problema mencione recorrer una matriz en espiral.
Cuando se indique orden de recorrido no convencional (espiral, zigzag, diagonal).
Cuando se trabaje con matrices 2D y se requiera control de límites.
"""

