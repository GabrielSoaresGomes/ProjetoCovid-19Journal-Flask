$('h3').click(function() {
    console.log("func")
    var todasTabs = $('li.cardContent')
    if ($(this).next().hasClass('tabActive') == false) {
        console.log("if")
        $(todasTabs).each(function() {
            if ($(this).hasClass('tabActive')) {
                $(this).removeClass('tabActive')
                $(this).addClass('d-none')
            }
        })
        $(this).next().addClass('tabActive')
        $(this).next().removeClass('d-none')

    }
})