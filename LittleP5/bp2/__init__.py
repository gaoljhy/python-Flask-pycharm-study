from flask import Blueprint
from flask import render_template

bp2 = Blueprint("bps", __name__, static_folder="static", template_folder="views", url_prefix="/bp2")


@bp2.route("/")
def index():
    return render_template("p2.html")
