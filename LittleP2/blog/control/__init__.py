from flask import Blueprint


con = Blueprint('control',__name__,template_folder="../view/demon")

from .demon.cont import index