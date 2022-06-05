class EstadoDAO:
    def __init__(self, dict_estados):
        self.dict_estados = dict_estados
    
    def get_lista_estados(self):
        return self.dict_estados.values()

    def get_por_id(self,id_estado):
        for estado in self.get_lista_estados():
            if estado.get_id() == id_estado:
                return estado
        return None
    
    def get_por_sigla(self, sigla_estado):
        for estado in self.get_lista_estados():
            if estado.get_sigla() == sigla_estado:
                return estado
        return None

    def get_por_nome(self, nome_estado):
        for estado in self.get_lista_estados():
            if estado.get_estado() == nome_estado:
                return estado
        return None


