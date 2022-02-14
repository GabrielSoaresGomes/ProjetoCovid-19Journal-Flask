$(document).ready(function() {
    $('.listaEstados').load('../templates/cards.html')
})


$("div.listaBandeiras a").click(function() {
    var idClicado = $(this).attr('id')
    $('div.card-all li').each(function() {
        if ($(this).attr('id').replace('id-', '') === idClicado) {
            var todasTabs = $('li.cardContent')
            if ($(this).hasClass('tabActive') == false) {
                $(todasTabs).each(function() {
                    if ($(this).hasClass('tabActive')) {
                        $(this).removeClass('tabActive')
                        $(this).addClass('d-none')
                        $(this).prev().removeClass("text-secondary")
                        $(this).prev().addClass('link-primary')
                    }
                })
                $(this).addClass('tabActive')
                $(this).prev().removeClass("link-primary")
                $(this).prev().addClass('text-secondary')
                $(this).removeClass('d-none')
            }
            $('html, body').animate( {
                'scrollTop': $(this).offset().top-40
            }, 0, 'swing', function () {
                window.location.hash = $(this).hash;
            } );
        }
    })
});
