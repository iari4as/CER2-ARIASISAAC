document.addEventListener("DOMContentLoaded", function() {
    const subcategorias = { 
        plastico: ["Botellas", "Envases", "Bolsas"],
        papel: ["Cartón", "Papel de oficina", "Periódicos"],
        vidrio: ["Botellas", "Frascos", "Vidrios rotos"],
        metales: ["Latas", "Chatarra", "Aluminio"],
        electronicos: ["Computadoras", "Celulares", "Baterías"]
    }

    function inicializarMenu() {
        var select1 = document.getElementById("select1");
        if (select1) {
            var opcionPorDefecto = document.createElement("option");
            opcionPorDefecto.value = "****"; 
            opcionPorDefecto.textContent = "****"; 
            select1.appendChild(opcionPorDefecto); 
            
            for (var tipo_de_reciclaje in subcategorias) {
                var opcion = document.createElement("option");
                opcion.value = tipo_de_reciclaje;
                opcion.textContent = tipo_de_reciclaje.charAt(0).toUpperCase() + tipo_de_reciclaje.slice(1);
                select1.appendChild(opcion);
            }
        }
    }

    function actualizarSubcategorias(opciones) { //actualiza las subcategrosias dependiendo de la categoria
        var select2 = document.getElementById("select2")
        if (select2) {
            select2.innerHTML = '<option value="">Seleccione una subcategoría</option>'
            opciones.forEach(function(subcat) {
                var opcion = document.createElement("option")
                opcion.value = subcat.toLowerCase()
                opcion.textContent = subcat
                select2.appendChild(opcion)
            })
        }
    }

    function validarCampos() { //valida la itegridad de los datos
        var emailInput = document.querySelector('input[name="email"]')
        var nombreInput= document.querySelector('input[name="Nombre"]')
        var direccionInput = document.querySelector('input[name="Direccion"]')
        var cantidadInput =document.querySelector('input[name="cantidad"]')
        var select1=document.getElementById('select1')
        var select2= document.getElementById('select2')

        var mensajesError = []

        var email;
        if (emailInput) {
            email = emailInput.value;
        } else {
            email = ''; 
        }
        var emailRegex= /^[^\s@]+@[^\s@]+\.[^\s@]+$/ //Expresin pa validar el formato del correo 
        if (!email || !emailRegex.test(email)) {
            mensajesError.push("Ingrese un correo electrónico válido")
        }

        var nombre = nombreInput ? nombreInput.value : ''
        if (!nombre.trim()) {
            mensajesError.push("El campo de nombre no puede estar vacío")
        }

        var direccion = direccionInput ? direccionInput.value : ''
        if (!direccion.trim()) {
            mensajesError.push("El campo de dirección no puede estar vacío")
        }

        var cantidad = cantidadInput ? cantidadInput.value : ''
        if (!cantidad || isNaN(cantidad) || cantidad <= 0) {
            mensajesError.push("Ingrese una cantidad válida de residuos")
        }

        var categoria = select1 ? select1.value : ''
        if (!categoria || categoria === "") {
            mensajesError.push("Seleccione una categoría de residuos")
        }

        var subcategoria = select2 ? select2.value : ''
        if (!subcategoria || subcategoria === "") {
            mensajesError.push("Seleccione una subcategoría de residuos")
        }

        if (mensajesError.length > 0) {
            alert(mensajesError.join("\n"))
            return false
        }

        return true
    }

    function manejarClickBoton(event) { //esta funcion es para el eevento del boton
        event.preventDefault()

        if (!validarCampos()) {
            return
        }

        var emailInput = document.querySelector('input[name="email"]')
        var nombreInput = document.querySelector('input[name="Nombre"]')
        var direccionInput = document.querySelector('input[name="Direccion"]')
        var cantidadInput = document.querySelector('input[name="cantidad"]')
        var comentariosInput = document.querySelector('input[name="comentarios"]')
        var select1 = document.getElementById('select1')
        var select2 = document.getElementById('select2')

        var email, nombre, direccion, cantidad, comentarios, categoria, subcategoria;

        if (emailInput) {
            email = emailInput.value;
        } else {
            email = '';
        }

        if (nombreInput) {
            nombre = nombreInput.value;
        } else {
            nombre = '';
        }

        if (direccionInput) {
            direccion = direccionInput.value;
        } else {
            direccion = '';
        }

        if (cantidadInput) {
            cantidad = cantidadInput.value;
        } else {
            cantidad = '';
        }

        if (comentariosInput) {
            comentarios = comentariosInput.value;
        } else {
            comentarios = '';
        }

        if (select1) {
            categoria = select1.value;
        } else {
            categoria = '';
        }

        if (select2) {
            subcategoria = select2.value;
        } else {
            subcategoria = '';
        }

        if (document.getElementById("Boton").textContent === "Enviar solicitud") {
            if (confirm("¿Está seguro de enviar la solicitud?")) {
                alert(`Nombre: ${nombre}\nCorreo: ${email}\nDirección: ${direccion}\nCantidad: ${cantidad}\nComentarios: ${comentarios}\nCategoría: ${categoria}\nSubcategoría: ${subcategoria}`)
                blanqueamento()
            }
        }
    }

    function blanqueamento() { //esta funcion limpia las casillas del fromulario
        var select1 = document.getElementById('select1')
        var select2 = document.getElementById('select2')
        var email = document.querySelector('input[name="email"]')
        var nombre = document.querySelector('input[name="Nombre"]')
        var direccion = document.querySelector('input[name="Direccion"]')
        var cantidad = document.querySelector('input[name="cantidad"]')
        var comentarios = document.querySelector('input[name="comentarios"]')
        // no es lo mismo ocupar el .querySelector('input[name="email"]')
        // que el getElementById(email)
        //el .querySelector busca name
        //console.log("lol: " + document.getElementById('email').value)
        if (select1) {
            select1.value = ''
            select1.innerHTML = '<option value="">Seleccione el tipo de residuo</option>'
            for (let tipo in subcategorias) {
                var opcion = document.createElement("option")
                opcion.value = tipo
                opcion.textContent = tipo.charAt(0).toUpperCase() + tipo.slice(1)
                select1.appendChild(opcion)
            }
        }

        if (select2) {
            select2.value = ''
            select2.innerHTML = '<option value="">Seleccione una subcategoría</option>'
        }

        if (email) {
            email.value = ''
        }
        if (nombre) {
            nombre.value = ''
        }
        if (direccion) {
            direccion.value = ''
        }
        if (cantidad) {
            cantidad.value = ''
        }
        if (comentarios) {
            comentarios.value = ''
        }
    }

    inicializarMenu()

    document.getElementById("select1").addEventListener("change", function() {
        var tipoSeleccionado = this.value.toLowerCase()
        if (subcategorias[tipoSeleccionado]) {
            actualizarSubcategorias(subcategorias[tipoSeleccionado])
        } else {
            actualizarSubcategorias([])
        }
        var boton = document.getElementById("Boton")
        if (boton) {
            boton.textContent = 'Enviar solicitud'
        }
    })

    var boton = document.getElementById("Boton")
    if (boton) {
        boton.addEventListener("click", manejarClickBoton)
    }
})
