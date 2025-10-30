"""
### **Problema: Procesador de Texto Simple**

Dado un string `text` y un entero `k`, tu tarea es procesar el texto de la siguiente manera:

1. **Dividir** el texto en palabras (separadas por espacios)
2. **Para cada palabra:**
   - Si la longitud de la palabra es **mayor que k**, convertirla a **MAYÚSCULAS**
   - Si la longitud de la palabra es **menor que k**, convertirla a **minúsculas**
   - Si la longitud es **exactamente k**, dejarla tal como está
3. **Reconstruir** el string con las palabras procesadas, manteniendo los espacios originales

---

### 📝 **Ejemplos:**

**Ejemplo 1:**
```python
text = "Hello World this is a Test"
k = 4
# Resultado: "HELLO WORLD this is a test"
# Explicación: 
# - "Hello" (5 > 4) → "HELLO"
# - "World" (5 > 4) → "WORLD"  
# - "this" (4 == 4) → "this"
# - "is" (2 < 4) → "is"
# - "a" (1 < 4) → "a"
# - "Test" (4 == 4) → "Test"
```

**Ejemplo 2:**
```python
text = "Programming is fun"
k = 6
# Resultado: "PROGRAMMING is fun"
```
"""
def solution(text, k):
    return ' '.join(
        word.upper() if len(word) > k else 
        word.lower() if len(word) < k else 
        word
        for word in text.split()
    )
