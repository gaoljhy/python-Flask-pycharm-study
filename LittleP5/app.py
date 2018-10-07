"""
多应用 蓝图使用
"""
from flask import Flask

app = Flask(__name__)

from bp1 import bp1
from bp2 import bp2

app.register_blueprint(bp1)
app.register_blueprint(bp2)



if __name__ == '__main__':
    app.run()
