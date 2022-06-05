from flask import render_template
from application import app
from application.models.dao import noticiaDAO
from application.models.dao import estadoDAO

@app.route("/")
def home():
    return render_template("home.html", noticias=noticiaDAO.get_noticia_lista(), estadosNav=estadoDAO.get_lista_estados(),mais_vistas = noticiaDAO.get_mais_vistas(), mais_curtidas = noticiaDAO.get_mais_curtidas(), 
        mais_recentes = noticiaDAO.get_mais_recentes(), estados=estadoDAO.get_lista_estados())



