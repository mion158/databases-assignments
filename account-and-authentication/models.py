from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#import db and login from app.py
from app import db, login

#user class with db.Model
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(70), index=True, unique=True)
  email = db.Column(db.String(120),index=True,unique=True)
  hashed_password = db.Column(db.String(200))
  post = db.relationship('Post', backref='author', lazy='dynamic')
  #setting password and hash it
  def set_password(self,password):
    self.hashed_password = generate_password_hash(password)
  #check passowrd
  def check_password(self,password):
    #return true if there is a match
    return check_password_hash(self.hashed_password, password) 

  def __repr__(self):
        return '<User {}>'.format(self.username)

#define user_loader to load and verify a user from database
@login.user_loader
def load_user(id):
    return User.query.get(int(id)) 

class Post():
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(140))
    country = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)