

if (location.pathname == "/appProyectoIW_Grupo3/listadoEquipos") {
  document.getElementById("enlaceIndex2").setAttribute(
    "style", "filter:alpha(opacity=50); opacity:0.4;");
  document.getElementById("enlaceIndex3").setAttribute(
    "style", "filter:alpha(opacity=50); opacity:0.4;");
} else if (location.pathname == "/appProyectoIW_Grupo3/listadoTickets") {
  document.getElementById("enlaceIndex1").setAttribute(
    "style", "filter:alpha(opacity=50); opacity:0.4;");
  document.getElementById("enlaceIndex3").setAttribute(
    "style", "filter:alpha(opacity=50); opacity:0.4;");
} else if (location.pathname == "/appProyectoIW_Grupo3/listadoEmpleados") {
  document.getElementById("enlaceIndex1").setAttribute(
    "style", "filter:alpha(opacity=50); opacity:0.4;");
  document.getElementById("enlaceIndex2").setAttribute(
    "style", "filter:alpha(opacity=50); opacity:0.4;");
}