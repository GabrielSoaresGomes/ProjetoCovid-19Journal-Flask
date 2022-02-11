$(document).ready(function() {
    console.log($('div#allCards').html())
    var todosEstados = $('div#allCards').html()
    $('.listaEstados').load('../templates/cards.html')
})