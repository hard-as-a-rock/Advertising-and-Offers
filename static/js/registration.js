$(document).ready(function(){
    $('.form-submit').click(function(event){
        event.preventDefault();
        $('.error').html('');
        $.ajax({
            method: 'POST',
            url: '/registration/',
            data: $('form').serializeArray()
        }).done(function(response){
            if (response.status == 'ok') {
                document.location.href = "/login/";
            } else {
                for(var key in response.input_errors) {
                    var errorDiv = $('#error_' + key);
                    errorDiv.html(response.input_errors[key][0])
                }
            }
        })
    });
});