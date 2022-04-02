$(document).ready(function() {
    $('#js-example-basic-single').select2();
});

$('#js-example-basic-single').change(function () {
    if ($(this).val() != "None") {
        if ((window.location.pathname).split('/')[1] == "estado") {
            window.location.href = $(this).val();
        }
        else{
            window.location.href = "estado/" + $(this).val();
        }
    }
})


