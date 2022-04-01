from flask import Flask, render_template
from Noticias import Noticias
from Estados import Estado
from listas_python.lista_noticias import lista_noticias
from listas_python.lista_estados import lista_estados

app = Flask(__name__)


@app.route("/")
def home():
    try:
        return render_template("home.html", noticias=lista_noticias, estados=lista_estados, home=True)
    except:
        return render_template("error.html")


@app.route("/detalhes/<int:id>")
def detalhes(id):
    for noticia in lista_noticias:
        if int(noticia.get_id()) == int(id):
            return render_template("detalhes.html", noticia=noticia)
    return render_template("error.html")


@app.route("/estado/<estado>")
def detalharEstado(estado):
    for est in lista_estados:
        if est.get_estado() == estado:
            return render_template("noticia_estado.html", estado=lista_estados[int(est.get_id())],
                                   noticias=lista_noticias)

    return render_template("error.html")

# app.run(debug=True)
