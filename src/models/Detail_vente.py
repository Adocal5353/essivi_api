from src.models.db  import db

class Detail_vente(db.Model):
    id_produit = db.Column(db.Integer,db.ForeignKey('produit.id'),primary_key=True)
    id_vente = db.Column(db.Integer,db.ForeignKey('vente.id'),primary_key=True)
    qte=db.Column(db.Integer,default=0,nullable=False)
    prix=db.Column(db.Float)
    produit=db.relationship('Produit')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
