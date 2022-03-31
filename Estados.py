class Estado:
    def __init__(self, id, estado, sigla, bandeira):
        self.__id = id
        self.__estado = estado
        self.__sigla = sigla
        self.__bandeira = bandeira
    
    def get_id(self):
        return self.__id

    def get_estado(self):
        return self.__estado

    def get_sigla(self):
        return self.__sigla

    def get_bandeira(self):
        return self.__bandeira
