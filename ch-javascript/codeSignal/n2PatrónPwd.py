"""
🧩 Módulo 2 - Data Manipulation
📋 Características del módulo:
Tiempo estimado: 15 minutos
Líneas de código esperadas: 10-20
Enfoque: Manipulación de estructuras de datos más complejas
Puede incluir: 1-2 loops anidados, combinación de 3-5 conceptos básicos
🎯 Problema: Validador de Patrón de Contraseña
Dado un string password y un patrón pattern que contiene solo los caracteres 'L' (letra), 'D' (dígito) y 'S' (símbolo), tu tarea es verificar si el password coincide con el patrón.

Reglas:
'L' en el patrón debe corresponder a una letra (a-z, A-Z)
'D' en el patrón debe corresponder a un dígito (0-9)
'S' en el patrón debe corresponder a un símbolo (cualquier carácter que no sea letra ni dígito)
El password y el patrón deben tener exactamente la misma longitud
Retorna: True si el password coincide con el patrón, False en caso contrario.
"""
def solution(password, pattern):
    if len(password) != len(pattern):
        return False
    
    checks = {
        'L': str.isalpha,
        'D': str.isdigit,
        'S': lambda c: not c.isalnum()
    }
    
    return all(checks[p](c) for c, p in zip(password, pattern))

"""
You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.
– The pattern and substring are equal in length.
– Where there is a 0 in the pattern, there is a vowel in the substring. 
– Where there is a 1 in the pattern, there is a consonant in the substring. 
"""
def solution1(password, pattern):
    if len(password) != len(pattern):
        return False
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    is_vowel = lambda c: c.lower() in vowels
    
    checks = {
        '0': is_vowel,
        '1': lambda c: not is_vowel(c)
    }
    
    return all(checks[p](c) for c, p in zip(password, pattern))

print(solution1("amazing","010"))
