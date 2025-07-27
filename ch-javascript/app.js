// El principal objetivo de este desafío es fortalecer tus habilidades en lógica de programación. Aquí deberás desarrollar la lógica para resolver el problema.
let amigos = []
/*
Capturar el valor del campo de entrada: 
Utilizar document.getElementById o document.querySelector para obtener el texto ingresado por el usuario.
Validar la entrada: Implementar una validación para asegurarse de que el campo no esté vacío. 
Si está vacío, mostrar un alert con un mensaje de error: "Por favor, inserte un nombre."
Actualizar el array de amigos: Si el valor es válido, añadirlo al arreglo que almacena los nombre de amigos usando el método.
push().
Limpiar el campo de entrada: Después de añadir el nombre, restablecer el campo de texto a una cadena vacía.
*/
function agregarAmigo(){
    if (document.getElementById("amigo").value === "") {
        alert("Por favor, inserte un nombre.");
    }else {
        amigos.push(document.getElementById("amigo").value);
        document.getElementById("amigo").value = "";
        mostrarAmigos(amigos);
    }
console.log("Amigo agregado: " + amigos[amigos.length - 1]);
    console.log("Lista de amigos actualizada: " + amigos);
}
/*
Crea una función que recorra el array amigos y agregue cada nombre 
como un elemento <li> dentro de una lista HTML. 
Usa innerHTML para limpiar la lista antes de agregar nuevos elementos.

Tareas específicas:

Obtener el elemento de la lista: Utilizar document.getElementById() o document.querySelector() para seleccionar la lista donde se mostrarán los amigos.

Limpiar la lista existente: Establecer lista.innerHTML = "" para asegurarse de que no haya duplicados al actualizar.

Iterar sobre el arreglo: Usa un bucle for para recorrer el arreglo amigos y crear elementos de lista (<li>) para cada título.

Agregar elementos a la lista: Para cada amigo, crear un nuevo elemento de lista.
*/
function mostrarAmigos(amigos) {
    let lista = document.getElementById("listaAmigos");
    lista.innerHTML = ""; // Limpiar la lista antes de agregar nuevos elementos
    for (let i = 0; i < amigos.length; i++) {
        const li = document.createElement("li");
        li.textContent = amigos[i];
        lista.appendChild(li);
        console.log("Desplegando a: " +amigos[i]);
    }
}