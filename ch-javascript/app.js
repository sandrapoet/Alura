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
    if (amigos[amigos.length - 1] === "") {
        alert("Por favor, inserte un nombre.");
    }else {
        amigos.push(document.getElementById("amigo").value);
        document.getElementById("amigo").value = "";
        console.log(amigos);
    }
}