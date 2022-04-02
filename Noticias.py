from random import randint

class Noticias:

    def __init__(self, id, dataPostagem, titulo, previa, conteudo, estado):
        self.__noticia_lista = None
        self.__id = id
        self.__previa = previa
        self.__dataPostagem = dataPostagem
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__estado = estado
        self.__likes = randint(0,10000)
        self.__views = randint(0,1000000)

    def get_id(self):
        return self.__id

    def get_previa(self):
        return self.__previa

    def get_dataPostagem(self):
        return self.__dataPostagem

    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_estado(self):
        return self.__estado

    def get_noticia_lista(self):
        return self.__noticia_lista

    @property
    def likes(self):
        return self.__likes
    
    @property
    def views(self):
        return self.__views

    @views.setter
    def views(self, views):
        self.__views = views

    def set_noticia_lista(self, noticia_lista):
        self.__noticia_lista = noticia_lista
