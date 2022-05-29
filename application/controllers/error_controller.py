from flask import render_template
from application import app

@app.errorhandler(404) 
def error(e): 
  return render_template("error.html", error=True)
