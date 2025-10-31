"""
You are given a 2D matrix of size m x n. Your task is to return all elements of the matrix in zigzag order, starting from the top-left corner. The zigzag pattern alternates direction on each row:
Row 0: left → right
Row 1: right → left
Row 2: left → right
Row 3: right → left
"""
def zigzag_traversal(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    for i, row in enumerate(matrix):
        # Si la fila es par, recorremos de izquierda a derecha
        # Si es impar, recorremos de derecha a izquierda
        result.extend(row if i % 2 == 0 else row[::-1])
    return result

# Test
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(zigzag_traversal(matrix))  # Output: [1, 2, 3, 6, 5, 4, 7, 8, 9]

