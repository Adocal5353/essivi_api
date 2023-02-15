from flask import Blueprint
from flask import request,jsonify
from src.models.Ventes import Vente
from src.models.db import db
import src.constants.http_status_codes as sts
from src.models.Detail_vente import Detail_vente
vente = Blueprint('vente',__name__,url_prefix="/api/v1/vente")

@vente.get("/all")
def all_vente():
    ventes = Vente.query.all()
    formated_ventes = [v.format() for v in ventes]
    return {
        "success":True,
        "ventes": formated_ventes,
        "Total":len(formated_ventes)
    }

@vente.post("/add")
def create():
    body = request.get_json()
    try:
        chargement_id = body.get("chargement",None)
        commande_id = body.get("commande_id",None)
        client_id = body.get("client_id",None)
        details = body.get("details",None)

        if details is None:
            return {
                "success":False,
                "msg":"Detils cannot be null"
            },sts.HTTP_400_BAD_REQUEST

        new_vente = Vente(chargement_id=chargement_id,commande_id=commande_id,client_id=client_id)
        new_vente.insert()

        for detail in details:
            new_detail_produit = detail.get('id_produit',None)
            new_detail_prix = detail.get('prix',None)
            new_detail_qte = detail.get('qte',None)

            new_detail = Detail_vente(id_produit=new_detail_produit,id_vente=new_vente.id,qte=new_detail_qte,prix=new_detail_prix)
            new_detail.insert()

        return {
            "success":True,
            "vente":vente
        },sts.HTTP_200_OK

    except Exception as e:
        return {
            "success":False,
            "msg": str(e),
            "vente":new_vente.format()
        },sts.HTTP_400_BAD_REQUEST

    finally:
        db.session.close()


@vente.get('/detail/<int:id>')
def get_detail_vente(id):
    try:
        one_vente = Vente.query.get(id)
        if one_vente is None:
            return {
                "success": False,
                "msg":"This vente doesn't exist"
            },sts.HTTP_404_NOT_FOUND

        return {
            "success":True,
            "vente":one_vente.format()
        },sts.HTTP_200_OK
    except:
        return{
            "success":False,
            "msg":"An error has occured"
        },sts.HTTP_400_BAD_REQUEST
