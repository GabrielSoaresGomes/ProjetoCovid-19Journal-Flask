from flask import render_template
from application import app

@app.route("/estado/<estado>")
def detalharEstado(estado):
    for est in lista_estados:
        if est.get_estado() == estado:
            return render_template("noticia_estado.html", estado=est,
                                   noticias=lista_noticias, estadosNav=lista_estados)