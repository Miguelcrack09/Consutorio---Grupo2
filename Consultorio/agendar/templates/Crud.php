<!DOCTYPE html>
<html lang="es">
{% load static %}
<head>
	<meta charset="Latin1">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet"href="{% static 'css/agenda.css' %}">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="bootstrap-4.3.1/js/bootstrap.min.js"></script>
	<title>Agendar</title>
</head>
<!--Inicio del encabezado-->

<header class="header">
		<div class="conteiner logo-nav-conteiner">
        
			<a href="#" class="logo"> <img src="{% static 'Imagenes/pokemon.gif' %}" width="100" height="100"> </a>
			<h1>Consultorio virtual</h1>
			<span class="menu-icon">Ver menú</span>
			<nav class="navigation">
		<ul class="menu">

		<!--Palabras que aparecen en el menu-->
		<li><a href=""></a>
		
		</li>
		<li><a href=""></a>
		<!--Menu plegable-->
		</li>
		<li><a href="#"></a>
			<ul class="submenu">
				<li><a href=""></a></li>
				<li><a href=""></a></li>
			</ul>
		</li>
		<!--Fin menu plegable-->	
	</ul>			
			</nav>
		</div>
	</header>
<script src="JS/jquery-slim.min.js" ></script>
<script src="JS/scripts.js" ></script>
<body class="body">
	
<!--fin del encabezado-->
<main class="main">
<!--- inicial contenido -->
<div class="container">

    <div class="row">
      <div class="col-12">
        <table class="table table-striped table-bordered table-hover" id="tablaproductos">
          <thead>
            <tr>
              <td>Fecha</td>
              <td>Hora</td>
              <td>Especialista</td>
              <td>Ingresar</td>
              <td>Modificar</td>
              <td>Borrar</td>
            </tr>
          </thead>
        </table>
        <button class="btn btn-sm btn-primary" id="BotonAgregar">Agregar artículo</button>
      </div>
    </div>

    <!-- Formulario (Agregar, Modificar) -->

    <div class="modal fade" id="FormularioProductos" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">

            <button type="button" class="close" data-dismiss="modal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <input type="hidden" id="Id_producto">
            <div class="form-row">
              <div class="form-group col-md-12">
                <label>Fecha</label>
                <input type="text" id="Descripcion" class="form-control" placeholder="">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group col-md-12">
                <label>Hora</label>
                <input type="number" id="Precio" class="form-control" placeholder="">
              </div>
            </div>


            <div class="modal-footer">
              <button type="button" id="ConfirmarAgregar" class="btn btn-success">Agregar</button>
              <button type="button" id="ConfirmarModificar" class="btn btn-success">Modificar</button>
              <button type="button" class="btn btn-success" data-dismiss="modal">Cancelar</button>
            </div>

          </div>
        </div>
      </div>

    </div>

    <script>
      document.addEventListener("DOMContentLoaded", function() {
        
        let tabla1 = $("#tablaproductos").DataTable({
          "ajax": {
            url: "datos.php?accion=listar",
            dataSrc: ""
          },
          "columns": [{
              "data": "id_producto"
            },
            {
              "data": "descripcion"
            },
            {
              "data": "precio"
            },
            {
              "data": "unidades"
            },
            {
              "data": null,
              "orderable": false
            },
            {
              "data": null,
              "orderable": false
            }
          ],
          "columnDefs": [{
            targets: 4,
            "defaultContent": "<button class='btn btn-sm btn-primary botonmodificar'>Modifica?</button>",
            data: null
          }, {
            targets: 5,
            "defaultContent": "<button class='btn btn-sm btn-primary botonborrar'>Borra?</button>",
            data: null
          }],
          "language": {
            "url": "DataTables/spanish.json",
          },
        });

        //Eventos de botones de la aplicación
        $('#BotonAgregar').click(function() {
          $('#ConfirmarAgregar').show();
          $('#ConfirmarModificar').hide();
          limpiarFormulario();
          $("#FormularioProductos").modal('show');
        });

        $('#ConfirmarAgregar').click(function() {
          $("#FormularioProductos").modal('hide');
          let registro = recuperarDatosFormulario();
          agregarRegistro(registro);
        });

        $('#ConfirmarModificar').click(function() {
          $("#FormularioProductos").modal('hide');
          let registro = recuperarDatosFormulario();
          modificarRegistro(registro);
        });

        $('#tablaproductos tbody').on('click', 'button.botonmodificar', function() {
          $('#ConfirmarAgregar').hide();
          $('#ConfirmarModificar').show();
          let registro = tabla1.row($(this).parents('tr')).data();
          recuperarRegistro(registro.id_producto);
        });

        $('#tablaproductos tbody').on('click', 'button.botonborrar', function() {
          if (confirm("¿Realmente quiere borrar el artículo?")) {
            let registro = tabla1.row($(this).parents('tr')).data();
            borrarRegistro(registro.id_producto);
          }
        });

        // funciones que interactuan con el formulario de entrada de datos
        function limpiarFormulario() {
          $('#Id_producto').val('');
          $('#Descripcion').val('');
          $('#Precio').val('');
          $('#Unidades').val('');
        }

        function recuperarDatosFormulario() {
          let registro = {
            id_producto: $('#Id_producto').val(),
            descripcion: $('#Descripcion').val(),
            precio: $('#Precio').val(),
            unidades: $('#Unidades').val()
          };
          return registro;
        }


        // funciones para comunicarse con el servidor via ajax
        function agregarRegistro(registro) {
          $.ajax({
            type: 'POST',
            url: 'datos.php?accion=agregar',
            data: registro,
            success: function(msg) {
              tabla1.ajax.reload();
            },
            error: function() {
              alert("Hay un problema");
            }
          });
        }

        function borrarRegistro(id_producto) {
          $.ajax({
            type: 'GET',
            url: 'datos.php?accion=borrar&id_producto=' + id_producto,
            data: '',
            success: function(msg) {
              tabla1.ajax.reload();
            },
            error: function() {
              alert("Hay un problema");
            }
          });
        }

        function recuperarRegistro(id_producto) {
          $.ajax({
            type: 'GET',
            url: 'datos.php?accion=consultar&id_producto=' + id_producto,
            data: '',
            success: function(datos) {
              $('#Id_producto').val(datos[0].id_producto);
              $('#Descripcion').val(datos[0].descripcion);
              $('#Precio').val(datos[0].precio);
              $('#Unidades').val(datos[0].unidades);
              $("#FormularioProductos").modal('show');
            },
            error: function() {
              alert("Hay un problema");
            }
          });
        }

        function modificarRegistro(registro) {
          $.ajax({
            type: 'POST',
            url: 'datos.php?accion=modificar&id_producto=' + registro.id_producto,
            data: registro,
            success: function(msg) {
              tabla1.ajax.reload();
            },
            error: function() {
              alert("Hay un problema");
            }
          });
        }

      });
    </script>

