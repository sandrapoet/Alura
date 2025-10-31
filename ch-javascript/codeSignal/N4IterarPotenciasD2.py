"""
# **¡Importante!** Para este problema específico, la condición i <= j en un array de números *únicos* simplifica el problema significativamente. 
por eso se puede usar 
from collections import defaultdict 
def solution(numbers): 
    counts = defaultdict(int) 
Si los números *no* fueran únicos, la lógica de conteo del Caso 2 sería esencial. 
Como el problema dice **"unique integers"**, counts[num] y counts[complemento] siempre serán 1. 
esta solucion si trabaja con numeros aun esten repetidos
1. Contar frecuencias del array. 
2. Iterar sobre las frecuencias/elementos. 
3. Para cada elemento, calcular el Complemento (Objetivo - Elemento). 
4. Sumar counts[Complemento]. 
Este patrón de Complemento con Hash Map se aplica a cualquier problema que busque pares con una suma específica
(ya sea constante o, en este caso, una de un conjunto pequeño de constantes, como las potencias de 2). 
"""
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
