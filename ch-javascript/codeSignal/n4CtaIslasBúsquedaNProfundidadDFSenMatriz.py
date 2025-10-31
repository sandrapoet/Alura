"""
El DFS es ideal para problemas de conectividad y exploración de un área completa a partir de un punto. Se implementa típicamente usando recursividad o una pila (Stack). 
💡 Ejercicio Práctico: Conteo de Islas (DFS) 
Problema: Dada una matriz binaria  m * n  que representa un mapa (donde '1' es tierra y '0' es agua), cuenta el número de "islas". Una isla es un grupo de '1's conectados horizontal o verticalmente. 
You are given a 2D binary grid representing a map of '1's (land) and '0's (water). An island is formed by connecting adjacent lands horizontally or vertically. You must return the number of distinct islands in the grid.
Estrategia: 
Iterar sobre cada celda de la matriz. 
Si encuentras una celda de tierra ('1'), has encontrado una nueva isla. Incrementa el contador. 
Llama a una función auxiliar de DFS para "hundir" (cambiar a '0') toda la isla conectada. Esto asegura que no la cuentes de nuevo. 
aplica el enfoque de Divide and Conquer mediante DFS (Depth-First Search). 
"""
def count_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        # Si está fuera de límites o es agua, no hacemos nada
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Marcamos como visitado
        # Exploramos las 4 direcciones
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count

# Test
grid_map = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(f"Número de islas encontradas: {count_islands(grid_map)}")  # Output: 3
"""
Usa tuplas para las direcciones en vez de repetir llamadas
 ¿Cuándo aplicar este patrón?
Cuando te den una matriz binaria y te pidan contar regiones conectadas.
Cuando se mencione "conectividad horizontal o vertical".
Cuando el problema implique recorrer áreas y marcar visitados.
"""
