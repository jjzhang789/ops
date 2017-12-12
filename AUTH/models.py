from OpsPay import db
from flask_login import AnonymousUserMixin

class USERS(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(64),nullable=False)
    telephone = db.Column(db.String(64),nullable=False)
    password = db.Column(db.String(128),nullable=False)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id