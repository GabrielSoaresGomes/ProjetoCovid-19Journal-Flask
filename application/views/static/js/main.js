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

$('#subir-pagina').click(function () {
    $('html, body').animate({
        scrollTop: 0
    }, 100);
    return false;
})

$('#subir-pagina').hover(function () {
    $(this).animate({
        fontSize: '+=3'
    }, 100);

}, function () {
    $(this).animate({
        fontSize: '-=3'
    }, 100);
})
