$('a.card-link').click(function() {
    let cardTitle = $(this).parent().siblings('div').first().children().first().html()
    let cardImage = $(this).parent().siblings('img').first().attr('src')
    let cardText = $(this).parent().siblings('div').first().children().last().html()
    console.log(cardText)
    localStorage.setItem("title",cardTitle);
    localStorage.setItem("image",cardImage);
    localStorage.setItem("text",cardText);



    window.location.href = '../templates/detalhes.html'
})