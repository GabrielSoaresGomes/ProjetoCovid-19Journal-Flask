$(document).ready(function() {
    $('#js-example-basic-single').select2();
});

$('#js-example-basic-single').change(function () {
    window.location.href = "estado/"+$(this).val()
})