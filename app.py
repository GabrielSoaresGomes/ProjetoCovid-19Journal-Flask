from flask import Flask, render_template

from Noticias import Noticias

app = Flask(__name__)

lista_noticias = [
        #       id  data postagem titulo        previa
        Noticias(0, "17/02/2004", "Lorem 00", "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto.",
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto."*10),

        Noticias(1, "23/03/2005", "Lorem 01", "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto.",
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto."*7),

        Noticias(2, "21/05/2006", "Lorem 02", "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto.",
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto."*5),

        Noticias(3, "22/05/2006", "Lorem 03", "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto.",
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere atque? Cupiditate nam natus minima iusto."*17),

    ]       

@app.route("/")
def home():
    
    return render_template("home.html", noticias=lista_noticias)


@app.route("/detalhes/<id>")
def detalhes(id):
    return render_template("detalhes.html", noticia=lista_noticias[int(id)])

