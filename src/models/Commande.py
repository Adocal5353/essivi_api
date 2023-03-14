from src.models.db import db
import datetime
import enum
from src.models.Client import Client

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

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id":self.id,
            "date_com":self.date_com,
            "etat_com":self.etat_com,
            "date_livraison":self.date_livraison,
            "client":Client.query.get(self.client_id).format()
        }