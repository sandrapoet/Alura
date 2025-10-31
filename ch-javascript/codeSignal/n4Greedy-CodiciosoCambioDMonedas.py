"""
Cambio de Monedas (Canadá) 
Problema: Dar la menor cantidad de monedas (25, 10, 5, 1 centavo) para un valor dado. 
Estrategia Greedy: En cada paso, elige la moneda de mayor valor que sea menor o igual al resto del cambio. 
Decisión Local: La mejor moneda disponible. 
Óptimo Global: La menor cantidad de monedas. 
Usa divmod(valor, moneda) para obtener cuántas monedas caben (divmod devuelve (cociente, residuo)).
Usa asignación dentro de la expresión (valor := valor % moneda) para actualizar el valor restante.
Usa sum() con una expresión generadora, lo que es más eficiente que crear listas intermedias.
Usa tupla inmutable (25, 10, 5, 1) como default para evitar problemas con listas mutables.
"""
def cambio_greedy(valor, monedas=(25, 10, 5, 1)):
    """
    Devuelve la cantidad mínima de monedas necesarias para un valor dado.
    Monedas disponibles: 25¢, 10¢, 5¢, 1¢
    """
    return sum(divmod(valor := valor % moneda, moneda)[0] for moneda in monedas if valor >= moneda)
"""
¿Y si quieres ver cuántas monedas de cada tipo?
"""
def cambio_detallado(valor, monedas=(25, 10, 5, 1)):
    resultado = {}
    for moneda in monedas:
        cantidad, valor = divmod(valor, moneda)
        if cantidad:
            resultado[moneda] = cantidad
    return resultado

# Ejemplo
print(cambio_detallado(48))  # Output: {25: 1, 10: 2, 1: 3}

