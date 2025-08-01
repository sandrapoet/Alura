import React, { useState, useEffect } from 'react';

function Cronometro() {
  // Estado para el contador
  const [segundos, setSegundos] = useState(0);
  
  // useEffect: ¡El "modo dios" que se activa al montar el componente!
  useEffect(() => {
    // 1. Al iniciar: Creamos un temporizador (como un reloj interno)
    const temporizador = setInterval(() => {
      setSegundos(s => s + 1); // Actualiza el estado cada segundo
    }, 1000);
    
    // 2. Función de LIMPIEZA (componentWillUnmount)
    return () => {
      clearInterval(temporizador); // ¡Destruye el temporizador al salir!
      console.log("¡Componente desmontado! Temporizador eliminado.");
    };
  }, []); // Array vacío = solo se ejecuta al inicio
  
  return (
    <div>
      <h2>⏱️ Tiempo: {segundos} segundos</h2>
      <button onClick={() => setSegundos(0)}>Reiniciar</button>
    </div>
  );
}