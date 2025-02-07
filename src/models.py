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
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    favourite_list = db.Column(db.String(50), ForeignKey('favourite.id'), nullable = False)

class Favourite(db.Model):
    __tablename__ = 'favourite'
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.Integer, nullable = False)
    type = db.Column(db.Enum('character_id', 'planet_id', 'starship_id', name="favourites_colums"), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable = False)

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    home_world = db.Column(db.String(50),ForeignKey('planets.id'), nullable = False)
    mass= db.Column(db.Integer, nullable = False) 
    hair_color= db.Column(db.String(50), nullable=False)
    eye_color=  db.Column(db.String(50), nullable = False)
    birth_year = db.Column(db.Integer, nullable=False) 
    gender = db.Column(db.String(50), nullable = False) 
    description = db.Column(db.String(5000), nullable=False)

class Starships(db.Model):
    _tablename_= 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    mlgt = db.Column(db.String(50), nullable=False)
    consumables = db.Column(db.String(50), nullable=False)
    cost_in_credits = db.Column(db.Integer, primary_key=True)
    crew = db.Column(db.String(5000), nullable=False)
    hyperdrive_rating = db.Column(db.Integer, primary_key=True)
    length  = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.Integer, nullable=False) 
    passengers = db.Column(db.String(5000), nullable=False)
    model = db.Column(db.String(5000), nullable=False)
    max_atmosphering_speed =  db.Column(db.Integer, primary_key=True)
    starship_class = db.Column(db.String(50), nullable=False)




class Planets(db.Model):
    _tablename_ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    climate =  db.Column(db.String(50), nullable=False)
    diameter = db.Column(db.Integer, primary_key=False)
    gravity = db.Column(db.Integer, primary_key=False)
    orbital_period = db.Column(db.Integer, primary_key=False)
    population = db.Column(db.Integer, primary_key=False)
    rotation_period = db.Column(db.Integer, primary_key=False)
    terrain =  db.Column(db.String(50), nullable=False)
    surface_water = db.Column(db.Integer, primary_key=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e