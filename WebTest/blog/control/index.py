from blog import wblog,db
from flask import render_template

@wblog.route("/")
def index():
    return render_template("index.ml")