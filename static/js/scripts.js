// function mandarLetra() {

// }
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
