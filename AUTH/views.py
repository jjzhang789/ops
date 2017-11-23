from flask import Flask,render_template,request,redirect,url_for,session,g
from .models import USERS
from . import AUTH
from .md5pass import md5set
from .loginDecorator import logindecorator


@AUTH.route("/")

def index():
    return render_template("base.html")

@AUTH.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        password = md5set(password)
        user = USERS.query.filter(USERS.telephone==telephone,USERS.password==password).first()
        if user:
            session['username'] = user.username
            g.user = user.username
            return redirect(url_for("AUTH.index"))
        else:
            errors = "用户名或密码错误！"
            return render_template("auth/login.html",errors=errors)
    return render_template("auth/login.html")


@AUTH.route("/logout")
def logout():
    session.clear()
    return render_template('auth/login.html')


@AUTH.before_request
def my_before_request():
    username = session.get('username')
    if username:
        user = USERS.query.filter(USERS.username==username).first()
        if user:
            g.user = user.username
            g.user_id = user.id



@AUTH.context_processor
def my_context_processor():
    if hasattr(g,"user"):
        username=g.user
        return {'username':username}
    else:
        return {'username':None}

