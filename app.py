from flask import Flask, render_template
from Noticias import Noticias
from Estados import Estado
from listas_python.lista_noticias import lista_noticias
from listas_python.lista_estados import lista_estados

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html", noticias=lista_noticias, estados=lista_estados, home=True)


@app.route("/detalhes/<id>")
def detalhes(id):
    for noticia in lista_noticias:
        if int(noticia.get_id()) == int(id):
            return render_template("detalhes.html", noticia=lista_noticias[int(id)])


@app.route("/estado/<estado>")
def detalharEstado(estado):
    for est in lista_estados:
        if est.get_estado() == estado:
            return render_template("noticia_estado.html", estado=lista_estados[int(est.get_id())],
                                   noticias=lista_noticias)



app.run(debug=True)