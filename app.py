from flask import Flask, render_template
from Noticias import Noticias
from Estados import Estado
from listas_python.lista_noticias import lista_noticias
from listas_python.lista_estados import lista_estados

app = Flask(__name__)

@app.errorhandler(404) 
def error(e): 
  return render_template("error.html", error=True) 


@app.route("/")
def home():
    return render_template("home.html", noticias=lista_noticias, estadosNav=lista_estados)


@app.route("/detalhes/<int:id>")
def detalhes(id):
    for noticia in lista_noticias:
        if int(noticia.get_id()) == int(id):
            return render_template("detalhes.html", noticia=noticia, estadosNav=lista_estados, detalhes=True)


@app.route("/estado/<estado>")
def detalharEstado(estado):
    for est in lista_estados:
        if est.get_estado() == estado:
            return render_template("noticia_estado.html", estado=lista_estados[int(est.get_id())],
                                   noticias=lista_noticias, estadosNav=lista_estados)

# app.run(debug=True)
