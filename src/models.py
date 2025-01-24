import os
import sys
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(200)) 

class Post(db.Model):
    _tablename_= 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

class Comment(db.Model):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(250))
    author_id = db.Column(db.String(250), ForeignKey('user.id'))
    post_id = db.Column(db.String(50), ForeignKey('post.id'))

class Media(db.Model):
    _tablename_ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('video', 'audio', 'image', name='media_types'), nullable=False)
    url = db.Column(db.String(250))
    post_id = db.Column(db.Integer, ForeignKey('post.id'))

class Follower(db.Model):
    _tablename_ = 'follower'
    user_from_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)







    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e