from flask import render_template
from application import app
from application.models.dao.NoticiaDAO import NoticiaDAO

@app.route("/detalhes/<int:id>")
def detalhes(id):
    resultado_busca = NoticiaDAO().buscar_noticia(id) 
    if resultado_busca:
        return render_template("detalhes.html", noticia=resultado_busca, estadosNav=lista_estados, detalhes=True)
    

