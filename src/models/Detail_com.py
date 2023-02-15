from src.models.db  import db

class Detail_com(db.Model):
    id_produit = db.Column(db.Integer,db.ForeignKey('produit.id'),primary_key=True)
    id_commande = db.Column(db.Integer,db.ForeignKey('commande.id'),primary_key=True)
    qte=db.Column(db.Integer,default=0,nullable=False)
    prix=db.Column(db.Float)
    produit=db.relationship('Produit')