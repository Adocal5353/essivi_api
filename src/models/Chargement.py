from src.models.db import db
import datetime


class Chargement(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime(80),default=datetime.date)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    details=db.relationship('Detail_charg')
    ventes=db.relationship('Vente',backref='chargement')
