$(document).ready(function() {
function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Check if username and password match
    if (username === "caosnew" && password === "caosnew123") {
        return true; // Allow form submission
    } else {
        alert("Nombre de usuario o contraseña inválidos");
        return false; // Prevent form submission
    }
}
});
/* La función validateForm() se ejecuta cuando se envía el formulario.
Dentro de esta función, se obtienen los valores ingresados por el usuario para el nombre de usuario y la contraseña utilizando document.getElementById().
Luego, se compara el nombre de usuario y la contraseña con los valores esperados ("caosnew" y "caosnew123" respectivamente).
Si ambos coinciden, la función devuelve true, lo que permite que el formulario se envíe y el usuario sea redirigido a la página principal.
Si los valores no coinciden, se muestra una alerta indicando que las credenciales son inválidas y la función devuelve false, lo que evita que el formulario se envíe.

<div class="container">...</div>: Este es un contenedor de Bootstrap. Bootstrap es un marco de trabajo de front-end que proporciona una estructura y estilo predefinidos para crear interfaces de usuario. El contenedor ayuda a centralizar y alinear el contenido en la página.
<h2>Login Noticias Caos New</h2>: Este es un elemento de encabezado HTML (<h2>)
    <form action="http://127.0.0.1:3000/Prog%20Web%202.0/principal.html" method="POST" onsubmit="return validateForm()">...</form>: Este es un formulario HTML (<form>). Tiene tres atributos importantes:

    action: Este atributo especifica la URL a la que se enviarán los datos del formulario cuando se envíe. En este caso, los datos se enviarán a "http://127.0.0.1:3000/Prog%20Web%202.0/principal.html".
    method: Este atributo especifica el método HTTP que se utilizará para enviar los datos del formulario. En este caso, se utiliza "POST".
    onsubmit: Este atributo especifica la acción que se llevará a cabo cuando se envíe el formulario. En este caso, se llama a la función validateForm() para validar los campos del formulario antes de enviarlos.

<input type="text" id="username" name="username" placeholder="Username" required>: Este es un campo de entrada de texto HTML (<input>). Tiene varios atributos:

type: Este atributo especifica el tipo de entrada, que en este caso es "text".
id: Este atributo proporciona un identificador único para el campo. Se utiliza para asociar el campo con etiquetas de <label> o para acceder al valor del campo mediante JavaScript.
name: Este atributo especifica el nombre del campo. Se utiliza cuando se envía el formulario para identificar el valor del campo.
placeholder: Este atributo proporciona un texto de marcador de posición que se muestra en el campo cuando está vacío.
required: Este atributo indica que el campo es obligatorio y no se puede enviar el formulario si está vacío.
   
<input type="password" id="password" name="password" placeholder="Password" required>: Este es un campo de entrada de contraseña HTML similar al campo de texto, pero está diseñado para ocultar los caracteres ingresados. Tiene atributos similares al campo de texto.

<button type="submit">Login</button>: Este es un botón de envío HTML (<button>). Cuando se hace clic en este botón dentro del formulario, el formulario se envía al destino especificado en el atributo action.
*/