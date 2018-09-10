"""
测试 前端界面搭建与简单交互
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html',
                           title="你好",
                           content="Haha")


if __name__ == '__main__':
    app.run(debug=True)
