from src.models.db import db
import datetime
from src.models.Detail_vente import Detail_vente

class Vente(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date_vente=db.Column(db.DateTime(80),default=datetime.date)
    chargement_id = db.Column(db.Integer,db.ForeignKey('chargement.id'),nullable=True)
    commande_id = db.Column(db.Integer,db.ForeignKey('commande.id'),nullable=True)
    client_id =db.Column(db.Integer,db.ForeignKey('client.id'))
    details= db.relationship('Detail_vente')

    def format(self):
        return {
            "id":self.id,
            "date_vente":self.date_vente,
            "chargement_id":self.chargement_id,
            "commande_id":self.commande_id,
            "client_id":self.client_id,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format_all(self):
        return {
            "id":self.id,
            "date_vente":self.date_vente,
            "chargement_id":self.chargement_id,
            "commande_id":self.commande_id,
            "client_id":self.client_id,
            "details": [detail.format() for detail in self.details]
        }