class Comentario:
  def __init__(self, nome_usuario="", email_usuario="", mensagem="", id_noticia=None):
    self._nome_usuario = nome_usuario
    self._email_usuario = email_usuario
    self._mensagem = mensagem
    self._id_noticia = id_noticia
  
  @property
  def nome_usuario(self):
    return self._nome_usuario
  
  @nome_usuario.setter
  def nome_usuario(self, nome_usuario):
    self._nome_usuario = nome_usuario

  @property
  def email_usuario(self):
    return self._email_usuario
  
  @email_usuario.setter
  def email_usuario(self, email_usuario):
    self._email_usuario = email_usuario

  @property
  def mensagem(self):
    return self._mensagem

  @mensagem.setter
  def mensagem(self, mensagem):
    self._mensagem = mensagem

  @property
  def id_noticia(self):
    return self._id_noticia
  
  @id_noticia.setter
  def id_noticia(self, id_noticia):
    self._id_noticia = id_noticia
