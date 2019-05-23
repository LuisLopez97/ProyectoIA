function mandarLetra() {

}

$(".letra").click(function (event) {
    // event.preventDefault();
    $.ajax({
        type: "GET",
        url: 'recibir',
        data: {
            letra: $("this.id").val()
        },
        success: function (data) {
            // separador_inicio = data.split('INICIO');
            // inicio = separador_inicio[0];
            // separador_etapa1 = separador_inicio[separador_inicio.length - 1].split('ETAPA1');
            // separador_etapa2 = separador_etapa1[separador_etapa1.length - 1].split('ETAPA2');
            // separador_etapa3 = separador_etapa2[separador_etapa2.length - 1].split('ETAPA3');
            // separador_final = separador_etapa3[separador_etapa3.length - 1].split('FINAL');
            // $('#salida').html(inicio + separador_etapa1[0] + separador_etapa2[0] + separador_etapa3[0] + separador_final[0]);
        }
    });