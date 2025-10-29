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