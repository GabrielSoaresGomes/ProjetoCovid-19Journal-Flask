from flask import Flask, render_template
from Noticias import Noticias
from Estados import Estado
from lista_noticias import lista_noticias

app = Flask(__name__)


lista_estados = [
    Estado(0, "Acre", "AC", "static/img/bandeiras/acre.png"),
    Estado(1, "Alagoas", "AL", "static/img/bandeiras/alagoas.png"),
    Estado(2, "Amapá", "AP", "static/img/bandeiras/amapa.png"),
    Estado(3, "Amazonas", "AM", "static/img/bandeiras/amazonas.png"),
    Estado(4, "Bahia", "BA", "static/img/bandeiras/bahia.png"),
    Estado(5, "Ceará", "CE", "static/img/bandeiras/ceara.png"),
    Estado(6, "Espírito Santo", "ES", "static/img/bandeiras/espiritosanto.png"),
    Estado(7, "Goiás", "GO", "static/img/bandeiras/goias.png"),
    Estado(8, "Maranhão", "MA", "static/img/bandeiras/maranhao.png"),
    Estado(9, "Mato Grosso", "MT", "static/img/bandeiras/matogrosso.png"),
    Estado(10, "Mato Grosso do Sul", "MS", "static/img/bandeiras/matogrossodosul.png"),
    Estado(11, "Minas Gerais", "MG", "static/img/bandeiras/minasgerais.png"),
    Estado(12, "Pará", "PA", "static/img/bandeiras/para.png"),
    Estado(13, "Paraíba", "PB", "static/img/bandeiras/paraiba.png"),
    Estado(14, "Paraná", "PR", "static/img/bandeiras/parana.png"),
    Estado(15, "Pernambuco", "PE", "static/img/bandeiras/pernambuco.png"),
    Estado(16, "Piauí", "PI", "static/img/bandeiras/piaui.png"),
    Estado(17, "Rio de Janeiro", "RJ", "static/img/bandeiras/riodejaneiro.png"),
    Estado(18, "Rio Grande do Norte", "RN", "static/img/bandeiras/riograndedonorte.png"),
    Estado(19, "Rio Grande do Sul", "RS", "static/img/bandeiras/riograndedosul.png"),
    Estado(20, "Rondônia", "RO", "static/img/bandeiras/rondonia.png"),
    Estado(21, "Roraima", "RR", "static/img/bandeiras/roraima.png"),
    Estado(22, "Santa Catarina", "SC", "static/img/bandeiras/santacatarina.png"),
    Estado(23, "São Paulo", "SP", "static/img/bandeiras/saopaulo.png"),
    Estado(24, "Sergipe", "SE", "static/img/bandeiras/sergipe.png"),
    Estado(25, "Tocantins", "TO", "static/img/bandeiras/tocantins.png"),
    Estado(26, "Distrito Federal", "DF", "static/img/bandeiras/distritofederal.png"),
]


@app.route("/")
def home():
    return render_template("home.html", noticias=lista_noticias, estados=lista_estados, home=True)


@app.route("/detalhes/<id>")
def detalhes(id):
    for noticia in lista_noticias:
        if int(noticia.get_id()) == int(id):
            return render_template("detalhes.html", noticia=lista_noticias[int(id)])


@app.route("/estado/<estado>")
def detalharEstado(estado):
    for est in lista_estados:
        if est.get_estado() == estado:
            return render_template("noticia_estado.html", estado=lista_estados[int(est.get_id())],
                                   noticias=lista_noticias)



app.run(debug=True)