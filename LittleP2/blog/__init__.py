from flask import  Flask
from blog.control import con

blg = Flask(__name__)

# 注册 control 蓝图
blg.register_blueprint(con)