<!--- Fin del contenido-->
</main>
<br>
<!--Inicio del footer-->
     <footer
	class="text-center text-lg-start text-white"
	style="background-color: #1c2331"
	>
	<!-- Section: Social media -->
	<section
	class="d-flex justify-content-between p-4"
	style="background-color: #0d6efd"
	>
	<!-- Left -->
	<div class="me-5">
		<span> Tu salud en las mejores manos</span>
	</div>
	<!-- Left -->

	<!-- Right -->
	<div>
		<a href="" class="text-white me-4">
			<i class="fab fa-facebook-f"></i>
		</a>
		<a href="" class="text-white me-4">
			<i class="fab fa-twitter"></i>
		</a>
		<a href="" class="text-white me-4">
			<i class="fab fa-google"></i>
		</a>
		<a href="" class="text-white me-4">
			<i class="fab fa-instagram"></i>
		</a>
		<a href="" class="text-white me-4">
			<i class="fab fa-linkedin"></i>
		</a>
		<a href="" class="text-white me-4">
			<i class="fab fa-github"></i>
		</a>
	</div>
	<!-- Right -->
</section>
<!-- Section: Social media -->

<!-- Section: Links  -->
<section class="">
	<div class="container text-center text-md-start mt-5">
		<!-- Grid row -->
		<div class="row mt-3">
			<!-- Grid column -->
			<div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
				<!-- Content -->
				<h6 class="text-uppercase fw-bold">Consultorio Online</h6>
				<hr
				class="mb-4 mt-0 d-inline-block mx-auto"
				style="width: 60px; background-color: #7c4dff; height: 2px"
				/>
				<p> Agenda tu cita desde la comodidad de tu hogar</p>
			</div>
			<!-- Grid column -->

			<!-- Grid column -->
			<div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
				<!-- Links -->
				<h6 class="text-uppercase fw-bold">Doctores</h6>
				<hr
				class="mb-4 mt-0 d-inline-block mx-auto"
				style="width: 60px; background-color: #7c4dff; height: 2px"
				/>
				<p> 
					<a href="#!" class="text-white">Dr. Chapatin</a>
				</p>
				<p>
					<a href="#!" class="text-white"> Dra. Corazón</a>
				</p>
				<p>
					<a href="#!" class="text-white">Dr. Huesitos</a>
				</p>
				<p>
					<a href="#!" class="text-white">Dra. Angular</a>
				</p>
			</div>
			<!-- Grid column -->

			<!-- Grid column -->
			<div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
				<!-- Links -->
				<h6 class="text-uppercase fw-bold">Especialidades</h6>
				<hr
				class="mb-4 mt-0 d-inline-block mx-auto"
				style="width: 60px; background-color: #7c4dff; height: 2px"
				/>
				<p>
					<a href="#!" class="text-white">Medicina General</a>
				</p>
				<p>
					<a href="#!" class="text-white">Odontologia</a>
				</p>
				<p>
					<a href="#!" class="text-white">Internista</a>
				</p>
				<p>
					<a href="#!" class="text-white">Urgencias</a>
				</p>
			</div>
			<!-- Grid column -->

			<!-- Grid column -->
			<div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
				<!-- Links -->
				<h6 class="text-uppercase fw-bold">Contactenos</h6>
				<hr
				class="mb-4 mt-0 d-inline-block mx-auto"
				style="width: 60px; background-color: #7c4dff; height: 2px"
				/>
				<p><i class="fas fa-home mr-3"></i> Colombia</p>
				<p><i class="fas fa-envelope mr-3"></i> consultorio@gmail.com</p>
				<p><i class="fas fa-phone mr-3"></i> +57 123 456 25</p>
				<p><i class="fas fa-print mr-3"></i> + 01 234 567 89</p>
			</div>
			<!-- Grid column -->
		</div>
		<!-- Grid row -->
	</div>
</section>
<!-- Section: Links  -->

<!-- Copyright -->
<div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)"> 
	© 2020 Copyright: Grupo 2 MisionTIC
</div>
</footer>

</body>
</html>