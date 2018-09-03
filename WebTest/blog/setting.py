#调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#mysql数据库连接信息,这里改为自己的账号
#  SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/Pycharm"
# `MySQLdb`只支持Python2.*，还不支持3.*

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/Pycharm"