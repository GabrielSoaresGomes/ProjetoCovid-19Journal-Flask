from flask import render_template
from application import app
from application.models.dao import noticiaDAO
from application.models.dao import estadoDAO

@app.route("/detalhes/<int:id>")
def detalhes(id):
    resultado_busca = noticiaDAO.buscar_noticia(id) 
    if resultado_busca:
        return render_template("detalhes.html", noticia=resultado_busca, estadosNav=estadoDAO.get_lista_estados(), detalhes=True)
    

