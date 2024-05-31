$(document).ready(function() {

    // Event listener para checkboxes
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            // Llama a la función para actualizar el carrito y verificar la compra
            actualizarCarrito();
            verificarCompra();
        });
    });

    // Event listener para botones radiales de suscripción
    const radios = document.querySelectorAll('input[type="radio"][name="subscripcion"]');
    radios.forEach(function (radio) {
        radio.addEventListener('change', function () {
            // Llama a la función para actualizar el carrito y verificar la compra
            actualizarCarrito();
            verificarCompra();
        });
    });

    // Event listener para campos de datos de pago
    const camposPago = document.querySelectorAll('input[type="text"]');
    camposPago.forEach(function (input) {
        input.addEventListener('input', function () {
            // Llama a la función para verificar la compra
            verificarCompra();
        });
    });

    // Función para actualizar el carrito de compras
    function actualizarCarrito() {
        const productosSeleccionados = [];
        let total = 0;

        // Obtener productos seleccionados y calcular total
        checkboxes.forEach(function (checkbox) {
            if (checkbox.checked) {
                // Obtiene el nombre del producto y su precio
                const producto = checkbox.labels[0].innerText;
                const precio = parseFloat(checkbox.value);
                total += precio;
                // Agrega el producto al array de productos seleccionados
                productosSeleccionados.push(`${producto} - $${(precio / 1000).toFixed(0)}.000`);
            }
        });

        // Obtener la suscripción seleccionada y calcular el total
        radios.forEach(function (radio) {
            if (radio.checked) {
                // Obtiene el nombre de la suscripción y su precio
                const subscripcion = radio.labels[0].innerText;
                const precio = parseFloat(radio.value);
                total += precio;
                // Agrega la suscripción al array de productos seleccionados
                productosSeleccionados.push(`${subscripcion} - $${(precio / 1000).toFixed(0)}.000`);
            }
        });

        // Actualizar lista de productos en el carrito
        const carrito = document.getElementById('carrito');
        carrito.innerHTML = '';
        productosSeleccionados.forEach(function (producto) {
            // Crea un elemento de lista para cada producto y lo agrega al carrito
            const li = document.createElement('li');
            li.className = 'list-group-item';
            li.textContent = producto;
            carrito.appendChild(li);
        });

        // Actualizar total
        const totalElement = document.getElementById('total');
        totalElement.textContent = `Total: $${(total / 1000).toFixed(0)}.000`;
    }

    // Función para verificar si se puede proceder con la compra
    function verificarCompra() {
        // Obtener valores de los campos de datos de pago
        const nombre = document.getElementById('nombre').value;
        const tarjeta = document.getElementById('numero').value;
        const expiracion = document.getElementById('expiracion').value;
        const codigo = document.getElementById('codigo').value;
        const direccion = document.getElementById('direccion').value;
        // Verificar si se ha seleccionado una suscripción
        const subscripcionMensual = document.getElementById('mensual').checked;
        const subscripcionAnual = document.getElementById('anual').checked;
        const subscripcionSeleccionada = subscripcionMensual || subscripcionAnual;
        // Verificar si todos los campos de datos de pago están completos
        const camposCompletos = nombre && tarjeta && expiracion && codigo && direccion;
        // Habilitar el botón de compra si todos los campos están completos y se ha seleccionado una suscripción
        const botonCompra = document.getElementById('comprarBtn');
        botonCompra.disabled = !(camposCompletos && subscripcionSeleccionada);
    }
    // Event listener para el botón de Comprar
    const comprarBtn = document.getElementById('comprarBtn');
    comprarBtn.addEventListener('click', function () {
        const nombre = document.getElementById('nombre').value;
        const suscripcion = document.querySelector('input[name="subscripcion"]:checked').nextElementSibling.textContent;
        const total = document.getElementById('total').textContent;

        // Mostrar detalles en el modal
        document.getElementById('nombreModal').textContent = nombre;
        document.getElementById('suscripcionModal').textContent = suscripcion;
        document.getElementById('totalModal').textContent = total;

        // Mostrar el modal
        document.getElementById('modalCompra').classList.add('show');
        document.getElementById('modalCompra').style.display = 'block';
    });
    // Event listener para cerrar el modal al hacer clic en la "x"
    const closeModalButton = document.querySelector('[data-dismiss="modal"]');
    closeModalButton.addEventListener('click', function () {
        const modal = document.getElementById('modalCompra');
        modal.classList.remove('show');
        modal.style.display = 'none';
    });

});