// Hoja de JavaScript

// Implemetear Js con JQuery para tener las validaciones
// https://youtu.be/0WXiaIpQk-Q?si=BST30CxTZRDbOz2h animaciones con JQuery para hacer

//animaciones de navar
$(document).ready(function(){ //asegura que el script se ejecute en el HTML cuando este cargado
        let ubicacionPrincipal = window.pageYOffset; //se define una variable para almacenar la osicion vertical de la pagina
        window.onscroll = function() { //funcion de evento que se activa cada vez que se realiza un desplazamiento en la pagina
            let Desplazamiento_Actual = window.pageYOffset; //variable de almacenamiento de posicion de la pagina
            if(ubicacionPrincipal >= Desplazamiento_Actual){ //compara la posicion inicial con la posicion actual y si la posicoin actual es menor o igual que la posocion actual significara que la persona se desplaza hacia arriba
                $('#navbar').fadeIn(); // Cambio aquí, utiliza fadeIn() | si la persona se desplaza hacia arriba se mostrara de manera suave (estos cambios tambien estan en el CSS)
            }
            else{
                $('#navbar').fadeOut(); // Cambio aquí, utiliza fadeOut() |  si la persona se desplaza hacia abajo se mostrara de manera suave y desaparezera  (estos cambios tambien estan en el CSS)
            }
            ubicacionPrincipal = Desplazamiento_Actual; //actualiza la posicion inicial con la posicion actual del desplazamiento de la pagina para que se pueda comparar con la nueva posicion del scroll
        };
    });


