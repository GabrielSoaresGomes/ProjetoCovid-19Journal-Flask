from flask import render_template, request
from application import app
from application.models.dao import noticiaDAO
from application.models.dao import estadoDAO
from application.models.dao import comentarioDAO
from application.models.entities.Comentario import Comentario

@app.route("/detalhes/<int:id>", methods=["GET", "POST"])
def detalhes(id):
    
    if request.method == "POST":
        nome_usuario = request.form.get("nome_usuario", "")
        
        email_usuario = request.form.get("email_usuario", "")
        comentario = request.form.get("comentario", "")

        novo_comentario = Comentario(nome_usuario,email_usuario,comentario, id)
        
        comentarioDAO.adicionar_comentarios(novo_comentario)
        print(comentarioDAO.listar_comentarios())
    resultado_busca = noticiaDAO.buscar_noticia(id) 
    if resultado_busca:
        print(comentarioDAO.listar_comentarios_noticia(id))
        return render_template("detalhes.html", noticia=resultado_busca, estadosNav=estadoDAO.get_lista_estados(), detalhes=True, comentarios=comentarioDAO.listar_comentarios_noticia(id))


@app.route("/like/<int:id>/", methods=["GET"])
def curtir_noticia(id):
    noticia = noticiaDAO.buscar_noticia(id)
    if noticia.status == 2:
        noticia.retirar_avaliacao()
    else:
        noticia.avaliar_like()
        noticia.status = 2
    return render_template('detalhes.html',noticia=noticia, estadosNav=estadoDAO.get_lista_estados(), detalhes=True, comentarios=comentarioDAO.listar_comentarios_noticia(id))

@app.route("/deslike/<int:id>", methods=["GET"])
def nao_curtir(id):
    noticia = noticiaDAO.buscar_noticia(id)
    if noticia.status == 0:
        noticia.retirar_avaliacao()
    else:
        noticia.avaliar_deslike()
        noticia.status = 0
    return render_template('detalhes.html',noticia=noticia, estadosNav=estadoDAO.get_lista_estados(), detalhes=True, comentarios=comentarioDAO.listar_comentarios_noticia(id))
    
    