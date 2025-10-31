"""
Diagonal Matrix Traversal
You are given a 2D matrix of size m x n. Your task is to return all elements of the matrix in diagonal order, starting from the top-left corner. The traversal should alternate directions:
First diagonal: up-right
Second diagonal: down-left
Third diagonal: up-right
"""
def diagonal_traversal(matrix):
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    for d in range(m + n - 1):
        intermediate = []

        # Determinar los límites de la diagonal
        r = 0 if d < n else d - n + 1
        c = d if d < n else n - 1

        # Recolectar elementos de la diagonal
        while r < m and c >= 0:
            intermediate.append(matrix[r][c])
            r += 1
            c -= 1

        # Alternar dirección
        if d % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)

    return result

# Test
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(diagonal_traversal(matrix))  # Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]

"""
¿Cómo identificar este patrón?
El problema menciona diagonal traversal o zigzag diagonales.
Se requiere recorrer la matriz en orden alternado por diagonales.
Se habla de sumas de índices constantes: en diagonales, los elementos tienen la propiedad de que row + col = constante.
"""
