from flask import Blueprint
from flask import request,jsonify
import src.constants.http_status_codes as sts
from src.models.db import db
from src.models.User import User
from werkzeug.security import generate_password_hash,check_password_hash
from src.config.functions import validateEmail
from src.models.Client import Client
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user

client = Blueprint('client',__name__,url_prefix='/api/v1/client')

@client.get('/all')
@jwt_required()
def all_client():
    clients=Client.query.all()
    formated_client=[client.format for client in clients]
    return jsonify({
        'success':True,
        'count':len(formated_client),
        'clients':formated_client
    }),sts.HTTP_200_OK

@client.get('/one/<int:id>')
def one_client(id):
    client = Client.query.get(id)

    if client is None:
        return jsonify({
            'success':False,
            'msg':'User not found'
        }),sts.HTTP_404_NOT_FOUND
    return jsonify({
        'success':True,
        'client_id':id,
        'client':client
    }),sts.HTTP_200_OK

@client.post('/add')
@jwt_required()
def add_client():
    body=request.get_json()

    new_name = body.get('name',None)
    new_phone = body.get('phone',None)
    new_long = body.get('long',None)
    new_lat = body.get('lat',None)
    _user_id = current_user.id


    if new_name is None or new_phone is None:
        return jsonify({
            'success':True,
            'Msg':'Both the name and the phone number must not be null'
        }),sts.HTTP_400_BAD_REQUEST

    client = Client(name=new_name,phone=new_phone,long=new_long,lat=new_lat,user_id=_user_id)

    client.insert()

    return jsonify({
        'success':True,
        'Msg':'User created successfully',
        'client':client.format()
    }),sts.HTTP_200_OK

