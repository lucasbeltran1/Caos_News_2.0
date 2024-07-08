// Añadir un event listener para el evento 'submit' en el formulario con el id 'registroForm'
document.getElementById('registroForm').addEventListener('submit', function(event) {
    // Prevenir el comportamiento predeterminado de enviar el formulario
    event.preventDefault();

    // Obtener los valores de los campos del formulario
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var edad = document.getElementById('edad').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmarPassword = document.getElementById('confirmarPassword').value;
    var terminos = document.getElementById('terminos').checked;

    // Verificar que todos los campos estén completos
    if (nombre === '' || apellido === '' || edad === '' || email === '' || password === '' || confirmarPassword === '') {
        alert('Todos los campos son obligatorios.');
        return;
    }

    // Verificar que el correo electrónico tenga un formato válido
    if (!validarEmail(email)) {
        alert('Por favor, ingresa una dirección de correo electrónico válida.');
        return;
    }

    // Verificar que la edad sea un número válido y que el usuario sea mayor de edad (18 años o más)
    if (!validarEdad(edad)) {
        alert('Por favor, ingresa una edad válida y asegúrate de que seas mayor de edad.');
        return;
    }

    // Verificar que la contraseña cumpla con los requisitos (al menos 6 caracteres y alfanumérica)
    if (!validarPassword(password)) {
        alert('La contraseña debe tener al menos 6 caracteres y ser alfanumérica.');
        return;
    }

    // Verificar que las contraseñas coincidan
    if (password !== confirmarPassword) {
        alert('Las contraseñas no coinciden.');
        return;
    }

    // Verificar que se hayan aceptado los términos y condiciones
    if (!terminos) {
        alert('Debes aceptar los términos y condiciones.');
        return;
    }

    // Si todas las validaciones pasan, enviar el formulario
    alert('Formulario enviado correctamente.');
    document.getElementById('registroForm').submit();
});

// Función para validar el formato del correo electrónico
function validarEmail(email) {
    var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return re.test(email);
}

// Función para validar que la edad sea un número y que el usuario sea mayor de edad
function validarEdad(edad) {
    var re = /^[0-9]+$/;
    if (!re.test(edad)) {
        return false;
    }
    var edadNum = parseInt(edad, 10);
    return edadNum >= 18;
}

// Función para validar que la contraseña tenga al menos 6 caracteres y sea alfanumérica
function validarPassword(password) {
    var re = /^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]{6,}$/;
    return re.test(password);
}
