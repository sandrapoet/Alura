"""
Rotate Matrix In-Place
You are given an N x N 2D matrix representing an image. Rotate the image 90 degrees clockwise, in-place (i.e., without using extra space for another matrix).
"""
def rotate_matrix(matrix):
    n = len(matrix)

    # Paso 1: Transponer la matriz (fila ↔ columna)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Paso 2: Invertir cada fila (para rotar 90°)
    for row in matrix:
        row.reverse()

# Test
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
rotate_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
"""
¿Por qué funciona?
Transposición convierte filas en columnas.
Reversión de filas completa la rotación de 90° en sentido horario.
Todo se hace in-place, sin usar matrices auxiliares.
¿Cuándo aplicar este patrón?
Cuando el problema mencione rotación de matriz y sin usar espacio adicional.
Cuando trabajes con matrices cuadradas.
Cuando se requiera modificar directamente la estructura de datos.
"""
"""
You are given an N x N 2D matrix representing an image. Rotate the image 90 degrees clockwise, in-place (i.e., without using extra space for another matrix).
"""
def rotate_matrix(matrix):
    n = len(matrix)

    # Paso 1: Transponer la matriz (fila ↔ columna)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Paso 2: Invertir cada fila (para rotar 90°)
    for row in matrix:
        row.reverse()

# Test
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
rotate_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
"""
¿Cuándo aplicar este patrón?
Cuando el problema mencione rotación de matriz y sin usar espacio adicional.
Cuando trabajes con matrices cuadradas.
Cuando se requiera modificar directamente la estructura de datos.
"""


"""
Rotate Matrix 180 Degrees In-Place
You are given an N x N 2D matrix. Rotate the matrix 180 degrees in-place, meaning you must modify the original matrix directly without using extra space proportional to its size.
"""
def rotate_180(matrix):
    n = len(matrix)

    # Intercambiar elementos simétricos respecto al centro
    for i in range(n // 2):
        for j in range(n):
            # Intercambio vertical
            matrix[i][j], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[i][j]

    # Si la matriz tiene tamaño impar, invertir la fila central
    if n % 2 == 1:
        mid = n // 2
        matrix[mid].reverse()

# Test
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
rotate_180(matrix)
print(matrix)  # Output: [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
"""
¿Por qué funciona?
Intercambia cada elemento con su opuesto en la matriz.
Para matrices impares, la fila del medio se invierte porque no tiene contraparte.
"""
