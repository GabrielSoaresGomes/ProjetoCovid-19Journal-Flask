class ComentarioDAO:
  def __init__(self):
    self._lista_comentarios = []

  def listar_comentarios(self):
    return self._lista_comentarios
  
  def adicionar_comentarios(self, comentario):
    self._lista_comentarios.append(comentario)
  
  def listar_comentarios_noticia(self, id_noticia):
    comentarios = []
    for comentario in self.listar_comentarios():
      if int(comentario.id_noticia) == int(id_noticia):
        comentarios.append(comentario)
    return comentarios