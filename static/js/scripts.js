// Ciclo para crear espacios para las letras
function generarEspacios(longitudPalabra) {
    var element = document.getElementById("espacios");
    for (let i = 0; i < longitudPalabra; i++) {
        var input = document.createElement("input");
        input.setAttribute("class","linea");
        input.setAttribute("type","text");
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
                console.log(data);
            }
        });
    })
})