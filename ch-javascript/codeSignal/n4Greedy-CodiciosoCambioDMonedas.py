"""
Cambio de Monedas (Canadá) 
Problema: Dar la menor cantidad de monedas (25, 10, 5, 1 centavo) para un valor dado. 
Estrategia Greedy: En cada paso, elige la moneda de mayor valor que sea menor o igual al resto del cambio. 
Decisión Local: La mejor moneda disponible. 
Óptimo Global: La menor cantidad de monedas. 
Usa divmod(valor, moneda) para obtener cuántas monedas caben (divmod devuelve (cociente, residuo)).
Usa asignación dentro de la expresión (valor := valor % moneda) para actualizar el valor restante.
Usa sum() con una expresión generadora, lo que es más eficiente que crear listas intermedias.
Usa tupla inmutable (25, 10, 5, 1) como default para evitar problemas con listas mutables.
"""
def cambio_greedy(valor, monedas=(25, 10, 5, 1)):
    """
    Devuelve la cantidad mínima de monedas necesarias para un valor dado.
    Monedas disponibles: 25¢, 10¢, 5¢, 1¢
    """
    return sum(divmod(valor := valor % moneda, moneda)[0] for moneda in monedas if valor >= moneda)
"""
¿Y si quieres ver cuántas monedas de cada tipo?
"""
def cambio_detallado(valor, monedas=(25, 10, 5, 1)):
    resultado = {}
    for moneda in monedas:
        cantidad, valor = divmod(valor, moneda)
        if cantidad:
            resultado[moneda] = cantidad
    return resultado

# Ejemplo
print(cambio_detallado(48))  # Output: {25: 1, 10: 2, 1: 3}

"""
Problema: Maximum Non-Overlapping Activities Cobertura Mínima de Tramos (Interval Scheduling) 
Tienes una serie de actividades, cada una con una hora de inicio y una hora de finalización. Quieres saber el máximo número de actividades que puedes realizar, asumiendo que solo puedes hacer una actividad a la vez (no pueden superponerse). 
Actividad     Inicio         Fin 
A             0                6 
B             1                4 
C             3                5 
.................. 
¿Cómo saber que es un problema greedy?
Te piden maximizar algo (número de actividades).
Hay una restricción de solapamiento.
Las actividades tienen inicio y fin, lo que sugiere ordenarlas.
La solución óptima se logra eligiendo localmente la mejor opción (la que termina antes).
Solución Algoritmo Greedy 
La decisión localmente óptima para el problema de Cobertura Mínima de Tramos (Interval Scheduling) es la opción 3: 
✅ Elegir la actividad que termina más temprano. 
Razón: Al elegir la actividad que termina antes, maximizas el tiempo disponible para comenzar la próxima actividad. Esto deja la ventana más grande posible para futuras elecciones, lo que garantiza el óptimo global (el máximo número de actividades). 
"""
def max_activities(activities):
    # Ordenar por hora de finalización (criterio greedy)
    activities.sort(key=lambda x: x[1])

    selected = []
    last_end = -1

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return len(selected), selected

# Test
activities = [(0, 6), (1, 4), (3, 5), (5, 7), (8, 9), (5, 9)]
count, selected = max_activities(activities)
print(f"Máximo número de actividades: {count}")
print("Actividades seleccionadas:", selected)
"""
Tip para entrevistas y exámenes
Este problema es un clásico de algoritmos greedy.
Siempre ordena por el final, no por el inicio.
Si te piden solo el número, puedes evitar guardar la lista selected para ahorrar memoria.
"""

"""
Minimum Number of Meeting Rooms
You are given a list of meeting time intervals represented as pairs of start and end times: [[start1, end1], [start2, end2], ...]. Your task is to determine the minimum number of meeting rooms required so that all meetings can take place without overlapping.
Solución Pythonic con Heap (Divide & Conquer + Greedy)
Ordenamos por hora de inicio para procesar las reuniones en orden.
Usamos un heap (min-heap) para mantener las salas ocupadas por hora de finalización.
Si la reunión actual puede usar una sala que ya terminó, la reutilizamos.
Si no, necesitamos una sala nueva.
Al final, el número de salas activas es el tamaño del heap.
"""
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # Ordenamos las reuniones por hora de inicio
    intervals.sort(key=lambda x: x[0])

    # Usamos un heap para llevar el seguimiento de las salas ocupadas (por hora de finalización)
    rooms = []

    for start, end in intervals:
        # Si la sala más temprana está libre antes de que empiece esta reunión, la reutilizamos
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)  # Liberamos la sala

        # Asignamos una sala (nueva o reutilizada)
        heapq.heappush(rooms, end)

    # El número de salas necesarias es el tamaño del heap
    return len(rooms)

# Test
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # Output: 2
print(min_meeting_rooms([[7, 10], [2, 4]]))             # Output: 1
"""
¿Cuándo aplicar esta técnica?
Cuando te pidan agendar actividades sin solapamientos.
Cuando el problema mencione recursos limitados (salas, máquinas, etc.).
Cuando haya intervalos de tiempo y se busque optimizar uso de recursos.
"""
