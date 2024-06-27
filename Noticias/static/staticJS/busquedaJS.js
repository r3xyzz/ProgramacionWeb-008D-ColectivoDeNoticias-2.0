// busquedaJS.js

$(document).ready(function(){ 
    document.addEventListener('DOMContentLoaded', function() {
        var searchForm = document.getElementById('searchForm');
        if (searchForm) {
            searchForm.addEventListener('submit', function(event) {
                event.preventDefault(); // Prevenir la acción por defecto del formulario
                buscar();
            });
        }
    });
    
    function buscar() {
        var query = document.getElementById('searchInput').value;
        if (query.trim() === "") {
            window.location.href = '/registrocaosnew'; // Redirigir a noticiascaosnew si la búsqueda está vacía
        } else {
            window.location.href = '/buscar?q=' + query; // Redirigir a la página de búsqueda con la consulta
        }
    }
    
    });