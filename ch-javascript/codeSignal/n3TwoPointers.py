"""
🧩 Problema Módulo 3 - Búsqueda en Matriz Ordenada
Problema: Encontrar Elemento en Matriz Ordenada
Dada una matriz matrix de tamaño m x n donde:
Cada fila está ordenada de izquierda a derecha
Cada columna está ordenada de arriba a abajo
No hay duplicados
Implementa una función que determine si un target existe en la matriz.
Restricción: Complejidad temporal debe ser O(m + n), no O(m × n)
"""
def solution(matrix, target):
    """
    Busca un 'target' en una matriz ordenada por filas y columnas.
    La complejidad es O(m + n).
    """
    # Manejar caso de matriz vacía
    if not matrix or not matrix[0]:
        return False

    # Obtener las dimensiones de la matriz
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Empezar en la esquina superior derecha
    current_row = 0
    current_col = cols - 1
    
    # Mientras nuestros punteros estén dentro de la matriz
    while current_row < rows and current_col >= 0:
        current_element = matrix[current_row][current_col]
        
        if current_element == target:
            return True  
        elif target < current_element:
            # El target es más pequeño, no puede estar en esta columna.
            # Moverse a la izquierda.
            current_col -= 1
        else: # El target es más grande, no puede estar en esta fila.
            # Moverse hacia abajo.
            current_row += 1
            
    # Si el bucle termina, es que nos salimos de la matriz sin encontrarlo.
    return False

matrix = [
    [1,  4,  7,  11],
    [2,  5,  8,  12],
    [3,  6,  9,  16],
    [10, 13, 14, 17]
]

print(f"Buscando el 9: {solution(matrix, 9)}")
print(f"Buscando el 15: {solution(matrix, 15)}")