<?php
header('Content-Type: application/json');

require("conexion.php");

$conexion = retornarConexion();

switch ($_GET['accion']) {
    case 'listar':
        $datos = mysqli_query($conexion, "select id_producto,descripcion,precio,unidades from productos");
        $resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
        echo json_encode($resultado);
        break;

    case 'agregar':
        $respuesta = mysqli_query($conexion, "insert into productos(descripcion,precio,unidades) values ('$_POST[descripcion]',$_POST[precio],$_POST[unidades])");
        echo json_encode($respuesta);
        break;

    case 'borrar':
        $respuesta = mysqli_query($conexion, "delete from productos where id_producto =$_GET[id_producto]");
        echo json_encode($respuesta);
        break;

    case 'consultar':
        $datos = mysqli_query($conexion, "select id_producto,descripcion,precio,unidades from productos where id_producto=$_GET[id_producto]");
        $resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
        echo json_encode($resultado);
        break;

    case 'modificar':
        $respuesta = mysqli_query($conexion, "update productos set descripcion ='$_POST[descripcion]', precio =$_POST[precio], unidades =$_POST[unidades] where id_producto =$_GET[id_producto]");
        
        echo json_encode($respuesta);
        break;
}
?>