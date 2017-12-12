from flask import Flask,render_template,request,session,g
from flask_sqlalchemy import SQLAlchemy
import config
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

#指定登录页视图以及登录保护
login_manager.login_view = "AUTH.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page."
login_manager.login_message_category = "info"

#user_load的回调函数
@login_manager.user_loader
def load_user(user_id):
    from AUTH.models import USERS
    return USERS.query.filter_by(id=user_id).first()

from AUTH import AUTH
app.register_blueprint(AUTH)


if __name__ == '__main__':

    app.run()