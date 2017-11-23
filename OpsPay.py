from flask import Flask,render_template,request,session,g
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from AUTH import AUTH
app.register_blueprint(AUTH)


if __name__ == '__main__':

    app.run()