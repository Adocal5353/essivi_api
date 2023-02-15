from flask import  Blueprint
from flask import request,jsonify
from src.models.Produit import Produit

produit = Blueprint('produit',__name__,url_prefix="/api/v1/produit")

@produit.get("/all")
def all_produit():
    produits = Produit.query.all()
    formated_produit = [prod.format() for prod in produits]
    return {
        "success":True,
        "produits":formated_produit,
        "Total":len(formated_produit)
    }
