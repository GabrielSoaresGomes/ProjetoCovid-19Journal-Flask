$(document).ready(function() {
    $('h1#tituloDetalhes').html(localStorage.getItem('title'))
    $('p#textoDetalhes').html(localStorage.getItem('text'))
    $('img#imagemDetalhes').attr('src',localStorage.getItem('image'))
})