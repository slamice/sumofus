#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from models import User

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        u = User(email='dude@example.com')
        avatar = u.avatar(128)
        expected = 'http://www.gravatar.com/avatar/b4b234cd882f78ac937b1186c6002ea3?d=mm&s=128'
        assert avatar[0:len(expected)] == expected

if __name__ == '__main__':
    unittest.main()