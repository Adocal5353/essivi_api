from src.models.db  import db

class Detail_charg(db.Model):
    id_chargement = db.Column(db.Integer,db.ForeignKey('chargement.id'),primary_key=True)
    id_produit=db.Column(db.Integer,db.ForeignKey('produit.id'),primary_key=True)
    qte=db.Column(db.Integer,default=0)
    prix=db.Column(db.Float)
    produit=db.relationship('Produit')
