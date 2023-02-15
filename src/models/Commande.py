from src.models.db import db
import datetime
import enum

class EtatLivraison(enum.Enum):
    En_attente = 1
    livre = 2

class Commande(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date_com = db.Column(db.DateTime(80),default=datetime.date)
    etat_com = db.Column(db.Enum(EtatLivraison),default=EtatLivraison.En_attente)
    date_livraison = db.Column(db.DateTime(80),nullable=True)
    client_id = db.Column(db.Integer,db.ForeignKey('client.id'))
    details = db.relationship('Detail_com')
    ventes =db.relationship('Vente',backref='commande')