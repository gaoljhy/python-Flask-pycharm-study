from flask import Flask
from flask_sqlalchemy import SQLAlchemy




# 创建 wblog web应用对象
wblog = Flask(__name__)






# 加载配置文件内容
wblog.config.from_object('blog.setting')  # 模块下的setting文件名，不用加py后缀

# 从外系统路径配置设定
# wblog.config.from_envvar('FLASKR_SETTINGS')  # 环境变量，指向配置文件setting的路径

# 创建数据库对象
db = SQLAlchemy(wblog)


