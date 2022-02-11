//Esse arquivo terá o propósito de adicionar class para os elementos do html de uma forma mais prática;
$(document).ready(function() {
    $('#allCards > div').each(function() {
        $(this).addClass('card-all') //Classe para controle
    })
    $('#allCards li').each(function() {
        $(this).addClass('cardContent justify-content-center d-flex flex-row w-50')
    })
    $('div.card-all h3').each(function() {
        $(this).addClass('text-uppercase')
        $(this).css('display', 'inline')
        $(this).attr('role','button')
        $(this).addClass('link-primary')
    })
    $('li.cardContent').each(function(index) {
        if (index == 0) {
            $(this).addClass('tabActive')
        }
        else {
            $(this).addClass('d-none')
        }
    })
    $('li.d-flex > div').each(function() {
        $(this).addClass('card w-25')
    })
    $('div.card img').each(function() {
        $(this).addClass('card-img-top img-fluid')
    })
    $('div.card > div').each(function() {
        $(this).addClass('card-body')
    })
    $('div.card-body h5').each(function() {
        $(this).addClass('card-title')
    })
    $('div.card-body p').each(function() {
        $(this).addClass('card-text fs-6')
        $(this).addClass('lead')
    })
    $('#allCards .card').each(function() {
        $(this).addClass('mx-1') //Margin "nivel" 4
    })
})