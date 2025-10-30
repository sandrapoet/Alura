"""
## 🧩 **Módulo 3 - Implementation Efficiency**
- **Puede incluir:** 
  - Arrays multidimensionales
  - Hashmaps/diccionarios para optimización
  - División en subtareas/funciones
  - Manipulación eficiente de datos

## 🎯 **Problema: Analizador de Transacciones Bancarias**
Tienes una lista de transacciones bancarias donde cada transacción es un string en formato:
`"fecha;cliente_id;monto;tipo"`

**Donde:**
- `fecha`: YYYY-MM-DD
- `cliente_id`: string único
- `monto`: número entero (puede ser positivo o negativo)
- `tipo`: "DEPOSITO" o "RETIRO"

**Tu tarea:** Encontrar **todos los clientes sospechosos** basado en estas reglas:
1. **Regla de Monto Grande:** Cualquier transacción ≥ 10,000
2. **Regla de Frecuencia:** Más de 5 transacciones en un mismo día
3. **Regla de Secuencia Rápida:** 3 o más transacciones consecutivas dentro de 10 minutos (mismo cliente)

**Retorna:** Lista ordenada alfabéticamente de IDs de clientes sospechosos (sin duplicados)
---

### 📝 **Ejemplo:**

```python
transactions = [
    "2024-01-15;A001;5000;DEPOSITO",
    "2024-01-15;A001;12000;DEPOSITO",      # Regla 1: Monto grande
    "2024-01-15;A002;200;DEPOSITO",
    "2024-01-15;A002;300;RETIRO", 
    "2024-01-15;A002;400;DEPOSITO",
    "2024-01-15;A002;500;RETIRO",
    "2024-01-15;A002;600;DEPOSITO",        # Regla 2: 5+ transacciones mismo día
    "2024-01-15;A002;700;RETIRO",
    "2024-01-15;A003;100;DEPOSITO",
    "2024-01-15 10:05;A003;200;RETIRO",    # Asumimos timestamps para regla 3
    "2024-01-15 10:08;A003;300;DEPOSITO",  # 3 transacciones en < 10 min
    "2024-01-15 10:12;A003;400;RETIRO"
]

# Resultado esperado: ["A001", "A002", "A003"]

"""

from datetime import datetime, timedelta
from collections import defaultdict, Counter

def solution(transactions):
    fraud = set()
    txs_por_cliente = defaultdict(lambda: {'todas': [], 'con_hora': []})
    
    # Parse y categorizar en un solo paso
    for tx_str in transactions:
        date, id, monto, tipo = tx_str.split(';')
        monto = float(monto)
        
        # Regla 1: Monto grande
        if monto >= 10000:
            fraud.add(id)
        
        tx_info = {'date': date, 'monto': monto}
        txs_por_cliente[id]['todas'].append(tx_info)
        
        if ' ' in date:
            txs_por_cliente[id]['con_hora'].append(
                datetime.strptime(date, "%Y-%m-%d %H:%M")
            )
    
    # Verificar reglas 2 y 3
    for cliente_id, data in txs_por_cliente.items():
        # Regla 2: Más de 5 transacciones en un mismo día
        dias = [tx['date'][:10] for tx in data['todas']]
        conteo_dias = Counter(dias) # numero de txs por dia para un mismo cliente 
        #print(conteo_dias)
        if any(count > 5 for count in conteo_dias.values()):
            fraud.add(cliente_id)
        
        # Regla 3: 3+ transacciones en ventana de 10 minutos
        timestamps = sorted(data['con_hora'])
        for i in range(len(timestamps) - 2):
            if timestamps[i+2] - timestamps[i] <= timedelta(minutes=10):
                fraud.add(cliente_id)
                break
    
    return sorted(fraud)

transactions = [
    "2024-01-15;A001;5000;DEPOSITO",
    "2024-01-15;A001;12000;DEPOSITO",      # Regla 1: Monto grande
    "2024-01-15;A002;200;DEPOSITO",
    "2024-01-15;A002;300;RETIRO", 
    "2024-01-15;A002;400;DEPOSITO",
    "2024-01-15;A002;500;RETIRO",
    "2024-01-15;A002;600;DEPOSITO",        # Regla 2: 5+ transacciones mismo día
    "2024-01-15;A002;700;RETIRO",
    "2024-01-15;A003;100;DEPOSITO",
    "2024-01-15 10:05;A003;200;RETIRO",    # Asumimos timestamps para regla 3
    "2024-01-15 10:08;A003;300;DEPOSITO",  # 3 transacciones en < 10 min
    "2024-01-15 10:12;A003;400;RETIRO"
]
print(solution(transactions))


"""
python
# En la regla 3, verificar si hay suficientes timestamps
timestamps = sorted(data['con_hora'])
if len(timestamps) >= 3:
    for i in range(len(timestamps) - 2):
        if timestamps[i+2] - timestamps[i] <= timedelta(minutes=10):
            fraud.add(cliente_id)
            break

"""
