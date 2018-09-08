from blog import wblog,db

# 项目入口调用
if __name__ == '__main__':
    # 在数据库中创建表

    # 在python 解释器中调用
    db.create_all()

    wblog.run(debug=False,port=80)
