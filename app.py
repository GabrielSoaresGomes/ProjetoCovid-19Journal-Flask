from flask import Flask, render_template
from Noticias import Noticias
from Estados import Estado
from listas_python.lista_noticias import lista_noticias
from listas_python.lista_estados import lista_estados

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", noticias=lista_noticias, estados=lista_estados, home=True)


@app.route("/detalhes/<int:id>")
def detalhes(id):
    for noticia in lista_noticias:
        if int(noticia.get_id()) == int(id):
            return render_template("detalhes.html", noticia=noticia)


@app.route("/estado/<estado>")
def detalharEstado(estado):
    for est in lista_estados:
        if est[0].get_estado() == estado:
            return render_template("noticia_estado.html", estado=lista_estados[int(est[0].get_id())],
                                   noticias=lista_noticias)


#app.run(debug=True)
