//Esse arquivo terá o propósito de adicionar class para os elementos do html de uma forma mais prática;
$(document).ready(function() {
    $('#allCards > div').each(function() {
        $(this).addClass('card-all') //Classe para controle
    })
    $('#allCards li').each(function() {
        $(this).addClass('justify-content-center') //Classe para alinhar flex no centro
    })
    $('#allCards .card').each(function() {
        $(this).addClass('mx-1') //Margin "nivel" 4
    })
})