
#ESSIVI project API

_What is "essivi"? Essivi is a school which has been developed with the purpose to help water delivery men to manage their sales_

##I - Getting it work

To install this project, you need to configure some few things before getting it working on your laptop.

###1 - Preparing the environment


First, you must create a virtual environment named `myenv` in your app root folder in which you will install all the liraries that you need for the app. \
When you are in the root folder of you application in the cmd, you can type:

``` python
python -m venv myenv
```

For more informations about venv see [here](https://docs.python.org/fr/3/library/venv.html)

### 2- Install all requirements for the application

Before installing all the requirements for the application, you must verify firstly if your virtual environment is activated. If it is, you should probably see the `(venv)` mark at the beginning of your lines in the cmd. If it is not, you should go to the root of the app folder and activate it by doing so:

- In shell :

```bash
source venv/scripts/activate
```

- In command prompt/windows cmd

```bash
"venv/scripts/activate"
```

And now you can install all the libraries specified in the `requirements.txt` file by doing so:

```bash
pip install -r requirments.txt
```
 😅

### 3 - Setting up the .flaskenv file

Here is the path you must follow to do it:

```properties
export FLASK_DEBUG=1 <We set this to "1" because we are in development. If we were in production, it would be "0"
export FLASK_APP=src
export SQLALCHEMY_DB_URI=sqlite:///essivi.db <The URI> of your database
export JWT_SECRET_KEY='A secret key' <Any string you want! it is required for flask-jwt-extended>
export SECRET_KEY='Any secret key' <Also any string you want>
```

### 4 - Creating the database

To create the database, you must follow this steps

* At first you must enter the shell of flask by doing

```bash
flask shell
```

* In the shell you must import the db (instance of sqlAlchemy)

```flask
>>> from src.models.db import db
```

* Then you can create the db

```flask
>>> db.create_all()
```

Now you can launch your app by doing a

```flask
flask run
```

and check if everything is working fineeee!!👀

## Authentification
The Auth part of the app has been made with [flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/)

In the [src module init file](src/__init__.py) there is an init of `flask_jwt_extended` using `JWTManager`.

For more informations or more examples on how to use, you can [read the doc](https://flask-jwt-extended.readthedocs.io/).

For any question you can contact me
written with 💖 for you by [Adocal](https://www.github.comAdocal5353)
