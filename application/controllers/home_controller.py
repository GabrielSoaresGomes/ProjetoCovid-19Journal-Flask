from flask import render_template
from application import app

@app.route("/")
def home():
    return render_template("home.html", noticias=lista_noticias, estadosNav=lista_estados,mais_vistas = maisVistas(), mais_curtidas = maisCurtidas(), 
        mais_recentes = maisRecentes(), estados=lista_estados)



