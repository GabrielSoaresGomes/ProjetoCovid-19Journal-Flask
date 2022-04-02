from flask import Flask, render_template
from listas_python.lista_noticias import lista_noticias
from listas_python.lista_estados import lista_estados

app = Flask(__name__)



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
    

@app.errorhandler(404) 
def error(e): 
  return render_template("error.html", error=True)


@app.route("/")
def home():
    return render_template("home.html", noticias=lista_noticias, estadosNav=lista_estados,mais_vistas = nova_mais_vistas, mais_curtidas = nova_mais_curtidas)


@app.route("/detalhes/<int:id>")
def detalhes(id):
    for noticia in lista_noticias:
        if int(noticia.get_id()) == int(id):
            noticia.views += 1
            return render_template("detalhes.html", noticia=noticia, estadosNav=lista_estados, detalhes=True)


@app.route("/estado/<estado>")
def detalharEstado(estado):
    for est in lista_estados:
        if est.get_estado() == estado:
            return render_template("noticia_estado.html", estado=lista_estados[int(est.get_id())],
                                   noticias=lista_noticias, estadosNav=lista_estados)

    


# app.run(debug=True)
