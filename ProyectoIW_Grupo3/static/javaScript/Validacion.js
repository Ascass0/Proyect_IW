
function validarEmpleado() {

    document.getElementById('spanTLFN').style.visibility = "hidden";
    document.getElementById('spanDNI').style.visibility = "hidden";

    var DNI = document.getElementById('id_DNI').value;
    var telefono = document.getElementById('id_telfono').value;


    if (String(DNI).length != 9) {
        document.getElementById('spanDNI').style.visibility = "visible";
        if (String(telefono).length != 9) {
            document.getElementById('spanTLFN').style.visibility = "visible";
            return false;
        }
        return false;
    } else if (String(telefono).length != 9) {
        document.getElementById('spanTLFN').style.visibility = "visible";
        return false;
    } else {
        return true;
    }

}



function validarEquipo() {

    document.getElementById('spanTLFN').style.visibility = "hidden";
    document.getElementById('spanFechas').style.visibility = "hidden";

    var telefono = document.getElementById('id_proveedorTelefono').value;
    var fechaCompra = document.getElementById('id_fechaAdquisicion').value;
    var fechaMarcha = document.getElementById('id_fechaPuestaMarcha').value;

    if (fechaCompra > fechaMarcha) {
        document.getElementById('spanFechas').style.visibility = "visible";
        if (String(telefono).length != 9) {
            document.getElementById('spanTLFN').style.visibility = "visible";
            return false;
        }
        return false;
    } else if (String(telefono).length != 9) {
        document.getElementById('spanTLFN').style.visibility = "visible";
        return false;
    } else {
        return true;
    }

}


function validarTicket() {

    document.getElementById('spanFechas').style.visibility = "hidden";

    var fechaApertura = document.getElementById('id_fechaApertura').value;
    var fechaResolucion = document.getElementById('id_fechaResolucion').value;

    if (fechaApertura > fechaResolucion) {
        document.getElementById('spanFechas').style.visibility = "visible";
        return false;
    } else {
        return true;
    }

}