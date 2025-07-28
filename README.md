# Alura
Este es un repositorio para resolver un conjunto de retos de Oracle One
El seguimiento del progreso de los mismos se encuentra en
Trello: https://trello.com/invite/b/68853c02d473357c87bc5124/ATTIe086da395db22670d83a8bf8e98546c6DA2EBC56/challenge-amigo-secreto

# README - Gestor de Amigos con Sorteo Aleatorio

## Descripción del Proyecto
Este proyecto es una aplicación web simple que permite a los usuarios gestionar una lista de amigos y seleccionar un amigo al azar mediante un sorteo. La aplicación está desarrollada con HTML, CSS y JavaScript, y su principal objetivo es demostrar habilidades en lógica de programación, manipulación del DOM y manejo de eventos.

## Características principales
- Agregar amigos a la lista mediante un formulario
- Validación de entrada para evitar campos vacíos
- Visualización de la lista de amigos actualizada en tiempo real
- Función para seleccionar un amigo al azar de la lista
- Interfaz intuitiva y fácil de usar

## Instalación y Configuración
No se requiere instalación compleja. Solo sigue estos pasos:

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

2. Abre el archivo `index.html` en tu navegador web (preferiblemente Chrome, Firefox o Edge).

## Dependencias
Este proyecto no requiere dependencias externas. Todo el código está implementado con:
- HTML5
- CSS3
- JavaScript Vanilla (ES6)

## Uso
1. **Agregar un amigo**:
   - Escribe el nombre de un amigo en el campo de texto
   - Haz clic en "Agregar Amigo"
   - Verás el nombre añadido a la lista de amigos

2. **Realizar un sorteo**:
   - Cuando tengas varios amigos en la lista
   - Haz clic en "Sortear Amigo"
   - Verás un nombre seleccionado aleatoriamente

## Estructura de Archivos
```
proyecto/
├── index.html         # Archivo principal HTML
├── style.css          # Estilos CSS
├── script.js          # Lógica JavaScript
└── README.md          # Este archivo
```


## Posibles Problemas y Soluciones
1. **Problema**: Al agregar un amigo, no aparece en la lista  
   **Solución**: Verifica que el elemento `<ul>` tenga el ID "listaAmigos"

2. **Problema**: El sorteo no funciona y muestra un error en consola  
   **Solución**: Asegúrate de que la función `amigoAleatorio()` esté correctamente enlazada al botón correspondiente

3. **Problema**: Se pueden agregar nombres vacíos  
   **Solución**: La validación actual evita esto, pero si ocurre, verifica que no haya espacios en blanco usando `trim()`

4. **Problema**: La lista se duplica al agregar nuevos amigos  
   **Solución**: La función `mostrarAmigos()` ya limpia la lista antes de agregar elementos, verifica su implementación

## Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue estos pasos:
1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcion`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

## Licencia
Este proyecto está licenciado bajo la bendición de Dios.

---

**Nota**: Para usar esta aplicación, simplemente abre el archivo `index.html` en tu navegador. El código está diseñado para ejecutarse completamente en el lado del cliente sin necesidad de servidores adicionales.

