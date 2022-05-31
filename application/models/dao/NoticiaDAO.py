from datetime import datetime

from application.models.entities.Noticia import Noticia
from application.models.dao import lista_noticias
from .EstadosDAO import *

class NoticiaDAO:
        def __init__(self):
                self.lista_noticias = lista_noticias
                        
        def get_noticia_lista(self):
                return self.lista_noticias

        def set_noticia_lista(self, noticia_lista):
                self.lista_noticias = noticia_lista

        def buscar_noticia(self, id_noticia):
                for noticia in self.lista_noticias:
                        if int(noticia.get_id()) == int(id_noticia):
                                noticia.views += 1
                                return noticia
                return False
        
        def get_mais_curtidas(self):
                mais_curtidas = []
                for noticia in self.get_noticia_lista:
                        if len(mais_curtidas) <= 4:
                                mais_curtidas.append(noticia)
                        elif noticia.likes > mais_curtidas[0].likes:
                                mais_curtidas.insert(0, noticia)
                        elif noticia.likes > mais_curtidas[1].likes:
                                mais_curtidas.insert(1, noticia)
                        elif noticia.likes > mais_curtidas[2].likes:
                                mais_curtidas.insert(2, noticia)
                        elif noticia.likes > mais_curtidas[3].likes:
                                mais_curtidas.insert(3, noticia)
                        elif noticia.likes > mais_curtidas[4].likes:
                                mais_curtidas.insert(4, noticia)
                nova_mais_curtidas = []
                for c in range(0,4):
                        nova_mais_curtidas.append(mais_curtidas[c])
                return nova_mais_curtidas
        
        def get_mais_vistas(self):
                mais_vistas = []
                for noticia in self.get_noticia_lista:
                        if len(mais_vistas) <= 4:
                                mais_vistas.append(noticia)
                        elif noticia.views > mais_vistas[0].views:
                                mais_vistas.insert(0, noticia)
                        elif noticia.views > mais_vistas[1].views:
                                mais_vistas.insert(1, noticia)
                        elif noticia.views > mais_vistas[2].views:
                                mais_vistas.insert(2, noticia)
                        elif noticia.views > mais_vistas[3].views:
                                mais_vistas.insert(3, noticia)
                        elif noticia.views > mais_vistas[4].views:
                                mais_vistas.insert(4, noticia)
                nova_mais_vistas = []
                for c in range(0,4):
                        nova_mais_vistas.append(mais_vistas[c])
                return nova_mais_vistas

        def get_mais_recentes(self):
                mais_recentes = []
                for noticia in self.get_noticia_lista:
                        data = datetime.strptime(noticia.get_dataPostagem(), "%d/%m/%Y")
                        if len(mais_recentes) <= 4:
                                mais_recentes.append(noticia)
                        elif data > datetime.strptime(mais_recentes[0].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(0, noticia)
                        elif data > datetime.strptime(mais_recentes[1].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(1, noticia)
                        elif data > datetime.strptime(mais_recentes[2].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(2, noticia)
                        elif data > datetime.strptime(mais_recentes[3].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(3, noticia)
                        elif data > datetime.strptime( mais_recentes[4].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(4, noticia)
                nova_mais_recentes = []
                for c in range(0,4):
                        nova_mais_recentes.append(mais_recentes[c])
                return nova_mais_recentes


