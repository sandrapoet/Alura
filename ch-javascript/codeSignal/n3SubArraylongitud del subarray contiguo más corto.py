"""
**Problema:** Dado un array de números `nums` y un `target`, encuentra la **longitud del subarray contiguo más corto** cuya suma sea **mayor o igual que (`>=`)** el `target`.

### 1. ¿Qué es un Subarray (Contiguo)?

Un subarray debe tener elementos que están **uno al lado del otro** en el array original.
Para `nums = [1, 2, 3, 4, 5]`:
*   `[2, 3, 4]` **SÍ** es un subarray.
*   `[1]` **SÍ** es un subarray.
*   `[1, 3, 5]` **NO** es un subarray (porque los elementos no son consecutivos).

### 2. La Condición: `suma >= target`

La mayoría de las veces, este problema no pide una suma *exactamente* igual al target, sino **mayor o igual**. Esto es crucial. Si la suma tuviera que ser exactamente 11, con `nums = [1, 2, 3, 4, 5]`, no habría ninguna solución y el resultado debería ser 0.

### 3. La Meta: La Longitud Mínima

No buscamos la suma, ni el subarray en sí mismo, ni un índice. Buscamos un **número**: la cantidad de elementos que tiene el subarray más corto que cumple la condición.

### Ejemplo 
*   `nums = [1, 2, 3, 4, 5]`
*   `target = 11`

Buscamos subarrays cuya suma sea **>= 11**.
*   `[5]` -> suma = 5 (No cumple)
*   `[4, 5]` -> suma = 9 (No cumple)
*   `[3, 4, 5]` -> suma = 12. **¡Sí cumple! (12 >= 11)**. La longitud de este subarray es **3**.
*   `[2, 3, 4, 5]` -> suma = 14. **¡Sí cumple! (14 >= 11)**. La longitud de este subarray es **4**.
*   `[1, 2, 3, 4, 5]` -> suma = 15. **¡Sí cumple! (15 >= 11)**. La longitud de este subarray es **5**.

Ahora, de todos los subarrays que cumplieron la condición, ¿cuál es el más corto?
*   `[3, 4, 5]` (longitud 3)
*   `[2, 3, 4, 5]` (longitud 4)
*   `[1, 2, 3, 4, 5]` (longitud 5)

El más corto es `[3, 4, 5]`, que tiene una **longitud de 3**.
**Por eso el resultado es 3.**

Restricciones:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
-10^6 <= target <= 10^6
Complejidad esperada: O(n)

### 1. Interpretación de las Restricciones Numéricas
#### `1 <= nums.length <= 10^5`
*   **Significado:** El array `nums` no estará vacío y puede tener hasta 100,000 elementos.
*   **Implicación:** **Este es el dato más importante.** Un array de 100,000 elementos es bastante grande. Un algoritmo ineficiente será demasiado lento. Por ejemplo, si tu solución tiene una complejidad de `O(n²)`, el número de operaciones sería aproximadamente `(10^5)² = 10^10` (diez mil millones). Ninguna plataforma de evaluación te permitirá ejecutar tantas operaciones; te dará un error de "Time Limit Exceeded". Esto te obliga a buscar una solución más inteligente.

#### `-10^4 <= nums[i] <= 10^4`
*   **Significado:** Los números dentro del array pueden ser positivos, negativos o cero. Su valor estará entre -10,000 y 10,000.
*   **Implicación:** **¡ESTO ES CRUCIAL Y CAMBIA TODO!** El hecho de que haya **números negativos** invalida la técnica más común para este tipo de problemas (la "ventana deslizante" o "sliding window" simple).
    *   **¿Por qué?** La ventana deslizante simple funciona porque al agregar un número positivo a la derecha, la suma siempre aumenta, y al quitar un número positivo de la izquierda, la suma siempre disminuye. Es un comportamiento predecible (monótono).
    *   Con números negativos, esta lógica se rompe. Al agregar un número negativo, ¡la suma de la ventana disminuye! Al quitar un número negativo, ¡la suma aumenta! El comportamiento ya no es predecible, por lo que se necesita una técnica más avanzada.

#### `-10^6 <= target <= 10^6`
*   **Significado:** El `target` también puede ser positivo, negativo o cero.
*   **Implicación:** Esto es menos crítico para la lógica del algoritmo, pero confirma que debes estar preparado para manejar todo tipo de escenarios (buscar una suma negativa, por ejemplo).

---

### 2. Interpretación de la Complejidad Esperada: `O(n)`

*   **Significado:** La complejidad `O(n)` se conoce como **Tiempo Lineal**. Significa que tu algoritmo debe resolver el problema recorriendo el array `nums` una sola vez (o un número constante de veces, como dos o tres pasadas, pero no bucles anidados).
*   **Implicación:** Esto confirma lo que sospechábamos por el `nums.length`.
    *   **Prohibido `O(n²)`:** No puedes usar un bucle anidado que, para cada elemento, vuelva a recorrer una gran parte del array. Esto es lo que haría una solución de "fuerza bruta" (probar todos los subarrays posibles).
    *   **Obligatorio `O(n)`:** Necesitas un algoritmo que procese cada elemento y mantenga alguna información útil en memoria para tomar decisiones rápidas, sin tener que volver a mirar elementos pasados una y otra vez.

---

### Conclusión y Estrategia a Seguir

Juntando todas las pistas:

1.  **Necesitas un algoritmo `O(n)`** porque el array es muy grande.
2.  **No puedes usar la ventana deslizante simple** porque hay números negativos.

Esto te empuja hacia una solución más robusta que sí funciona con números negativos. La técnica estándar para este tipo de problema (encontrar subarrays que cumplan una condición de suma en `O(n)`) es usar **Sumas Acumuladas (Prefix Sums)** en combinación con alguna estructura de datos inteligente.

**La idea general del algoritmo `O(n)` para este caso es:**

1.  **Calcular las Sumas Acumuladas:** Recorres el array una vez para crear un array de "sumas prefijo", donde `prefix_sum[i]` es la suma de todos los elementos desde el inicio hasta el índice `i`.
2.  **Usar una Estructura de Datos Auxiliar:** Mientras calculas las sumas, usas una estructura de datos (para este problema específico, una **cola monotónica o `deque`** es la solución óptima) para mantener un registro de las sumas anteriores.
3.  **Encontrar la Longitud Mínima:** En cada paso, usas la suma actual y la estructura de datos para encontrar eficientemente si existe un subarray anterior que, al "restarlo" de tu suma actual, cumpla la condición `suma >= target`. Gracias a la estructura, puedes encontrar la longitud mínima en tiempo casi constante en cada paso.

En resumen: **Las restricciones te dicen que una solución simple no pasará, y la presencia de números negativos te obliga a usar una técnica avanzada como "Sumas Acumuladas + Deque" para lograr la eficiencia `O(n)` requerida.**
"""
def solution(nums, target):
    """
    Encuentra la longitud del subarray contiguo más corto con suma exacta igual a target.
    
    Args:
        nums: Lista de enteros
        target: Suma objetivo
    
    Returns:
        int: Longitud mínima del subarray, o 0 si no existe
    """
    prefx_sum = {0:1}
    suma = 0
    cont = 0
    for num in nums:
        suma += num
        if(suma-target) in prefx_sum:
            cont += prefx_sum[suma-target]
        prefx_sum[suma]= prefx_sum.get(suma,0)+1
    print(prefx_sum)
    return cont

# Caso 4: Números negativos
nums = [-1, 4, 2, -3, 1, 6]
target = 3
print(solution(nums,target))
# Resultado: 1 (el elemento 3)

# Caso 5: Array vacío
nums = []
target = 5
print(solution(nums,target))
# Resultado: 0

# Caso 6: Target al inicio
nums = [5, 1, 1, 1, 1]
target = 5
print(solution(nums,target))
# Resultado: 1
