
DEBUG = True

#数据库配置

DIALECT = 'mysql'
#使用pymysql驱动
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'ops'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SECRET_KEY = 'sdgHJsfdgGewofFGdf/b,ceSDgshDsrg[df'