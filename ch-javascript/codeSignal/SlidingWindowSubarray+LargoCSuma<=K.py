"""
Punteros de Deslizamiento (Sliding Window / Same Direction Pointers) 
Uso: Típico para subarrays, subcadenas o rangos de tamaño variable que deben cumplir una condición (ej: el subarray más largo con suma <= K, o la subcadena más corta con todos los caracteres únicos). 
Problema: Encontrar la longitud del subarray contiguo más largo cuya suma es menor o igual a K. 
Mecánica: 
Ambos punteros (start y end) comienzan en el inicio del array. 
El puntero end avanza para expandir la ventana, incluyendo un nuevo elemento. 
Cuando la ventana viola la condición (ej: la suma excede el límite), el puntero start avanza para contraer la ventana hasta que la condición se restablece. 
Se registra la mejor solución encontrada en cada paso. 
"""
    """
    Encuentra la longitud del subarray contiguo más largo cuya suma ≤ k.
    Args:
        arr: Lista de enteros (pueden ser negativos)
        k: Suma máxima permitida
    Returns:
        LONGITUD del subarray más largo
    Complejidad:
        Tiempo: O(n)
        Espacio: O(1)
    """
def longest_subarray_sum_less_than_k(arr, k):
    if not arr:
        return 0
    
    start = max_length = current_sum = 0
    
    for end, num in enumerate(arr):
        current_sum += num
        
        # Contraer ventana si la suma excede k
        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1
        
        max_length = max(max_length, end - start + 1)
    return max_length

# Tests
assert longest_subarray_sum_less_than_k([3, 1, 2, 7, 4, 2, 1, 1], 8) == 4
assert longest_subarray_sum_less_than_k([1, 2, 3, 4, 5], 10) == 4  # [1,2,3,4]
assert longest_subarray_sum_less_than_k([], 5) == 0
assert longest_subarray_sum_less_than_k([10], 5) == 0
print("✅ Todos los tests pasaron")

"""
retornar también el subarray
"""
def longest_subarray_sum_less_than_k(arr, k):
    """Retorna la longitud Y el subarray."""
    if not arr:
        return 0, []
    
    start = max_length = current_sum = 0
    best_start = best_end = 0
    
    for end, num in enumerate(arr):
        current_sum += num
        
        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1
        
        if end - start + 1 > max_length:
            max_length = end - start + 1
            best_start, best_end = start, end
    return max_length, arr[best_start:best_end + 1]

# Test
length, subarray = longest_subarray_sum_less_than_k([3, 1, 2, 7, 4, 2, 1, 1], 8)
print(f"Longitud: {length}, Subarray: {subarray}")
# Longitud: 4, Subarray: [4, 2, 1, 1]
