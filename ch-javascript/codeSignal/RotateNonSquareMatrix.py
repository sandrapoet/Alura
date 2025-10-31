"""
Cuando te piden rotar una matriz no cuadrada 90° en sentido horario (clockwise), el enfoque cambia ligeramente respecto a una matriz cuadrada, porque no puedes hacerlo in-place sin usar espacio adicional.
Problem Name: Rotate Non-Square Matrix 90 Degrees Clockwise
Difficulty: Medium
Prompt:
You are given a 2D matrix of size m x n (not necessarily square). Your task is to return a new matrix that represents the original matrix rotated 90 degrees clockwise.
"""
def rotate_matrix_90(matrix):
    # Transponer y luego invertir cada fila
    return [list(row)[::-1] for row in zip(*matrix)]
matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
rotated = rotate_matrix_90(matrix)
for row in rotated:
    print(row)
# Output:
# [4, 1]
# [5, 2]
# [6, 3]  
"""
¿Por qué funciona?

zip(*matrix) transpone la matriz (convierte columnas en filas).
[::-1] invierte cada fila para lograr la rotación en sentido horario.
Se usa comprensión de listas para crear la nueva matriz de forma elegante.
"""
"""
Problem Name: Rotate Non-Square Matrix 90 Degrees Counterclockwise
Prompt:
You are given a 2D matrix of size m x n. Return a new matrix that represents the original rotated 90 degrees counterclockwise.
"""
def rotate_ccw(matrix):
    # Transponer y luego invertir columnas (filas del resultado)
    return [list(row) for row in zip(*matrix)][::-1]
"""
Rotación 180° (Clockwise o Counterclockwise)
Enunciado estilo CodeSignal
Problem Name: Rotate Non-Square Matrix 180 Degrees
Prompt:
You are given a 2D matrix of size m x n. Return a new matrix that represents the original rotated 180 degrees.
"""
def rotate_180(matrix):
    # Invertir filas y luego invertir cada fila
    return [row[::-1] for row in matrix[::-1]]
"""
¿Cómo identificar qué rotación aplicar?
90° clockwise: zip(*matrix) + [::-1] en filas
90° counterclockwise: zip(*matrix) + [::-1] en columnas
180°: invertir filas y luego invertir cada fila
"""
