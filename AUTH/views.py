from flask import Flask,render_template,request,redirect,url_for,session,g
from .models import USERS
from . import AUTH
from .md5pass import md5set
from flask_login import login_user, logout_user, login_required
from OpsPay import db

#主页路由
@AUTH.route("/")
@login_required
def index():
    return render_template("base.html")

#登录页路由
@AUTH.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #获取电话，密码
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        password = md5set(password)
        user = USERS.query.filter(USERS.telephone==telephone,USERS.password==password).first()
        #判断登录信息并设置session
        if user:
            login_user(user)
            session['username'] = user.username
            session['telephone'] = user.telephone
            return redirect(url_for("AUTH.index"))
        else:
            errors = "用户名或密码错误！"
            return render_template("auth/login.html",errors=errors)
    return render_template("auth/login.html")

#用户信息
@AUTH.route("/adduser", methods=['GET','POST'])
def adduser():
    if request.method == 'POST':
        username = request.form.get('username')
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        #密码一致性以及手机号验证后续使用js，再次不多做纠缠
        password = md5set(password)
        user = USERS.query.filter(USERS.telephone==telephone).first()
        if user:
            errors = "手机号已存在，请使用有效的号码"
            return render_template("auth/adduser.html",errors=errors)
        else:
            user = USERS(username=username,telephone=telephone,password=password)
            db.session.add(user)
            db.session.commit()
            messages = "添加用户成功！"
            return render_template('auth/login.html',messages=messages)


    return render_template('auth/adduser.html')

#用户登出
@AUTH.route("/logout")
def logout():
    logout_user()
    return render_template('auth/login.html')

#在函数执行前设置全局变量
# @AUTH.before_request
# def my_before_request():
#     username = session.get('username')
#     if username:
#         user = USERS.query.filter(USERS.username == username).first()
#         if user:
#             g.user = user.username
#             g.user_id = user.id


#设置模板变量，此变量可以被所有模板引用，无需多次定义
@AUTH.context_processor
def my_context_processor():
    username = session.get('username')
    if username:
        telephone = session.get('telephone')
        return {'username':username,'telephone':telephone}
    else:
        return {'username':""}


