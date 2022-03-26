class Noticias:

    def __init__(self, id, dataPostagem, titulo, previa, conteudo, estado=None):
        self.__id = id
        self.__previa = previa
        self.__dataPostagem = dataPostagem
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__estado = estado

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
