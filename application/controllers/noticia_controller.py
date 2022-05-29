from flask import render_template
from application import app

@app.route("/detalhes/<int:id>")
def detalhes(id):
    for noticia in lista_noticias:
        if int(noticia.get_id()) == int(id):
            noticia.views += 1
            return render_template("detalhes.html", noticia=noticia, estadosNav=lista_estados, detalhes=True)

