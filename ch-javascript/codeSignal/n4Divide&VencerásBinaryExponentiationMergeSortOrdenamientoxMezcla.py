"""
Problema: Ordenar un array de forma eficiente. 
Divide: Rompe el array en dos mitades hasta que solo queden elementos individuales (que por definición están ordenados). 
Conquer (Vencer): Ordena cada sub-array recursivamente. 
Combine (Combinar): Mezcla los sub-arrays ordenados para producir el array final ordenado. 
Condicionales en una sola línea: result.append(...) con if-else en línea.
Incrementos inteligentes: i += left[i] < right[j] es una forma elegante de decir "si se eligió left[i], avanza i".
Nombres más cortos pero claros: left, right, mid son estándar en algoritmos de divide y vencerás.

"""
def merge_sort(arr):
    # Caso base: listas de 0 o 1 elemento ya están ordenadas
    if len(arr) <= 1:
        return arr
    # DIVIDE
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # COMBINA
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Mezcla ordenada de las dos mitades
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] < right[j] else right[j])
        i += left[i] < right[j]
        j += left[i] >= right[j]

    # Agrega lo que queda de cada mitad
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(arr))  # Salida: [5, 6, 7, 11, 12, 13]

"""
Problema: Exponenciación Rápida (Binary Exponentiation) 
Calcula x^n  (elevar  x  a la potencia  n ) de manera eficiente. La forma de fuerza bruta toma   O(n)  tiempo. Queremos una solución Divide and Conquer en   O( n) . 
La clave para la optimización   O( n)  es la división. ¿Cómo puedes dividir el problema de  x^n  en subproblemas, dependiendo de si  n  es par o impar? 
Si  n  es par ( n = 2k ): 
  x^n = x^{2k} = (x^k)^2   
Si  n  es impar ( n = 2k + 1 ): 
  x^n = x^{2k+1} = x * x^{2k} = x * (x^k)^2   

Este tipo de problema suele aparecer como parte de algoritmos de modular exponentiation o algoritmos criptográficos.
Si el problema incluye modulo (mod m), puedes modificar la línea final así:
return (half * half) % m if n % 2 == 0 else (x * half * half) % m
"""
def power(x, n):
    """
    Calcula x elevado a la potencia n usando exponenciación rápida.
    Complejidad: O(log n)
    """
    if n == 0:
        return 1
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else x * half * half

# Test
print(f"2^10 = {power(2, 10)}")  # 1024
print(f"3^5 = {power(3, 5)}")    # 243
""""
¿Y si n -el exponente- es negativo?
"""
def power(x, n):
    """
    Calcula x^n usando exponenciación rápida.
    Soporta exponentes negativos.
    """
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else x * half * half

# Test
print(f"2^-3 = {power(2, -3)}")  # 0.125
