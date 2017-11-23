from flask import g,render_template,session

def logindecorator(func):
    def wraps():
        if g.user =='admin':
            return render_template("auth/login.html")
    return wraps