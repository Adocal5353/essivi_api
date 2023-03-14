from flask import Blueprint
from flask import request,jsonify
import src.constants.http_status_codes as sts
from src.models.db import db
from src.models.User import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token

auth = Blueprint("auth",__name__,url_prefix="/api/v1/auth")
@auth.get("/me")
def me():
    return {
        "user":"me",
        "name":"caleb"
    }


@auth.post('/login')
def login():
    body = request.get_json()
    try:
        new_password = str(body.get('password',None))
        new_phone = str(body.get('phone',None))
        user:User = User.query.filter_by(phone=new_phone).first()
        if user is None:
            return jsonify({
                'status': 'fail',
            }),sts.HTTP_404_NOT_FOUND
        elif check_password_hash(user.password, new_password):
            access_token = create_access_token(identity=user)
            refresh_token = create_refresh_token(identity=user)
            return jsonify({
                'status':'Success',
                'message':'User authentifiated successfully',
                'access_token':access_token,
                'refresh_token':refresh_token,
                'user':user.format()
            }),sts.HTTP_200_OK
        else:
            return jsonify({
                'status': 'fail',
                'Message':'Verify your authentification informations'
            }),sts.HTTP_400_BAD_REQUEST

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({
                'status': 'fail',
                'Message': 'Authentification failed due to an internal server error',
            }),sts.HTTP_500_INTERNAL_SERVER_ERROR