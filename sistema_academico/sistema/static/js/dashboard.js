window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

  // Obtenemos el botón por su ID
  var addbto = document.getElementById('addbto');

  // Agregamos un evento de clic al botón
addbto.addEventListener('click', function() {
    // Obtenemos el modal por su ID
    var myModal = document.getElementById('myModal');
    
    // Mostramos el modal utilizando el método 'modal' de Bootstrap
    // 'show' es el parámetro que indica que queremos mostrar el modal
    var modal = new bootstrap.Modal(myModal);
    modal.show();
  });

