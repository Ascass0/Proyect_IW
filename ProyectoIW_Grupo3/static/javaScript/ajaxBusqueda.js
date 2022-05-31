

let botonenviar = document.querySelector('.jsbotonbusqueda')
botonenviar.addEventListener('click', e => {
    e.preventDefault()
    let datosbusqueda = document.querySelector('#botonbusq').value
    datosbusqueda = { 'searchTerm': datosbusqueda }
    fetch('listadoTickets', {
        method: 'POST',
        body: JSON.stringify(datosbusqueda),
    }
    ).then(
        function (response) {
            console.log(response)
            return response.json()
        }
    ).then(
        (data) => {
            let tbody = document.querySelector('#jstablabusqueda')
            tbody.innerHTML = ''
            let tabla = document.querySelector('#jstabla')
            data.tickets.forEach(element => {
                let { id, titulo, estado } = element
                let row = tbody.insertRow(0)
                let cell0 = row.insertCell(0)
                let cell1 = row.insertCell(1)
                let cell2 = row.insertCell(2)
                cell0.innerHTML = titulo
                cell1.innerHTML = estado
                cell2.innerHTML = `<a href="/appProyectoIW_Grupo3/listadoTickets/${id}" class="detalles">Ver detalles</a>`
            });

        }
    )
})


