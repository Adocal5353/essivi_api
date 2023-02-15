import enum
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Enum
from src.models.db import db

class MyEnum(enum.Enum):
    admin = 1
    gerant = 2
    vendeur = 3


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(80),nullable=True)
    lastname=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(80),nullable=True)
    password=db.Column(db.Text(80),unique=False,nullable=False)
    phone=db.Column(db.String(80),unique=True,nullable=False)
    role = db.Column(db.Enum(MyEnum), nullable=True)
    created_at=db.Column(db.DateTime(80),default=datetime.now)
    updated_at=db.Column(db.DateTime(80),onupdate=datetime.now)
    clients=db.relationship('Client',backref="user")
    chargement=db.relationship('Chargement',backref='user')


    def format(self):
        """
            Return the formated-in-json value of the class User
        """
        return {
            'id':self.id,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'email':self.email,
            'phone':self.phone,
            'hashed_password':self.password,
            'created_at':self.created_at,
            'updated_at':self.updated_at,
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()

