from flask import Blueprint

bp1 = Blueprint("bpf", __name__, static_folder="static", template_folder="views", url_prefix="/bp1")

from flask import render_template


@bp1.route("/")
def index():
    return render_template("p1.html")
