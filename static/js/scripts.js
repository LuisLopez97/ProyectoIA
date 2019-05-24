// Ciclo para crear espacios para las letras
function generarEspacios(longitudPalabra) {
    var element = document.getElementById("espacios");
    for (let i = 0; i < longitudPalabra; i++) {
        var input = document.createElement("input");
        input.setAttribute("type","text");
        input.setAttribute("class","linea");
        input.setAttribute("id", i+1);
        input.disabled = true;
        // input.value = "A"
        element.appendChild(input);
    }
}

$(document).ready(function(){
    $(".letra").click(function (event) {
        // event.preventDefault();
        
        $.ajax({
            type: "GET",
            url: '/recibir',
            data: {
                letra: $(this).val()  
            },
            success: function (data) {
                console.log(data.letra);
                console.log(data.posicion);
                for (let i = 0; i < data.posicion.length; i++) {
                    var espacio = document.getElementById( data.posicion[i] );
                    espacio.value = data.letra;
                }
            }
        });
    })
})