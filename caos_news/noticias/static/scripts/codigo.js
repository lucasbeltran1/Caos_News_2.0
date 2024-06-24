"strict mode";

/*   FUNCION PARA OCULTAR Y MOSTRAR PARRAFO   */ 
$(document).ready(function(){  /*  Asegura que el DOM esté completamente cargado antes de ejecutar el código.  */
  $("#hide").click(function(){  /*  Oculta todos los párrafos cuando se hace clic en el elemento con el id hide.  */
    $("p").hide();  
  });
  $("#show").click(function(){    /*  /*  Muestra todos los párrafos cuando se hace clic en el elemento con el id show.  */
    $("p").show();  /*    */
  });
});

$(".btn-2").click(function(){   /*  Alterna la visibilidad de los elementos con la clase parrafo cuando se hace clic en un elemento con la clase btn-2.  */
  $(".parrafo").toggle();     /*    */
});


/*   FUNCION PARA CAMBIAR EL TAMAÑO DEL PARRAFO     */

/*  cambiarTamaño(tamaño): Devuelve una función que cambia el tamaño de la fuente del elemento con la clase parrafo al valor especificado.*/ 
const cambiarTamaño = tamaño => {
  return ()=> {
      document.querySelector(".parrafo").style.fontSize = `${tamaño}px`;
  }
}

/* Asigna funciones específicas para tamaños 12px, 14px, y 16px. */
px12 = cambiarTamaño(12);
px14 = cambiarTamaño(14);
px16 = cambiarTamaño(16);

/* Asocia estas funciones a los eventos de clic de los elementos con las clases t12, t14, y t16. */
document.querySelector(".t12").addEventListener("click",px12);
document.querySelector(".t14").addEventListener("click",px14);
document.querySelector(".t16").addEventListener("click",px16);



/*    FUNCION PARA MOSTRAR LA HORA ACTUAL    */

/* addZeros(n): Añade un cero delante de números menores a 10 para mantener un formato de dos dígitos. */
const addZeros = n => {
  if(n.toString().length < 2) return "0".concat(n); /* // Convierte el número a cadena y si la longitud es menor que 2, agrega un cero al principio */
  return n;
}

/* actualizaHora(): Obtiene la hora actual y actualiza los elementos con las clases hora, min, y seg cada segundo usando setInterval. */
const actualizaHora = ()=> {
  const time = new Date();  /* Obtiene la fecha y hora actual */
  /*  Obtiene la hora,minutos y segundos actual y la formatea para que siempre tenga dos dígitos */
  let hora = addZeros(time.getHours());
  let min = addZeros(time.getMinutes());
  let seg = addZeros(time.getSeconds());
  /* Selecciona el elemento con la clase "hora""min" "seg" y actualiza su contenido con la hora formateada */
  document.querySelector(".hora").textContent = hora;
  document.querySelector(".min").textContent = min;
  document.querySelector(".seg").textContent = seg;
}

actualizaHora()   /* Llama a la función actualizaHora inmediatamente para establecer la hora actual al cargar el script */
setInterval(actualizaHora,1000) /* Configura un intervalo para llamar a la función actualizaHora cada 1000 milisegundos (1 segundo) */



/*POPOVER FUNCION*/
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
  
const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')
myModal.addEventListener('shown.bs.modal', () => {
myInput.focus()})


const popover = new bootstrap.Popover('.popover-dismiss', {
  trigger: 'focus'
})


/*   API RESULTADOS PARTIDOS DE FUTBOL EN VIVO   */

var myHeaders = new Headers();
myHeaders.append("x-rapidapi-key", "b58117cc7b0945b18cb771ae60be02c7");
myHeaders.append("x-rapidapi-host", "v3.football.api-sports.io");

/* Define las opciones para la solicitud fetch */
var requestOptions = {
  method: 'GET',    /* Establece el método HTTP a 'GET' */
  headers: myHeaders, /* Incluye los encabezados definidos anteriormente */
  redirect: 'follow'  /* Define la política de redirección como 'follow' (seguir redirecciones) */
};

fetch("https://v3.football.api-sports.io/leagues", requestOptions) /* Realiza una solicitud fetch a la URL especificada con las opciones definidas */
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error)); /* Si ocurre un error durante el fetch, lo captura y lo registra en la consola */



  
  /*  testing  */

  document.addEventListener('DOMContentLoaded', function() {
    var mas = document.querySelector('.mas');
    var menos = document.querySelector('.menos');
    var contenidoAdicional = document.querySelector('.contenido-adicional');
  
    mas.addEventListener('click', function() {
      contenidoAdicional.style.display = 'block';
      mas.style.display = 'none';
      menos.style.display = 'inline';
    });
  
    menos.addEventListener('click', function() {
      contenidoAdicional.style.display = 'none';
      mas.style.display = 'inline';
      menos.style.display = 'none';
    });
  });
  