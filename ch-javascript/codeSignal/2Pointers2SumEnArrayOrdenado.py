"""
Problema: Encontrar un par de números en un array ordenado que sume a un target específico. 
Mecánica: 
Un puntero (left) comienza en el inicio del array. 
El otro puntero (right) comienza en el final del array. 
En cada paso, comparas la condición (ej: arr[left] + arr[right] con el objetivo). 
Si la condición es muy grande, mueves el puntero right hacia la izquierda (buscando un número menor). 
Si la condición es muy pequeña, mueves el puntero left hacia la derecha (buscando un número mayor). 
"""
def find_two_sum(arr, target):
    """
    Encuentra un par de números que suman target.
    Retorna: (valor1, valor2) o None si no existe.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        s = arr[left] + arr[right]
        
        if s == target:
            return (arr[left], arr[right])
        
        left, right = (left + 1, right) if s < target else (left, right - 1)
    return None

# Si quieres retornar índices en vez de valores:
def find_two_sum_indices(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        s = arr[left] + arr[right]
        
        if s == target:
            return (left, right)  # 👈 Retorna índices
        
        left, right = (left + 1, right) if s < target else (left, right - 1)
    return None

print(find_two_sum_indices([-2, 1, 3, 5, 8], 6))  # (1, 3)

def find_all_two_sum(arr, target):
    """Encuentra TODOS los pares que suman target."""
    left, right = 0, len(arr) - 1
    pairs = []
    
    while left < right:
        s = arr[left] + arr[right]
        
        if s == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1
    return pairs

# Test
print(find_all_two_sum([1, 2, 3, 4, 5, 6], 7))
# [(1, 6), (2, 5), (3, 4)]
