from OpsPay import db

class USERS(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(64),nullable=False)
    telephone = db.Column(db.String(64),nullable=False)
    password = db.Column(db.String(128),nullable=False)