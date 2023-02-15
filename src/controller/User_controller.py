from flask import Blueprint
from flask import request,jsonify
import src.constants.http_status_codes as sts
from src.models.db import db
from src.models.User import User
from werkzeug.security import generate_password_hash,check_password_hash
from src.config.functions import validateEmail
from flask_jwt_extended import jwt_required,current_user


user = Blueprint("user",__name__,url_prefix="/api/v1/user")

@user.get('/all')
@jwt_required()
def get_all_users():
    users = User.query.all()
    formated_users= [i.format() for i in users]
    current=current_user
    return {
        'success':True,
        'count': len(formated_users),
        'users':formated_users,
        'logged_user':current.format()
    },sts.HTTP_200_OK



# Route for users registration
@user.post("/register")
def register():
    body = request.get_json()
    try:
        new_firstname  =  str(body.get('firstname',None))
        new_lastname= str(body.get('lastname',None))
        new_email = str(body.get('email',None))
        new_password = str(body.get('password',None))
        new_phone = str(body.get('phone',None))

        if len(new_password)<6:
            return jsonify({
                'error':'The specified password is two short'
            }), sts.HTTP_400_BAD_REQUEST

        if ( not new_firstname.isalnum() or (" " in new_firstname)):
            return jsonify({
                'error':'Firstname must be alphanumeric and must not contain a space'
            }),sts.HTTP_400_BAD_REQUEST

        if ( not new_lastname.isalnum() or " " in new_lastname):
            return jsonify({
                'error':'Lastname must be alphanumeric and must not contain a space'
            }),sts.HTTP_400_BAD_REQUEST

        if not validateEmail(email=new_email):
            return jsonify({
                "error":"The mail you have entered is not valid.",
            }),sts.HTTP_400_BAD_REQUEST

        if User.query.filter_by(email=new_email).first() is not None:
            return jsonify({
                'error':'Email is already taken'
            }),sts.HTTP_409_CONFLICT

        if not new_phone.isnumeric():
            return jsonify({
                'error':'The phone must contains only numeric values'
            })

        if User.query.filter_by(phone=new_phone).first() is not None:
            return jsonify({
                'error':'Phone is already in our database'
            }),sts.HTTP_409_CONFLICT


        pwd_hash = generate_password_hash(new_password)
        user = User(firstname=new_firstname,lastname=new_lastname,email=new_email,password=pwd_hash,phone=new_phone)
        db.session.add(user)

        return jsonify({
            'Success': 'user added succesfully',
            'User':user.format()
        })
    except Exception as e:
        print(e)
        db.session.rollback()
        return ({
            "error":'An error was occured',
            "message":'user not added'
        }),sts.HTTP_400_BAD_REQUEST

    finally:
        db.session.commit()

