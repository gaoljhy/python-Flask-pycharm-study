from blog.control import con
from flask import render_template

@con.route("/index")
@con.route("/")
def index():
    return render_template("index.html",
                           content="你好")