def encontrar_posicion_caida(campo, figura):
    """
    Encuentra la posición de columna para soltar una figura que resulte
    en al menos una fila completa en el campo de juego.
    con funciones auxiliares y expresiones generadoras.
    """
    altura_campo, ancho_campo = len(campo), len(campo[0])
    tam_figura = len(figura)

    def _hay_colision(fila, col):
        """Verifica si la figura colisiona con el campo en una posición dada."""
        return any(
            figura[r][c] == 1 and campo[fila + r][col + c] == 1
            for r in range(tam_figura)
            for c in range(tam_figura)
        )

    # Probar cada columna de inicio posible
    for col_inicio in range(ancho_campo - tam_figura + 1):
        
        # 1. Encontrar la fila donde la figura se detiene
        fila_detenida = -1
        # Simula la caída de la figura desde arriba
        for fila in range(altura_campo - tam_figura + 1):
            if _hay_colision(fila, col_inicio):
                fila_detenida = fila - 1
                break
        else:
            # Si el bucle termina sin 'break', la figura llega al fondo
            fila_detenida = altura_campo - tam_figura

        # Si la figura colisiona desde el inicio, esta columna no es válida
        if fila_detenida < 0:
            continue

        # 2. Crear un estado temporal del campo con la figura ya colocada
        campo_temporal = [row[:] for row in campo]
        for r in range(tam_figura):
            for c in range(tam_figura):
                if figura[r][c] == 1:
                    campo_temporal[fila_detenida + r][col_inicio + c] = 1
        
        # 3. Verificar si alguna de las filas afectadas ahora está completa
        for r in range(tam_figura):
            fila_afectada_idx = fila_detenida + r
            # all() es perfecto para verificar si todos los elementos son verdaderos (o 1 en este caso)
            if all(celda == 1 for celda in campo_temporal[fila_afectada_idx]):
                return col_inicio # ¡Éxito! Encontramos la columna.
    
    return -1 # Si se prueban todas las columnas y no hay solución

# Test (mismo que el original)
campo = [
    [0, 0, 0],
    [0, 0, 0], 
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
]

figura = [
    [0, 0, 1],
    [0, 1, 1],
    [0, 0, 1]
]

print(encontrar_posicion_caida_pythonic(campo, figura))  # Sigue imprimiendo 0
