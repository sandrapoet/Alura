from collections import defaultdict
def solution(numbers):
    # casos border!!
    if not numbers:
        return 0
    
    cuantos = defaultdict(int)
    answer = 0
    
 # Paso 1: Contar la frecuencia de todos los elementos O(n)
    for element in numbers:
        cuantos[element] += 1
 
 # Paso 2: Iterar sobre las posibles potencias de 2 O(nx21) que la suma pueda alcanzar.y buscar su complemento para cada potencia
    for element in cuantos.keys(): # 
        for exp in range(21): # Cubre hasta 2^20 (2,097,152)
            potencia = (1 << exp) # (1 << k) es 2^k + rapido que 2**exp
 
 # Calcular el complemento: complemento = potencia - elemento evaluado del arreglo
            complemento = potencia - element
 
 # Evitar doble conteo: solo buscar complementos que ya están 'a la derecha' de element en el array (o que son el mismo element)
            if element <= complemento: # Solo contamos si element <= complemento
                if complemento in cuantos: #formula n*(n-1)/2
 # Caso Especial: numbers[i] == numbers[j]
                    if element == complemento:
 # Si un número es igual a su complemento (ej: 2+2=4), solo contamos los pares (i, j) donde i <= j. El número de pares (i, i) es counts[element]. 
 # El número de pares (i, j) con i<j es counts[element] * (counts[element] - 1) / 2
                        n = cuantos[element]
                        answer += n*(n-1) // 2
                    else:
                        answer += cuantos[element] * cuantos[complemento]
    return answer            
# version pitonica
from collections import Counter

def solution(numbers):
    if not numbers:
        return 0
    
    counts = Counter(numbers)
    pairs = 0
    
    for num in counts:
        for exp in range(21):
            power = (1 << exp)
            complement = power - num
            
            if num <= complement and complement in counts:
                if num == complement:
                    n = counts[num]
                    pairs += n * (n - 1) // 2
                else:
                    pairs += counts[num] * counts[complement]
    
    return pairs