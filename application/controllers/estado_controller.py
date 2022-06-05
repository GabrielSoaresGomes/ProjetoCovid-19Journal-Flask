from flask import render_template
from application import app
from application.models.dao import estadoDAO
from application.models.dao import noticiaDAO

@app.route("/estado/<estado>")
def detalharEstado(estado):
    print(estado)
    resultado_busca_estado = estadoDAO.get_por_nome(estado)
    lista_noticias = noticiaDAO.get_noticia_lista()
    lista_estados = estadoDAO.get_lista_estados()
    if resultado_busca_estado:
        return render_template("noticia_estado.html", estado=resultado_busca_estado,noticias=lista_noticias, estadosNav=lista_estados)
    return render_template("error.html", motivo_erro="Não foi possível encontrar o estado solicitado!")