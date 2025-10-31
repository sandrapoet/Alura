"""
You are given two integers, x and n, where x is the base and n is the exponent. Your task is to compute the value of xnx^nxn efficiently.
The brute-force approach of multiplying x by itself n times takes O(n) time. Instead, implement a divide-and-conquer algorithm that computes the result in O(log n) time.
 Claves para identificar que debes usar Binary Exponentiation:
Te piden eficiencia: mencionan que el enfoque fuerza bruta es lento.
Hay una potencia grande: n puede ser hasta 10^9, lo que hace inviable usar bucles simples.
Mencionan divide and conquer o logarithmic time.
No hay necesidad de calcular cada paso intermedio, solo el resultado final.
ej 1 con módulo (x^n % m)
"""
def power(x, n, m):
    """
    Calcula (x^n) % m usando exponenciación rápida.
    Soporta exponentes negativos.
    """
    if n == 0:
        return 1
    if n < 0:
        x = pow(x, -1, m)  # Inverso modular si n es negativo
        n = -n
    half = power(x, n // 2, m)
    return (half * half) % m if n % 2 == 0 else (x * half * half) % m
  """
   Explicación clave:
pow(x, -1, m): Calcula el inverso modular de x cuando n es negativo. Esto es válido solo si x y m son coprimos.
Se pasa m como argumento para aplicar el módulo en cada paso.
La complejidad sigue siendo O(log n).
print(power(2, 10, 1000))  # Output: 24
print(power(3, -2, 11))    # Output: 5 (porque 3^-2 mod 11 = 1/9 mod 11 = 5)
"""
