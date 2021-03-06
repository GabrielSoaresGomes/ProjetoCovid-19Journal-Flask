from random import randint

class Noticia:

    def __init__(self, id, dataPostagem, titulo, previa, conteudo, estado, imagem="https://via.placeholder.com/286x286"):
        self.__noticia_lista = None
        self.__id = id
        self.__previa = previa
        self.__dataPostagem = dataPostagem
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__imagem = imagem
        self.__estado = estado
        self.__likes = randint(0,10000)
        self.__deslikes = randint(0, 10000)
        self.__views = randint(0,1000000)
        self.__status = 1 # Não avaliado

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

    def get_imagem(self):
        return self.__imagem

    def retirar_avaliacao(self):
        if self.__status == 2:
            self.__likes -= 1
        else:
            self.__deslikes -= 1
        self.__status = 1

    def avaliar_like(self):
        if self.__status == 1:
            self.__likes += 1
        else:
            self.__deslikes -= 1
            self.__likes += 1
    
    def avaliar_deslike(self):
        if self.__status == 1:
            self.__deslikes += 1
        else:
            self.__deslikes += 1
            self.__likes -= 1
            

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, numero_likes):
        self.__deslikes = numero_likes

    @property
    def deslikes(self):
        return self.__deslikes
    
    @deslikes.setter
    def deslikes(self, numero_deslikes):
        self.__deslikes = numero_deslikes

    @property
    def views(self):
        return self.__views

    @views.setter
    def views(self, views):
        self.__views = views

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status
        