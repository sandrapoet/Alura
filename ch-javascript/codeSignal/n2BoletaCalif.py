"""
Problema: Procesador de Datos de Estudiantes
Tienes una lista de strings students donde cada string representa la información de un estudiante en el formato:
"nombre:nota1,nota2,nota3;edad"

Ejemplo: "Ana:85,90,78;20"
Tu tarea es:
Parsear cada string para extraer: nombre, lista de notas, y edad
Calcular el promedio de notas para cada estudiante
Filtrar solo los estudiantes con promedio ≥ 80 y edad ≥ 18
Ordenar los estudiantes resultantes por promedio (descendente)
Devolver una lista de strings en formato: "Nombre: Promedio"

📝 Ejemplo:
python
students = [
    "Ana:85,90,78;20",
    "Luis:70,65,60;17",      # Edad < 18 → excluido
    "Maria:95,88,92;19",
    "Carlos:75,80,85;21",    # Promedio < 80 → excluido
    "Elena:100,95,98;22"
]

# Resultado esperado:
["Elena: 97.67", "Maria: 91.67", "Ana: 84.33"]
"""
def solution(students):
    def parse(s):
        nombre, resto = s.split(':')
        notas_str, edad = resto.split(';')
        notas = list(map(int, notas_str.split(',')))
        return {
            'nombre': nombre,
            'edad': int(edad),
            'promedio': sum(notas) / len(notas)
        }
    
    estudiantes = [parse(s) for s in students]
    filtrados = [e for e in estudiantes if e['promedio'] >= 80 and e['edad'] >= 18]
    filtrados.sort(key=lambda e: e['promedio'], reverse=True)
    
    return [f"{e['nombre']}: {e['promedio']:.2f}" for e in filtrados] 

test = [
    "Ana:85,90,78;20",
    "Luis:70,65,60;17",      # Edad < 18 → excluido
    "Maria:95,88,92;19",
    "Carlos:75,80,85;21",    # Promedio < 80 → excluido
    "Elena:100,95,98;22"
]

print(solution(test))
