from listas_python.lista_noticias import lista_noticias
from datetime import datetime


def maisCurtidas():
    mais_curtidas = []
    for noticia in lista_noticias:
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

def maisVistas():
    mais_vistas = []
    for noticia in lista_noticias:
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

def maisRecentes():
    mais_recentes = []
    for noticia in lista_noticias:
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
    