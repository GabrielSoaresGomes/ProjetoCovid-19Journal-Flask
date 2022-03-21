lista_estados = ("Acre","AC","Alagoas","AL","Amapá","AP","Amazonas","AM","Bahia","BA","Ceará","CE","Espírito Santo","ES","Goiás","GO","Maranhão","MA","Mato Grosso","MT","Mato Grosso do Sul","MS","Minas Gerais","MG","Pará","PA","Paraíba","PB","Paraná","PR","Pernambuco","PE","Piauí","PI","Rio de Janeiro","RJ","Rio Grande do Norte","RN","Rio Grande do Sul","RS","Rondônia","RO","Roraima","RR","Santa Catarina","SC","São Paulo","SP","Sergipe","SE","Tocantins","TO","Distrito Federal","DF")

class Estado:
    def __init__(self, id, estado, sigla, bandeira = None):
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
