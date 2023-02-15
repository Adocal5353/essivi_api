from src.models.db import db
from datetime import datetime

class Produit(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    reference=db.Column(db.String(80),unique=True,nullable=True)
    libelle=db.Column(db.String(80),nullable=False)
    description=db.Column(db.String(100),nullable=True)
    prix_unit=db.Column(db.Float,nullable=True)
    qte_dispo = db.Column(db.Integer,nullable=False,default=0)
    created_at=db.Column(db.DateTime(80),default=datetime.now)
    updated_at=db.Column(db.DateTime(80),onupdate=datetime.now)

    def insert(self):
        db.session.add(self)
        db.session.commit()
        self.Reference = "PO"+id
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id":self.id,
            "reference":self.reference,
            "libelle":self.libelle,
            "description":self.description,
            "prix_unit":self.prix_unit,
            "qte_dispo":self.qte_dispo,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
