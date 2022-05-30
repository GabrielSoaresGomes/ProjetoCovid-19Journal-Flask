from flask import render_template
from application import app
from application.models.dao.NoticiaDAO import NoticiaDAO

@app.route("/")
def home():
    return render_template("home.html", noticias=NoticiaDAO().get_noticia_lista, estadosNav=lista_estados,mais_vistas = NoticiaDAO().get_mais_vistas(), mais_curtidas = NoticiaDAO().get_mais_curtidas(), 
        mais_recentes = NoticiaDAO().get_mais_recentes(), estados=lista_estados)



