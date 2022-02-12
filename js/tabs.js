$('h3').click(function() {
    var todasTabs = $('li.cardContent')
    if ($(this).next().hasClass('tabActive') == false) {
        $(todasTabs).each(function() {
            if ($(this).hasClass('tabActive')) {
                $(this).removeClass('tabActive')
                $(this).addClass('d-none')
                $(this).prev().removeClass("text-secondary")
                $(this).prev().addClass('link-primary')
            }
        })
        $(this).next().addClass('tabActive')
        $(this).removeClass("link-primary")
        $(this).addClass('text-secondary')
        $(this).next().removeClass('d-none')
    }
})