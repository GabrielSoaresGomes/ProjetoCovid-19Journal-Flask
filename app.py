from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')


@app.route("/detalhes")
def detalhes():
	return render_template('detalhes.html')

if __name__ == "__main__":
	app.run()
