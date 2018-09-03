from blog import db


# 创建 b_users 表单
class users(db.Model):
    # 设置表名
    __tablename__ = 'b_user'

    # 设置 columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(16))

    # 设置默认初始化
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 方便调试 ，返回用户的名字
    def __repr__(self):
        return '<User %r>' % self.username
