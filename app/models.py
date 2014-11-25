from app import db
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(64), index=True, unique=True)
    last_name= db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    ctime = db.Column(db.DateTime)
    about_user = db.Column(db.String(140))
    mtime = db.Column(db.DateTime)
    posts = db.relationship('Article', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    def __repr__(self):
        return '<User %r>' % (self.email)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    ctime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class Magazine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue = db.Column(db.Integer, primary_key=True)
    ctime = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    articles = db.relationship('Article', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Post %r>' % (self.body)