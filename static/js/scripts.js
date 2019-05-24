// Ciclo para crear espacios para las letras
function generarEspacios(longitudPalabra) {
    var element = document.getElementById("espacios");
    for (let i = 0; i < longitudPalabra; i++) {
        var input = document.createElement("input");
        input.setAttribute("type","text");
        input.setAttribute("class","linea");
        input.setAttribute("id", i+1);
        input.disabled = true;
        element.appendChild(input);
    }
}
var contador = 1;
var aciertos = 0;
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
                if(data.posicion.length!=0){
                    // console.log("acertaste");
                    for (let i = 0; i < data.posicion.length; i++) {
                        var espacio = document.getElementById( data.posicion[i] );
                        espacio.value = data.letra;
                        aciertos++;
                    }
                    if(aciertos==$("#size").val()){
                        window.location="/ganar";
                    }
                }
                else{
                    // console.log("fallaste");
                    var cuerpo = document.getElementById('cuerpo');
                    var imagen = document.getElementById('imagen');
                    cuerpo.removeChild(imagen);
                    var img = document.createElement('img');
                    img.setAttribute('src','/static/img/imagen_cuerpo_'+ contador+ '.png');
                    img.setAttribute('id','imagen')
                    cuerpo.appendChild(img);
                    contador++;
                    // console.log(aciertos);
                    
                    if(contador==7){
                        window.location="/perder";
                    }
                    

                }
                
            }
        });
    })
})