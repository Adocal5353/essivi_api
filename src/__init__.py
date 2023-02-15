from flask import Flask
import os
from src.controller.Auth_controller import auth
from src.controller.Client_controller import client
from src.models.db import db
from src.models.Client import Client
from src.models.Chargement import Chargement
from src.models.Commande import Commande
from src.models.Detail_charg import Detail_charg
from src.models.Detail_com import Detail_com
from src.models.Detail_vente import Detail_vente
from src.models.Produit import Produit
from src.models.User import User
from src.models.Ventes import Vente
from src.controller.User_controller import user
from flask_jwt_extended import JWTManager

#/*TODO: Create a runner that works*/

jwt = JWTManager()
def create_app(test_config=None):
    """
        "La grandeur, c'est de petite choses bien faite.", Ray lewis
    """
    app = Flask(__name__,
    instance_relative_config=True,
    template_folder="views")

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
        )
    else:
        app.config.from_mapping(test_config)

    db.app=app
    db.init_app(app)

    jwt.init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(client)

    return app

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()
