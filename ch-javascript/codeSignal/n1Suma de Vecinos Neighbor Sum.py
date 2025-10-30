"""
Se te da un array de enteros. Tu tarea es devolver un nuevo array donde cada elemento en el índice i es la suma del elemento en el índice i-1, el elemento en el índice i, y el elemento en el índice i+1 del array original.
Para los elementos en los extremos del array (el primero y el último), si un vecino no existe (por ejemplo, el vecino izquierdo del primer elemento o el vecino derecho del último), debes considerarlo como 0.
Ejemplo
Para a = [1, 2, 3], el resultado debería ser solution(a) = [3, 6, 5].
Para el primer elemento 1 (en el índice 0):
El vecino izquierdo no existe, así que es 0.
El elemento actual es 1.
El vecino derecho es 2.
Suma: 0 + 1 + 2 = 3.
Utiliza una técnica llamada "padding" (relleno). Crea un nuevo array temporal (padded) que es el original con un 0 al principio y otro al final.
"""
def solution(a):
    padded = [0] + a + [0]
    return [padded[i] + padded[i+1] + padded[i+2] for i in range(len(a))]
