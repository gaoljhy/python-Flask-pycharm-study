from blog import db
from datetime import datetime

class articles(db.Model):
    # 创建表名字
    __tablename__ = 'b_articles'

    # 创建clomuns
    id = db.Column(db.Integer,autoincrement=True ,primary_key=True)
    title = db.Column(db.String(20),unique=True)
    content = db.Column(db.Text)
    time = db.Column(db.DateTime)

    def __init__(self,title,content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<article %>'% self.title



