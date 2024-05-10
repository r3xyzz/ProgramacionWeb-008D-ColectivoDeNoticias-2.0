// Hoja de JavaScript

// Implemetear Js con JQuery para tener las validaciones
// https://youtu.be/0WXiaIpQk-Q?si=BST30CxTZRDbOz2h animaciones con JQuery para hacer

//

    $(document).ready(function(){
        let ubicacionPrincipal = window.pageYOffset;
        window.onscroll = function() {
            let Desplazamiento_Actual = window.pageYOffset;
            if(ubicacionPrincipal >= Desplazamiento_Actual){
                $('#navbar').fadeIn(); // Cambio aquí, utiliza fadeIn()
            }
            else{
                $('#navbar').fadeOut(); // Cambio aquí, utiliza fadeOut()
            }
            ubicacionPrincipal = Desplazamiento_Actual;
        };
    });

