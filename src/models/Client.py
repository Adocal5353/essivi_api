from src.models.db import db
from datetime import datetime


class Client(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    phone=db.Column(db.String(80),unique=True,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    long=db.Column(db.Float,nullable=True)
    lat = db.Column(db.Float,nullable=True)
    created_at=db.Column(db.DateTime(80),default=datetime.now)
    updated_at=db.Column(db.DateTime(80),onupdate=datetime.now)
    commandes = db.relationship('Commande',backref='client')
    ventes=db.relationship('Vente',backref='client')


    def format(self):
        return {
            "name":self.name,
            "phone":self.phone,
            "user_id":self.user_id,
            "long":self.long,
            "lat":self.lat,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()