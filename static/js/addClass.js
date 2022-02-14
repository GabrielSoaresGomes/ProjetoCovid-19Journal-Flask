//Esse arquivo terá o propósito de adicionar class para os elementos do html de uma forma mais prática;
var todosEstados = [
    'acre', 'alagoas', 'amapa', 'amazonas', 'bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão',
    'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
    'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo',
    'Sergipe', 'Tocantins'
]
var c = 0

$(document).ready(function() {
    $('#allCards > div').each(function() {
        $(this).addClass('card-all') //Classe para controle
    })
    $('#allCards li').each(function() {
        $(this).addClass('cardContent justify-content-center d-flex flex-row w-50')
    })
    $('div.card-all').each(function() {
        $(this).addClass('my-5')
    })
    $('div.card-all h3').each(function(index) {
        if (index == 0) {
            $(this).addClass('text-secondary')
        }
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
        $(this).addClass('card w-25 shadow ')
    })
    $('div.card img').each(function() {
        $(this).addClass('h-75 card-img-top img-fluid')
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
    $('div.listaBandeiras img').each(function() {
        $(this).css('width', '20px')
    })
    $('h3 img').each(function() {
        $(this).css('width', '30px')
        $(this).css('margin-right', '5px')
    })
    // $('div.listaBandeiras a').each(function() {
    //     $(this).attr('href','#id-'+$(this).attr('id'))
    // })

})